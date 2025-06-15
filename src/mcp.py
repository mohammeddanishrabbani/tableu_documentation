# MCP Server to Generate Consumer-Friendly Documentation for Tableau Dashboards

# Prerequisites:
# - Install LangChain, FastAPI, Gemini SDK, and Tableau-related Python packages
# - Ensure you have access to the Gemini API with multimodal support
# - Assumes `.twbx` file parsing capability (requires unzipping and XML parsing)

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import uvicorn
import os
import zipfile
import xml.etree.ElementTree as ET
from tempfile import TemporaryDirectory
from langchain.llms import GooglePalm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

app = FastAPI(title="MCP Server - Tableau Dashboard Documentor")

# --- CONFIGURATION ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Use secure storage in production

# Load Gemini LLM via LangChain
llm = GooglePalm(google_api_key=GEMINI_API_KEY, temperature=0.4)

prompt_template = PromptTemplate(
    input_variables=["dashboard_meta"],
    template="""
You are an expert in creating user-friendly documentation for data dashboards.
Based on the following metadata extracted from a Tableau dashboard, generate a Markdown-formatted documentation for business stakeholders.

Metadata:
{dashboard_meta}

Include:
1. Dashboard Overview
2. Purpose and Business Questions
3. Target Audience
4. Data Sources
5. Key Metrics and Filters
6. Charts/Visuals with Brief Explanations

Return output in Markdown format.
"""
)

documentation_chain = LLMChain(llm=llm, prompt=prompt_template)

# --- HELPER FUNCTIONS ---
def extract_metadata_from_twbx(twbx_file_path: str) -> str:
    with TemporaryDirectory() as tmpdirname:
        with zipfile.ZipFile(twbx_file_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdirname)

        # Find the .twb file inside
        twb_files = [f for f in os.listdir(tmpdirname) if f.endswith('.twb')]
        if not twb_files:
            return "No .twb file found inside .twbx."

        twb_path = os.path.join(tmpdirname, twb_files[0])
        tree = ET.parse(twb_path)
        root = tree.getroot()

        # Extract metadata: datasources, worksheets, dashboards, etc.
        meta_parts = []

        # Example: Extract datasources
        for ds in root.findall('.//datasource'):
            meta_parts.append(f"Datasource Name: {ds.attrib.get('name')}")

        # Example: Extract worksheets
        for worksheet in root.findall('.//worksheet'):
            meta_parts.append(f"Worksheet Name: {worksheet.attrib.get('name')}")

        # Example: Extract dashboards
        for dashboard in root.findall('.//dashboard'):
            meta_parts.append(f"Dashboard Name: {dashboard.attrib.get('name')}")

        return "\n".join(meta_parts)

# --- API ENDPOINT ---
@app.post("/generate-documentation/")
async def generate_documentation(file: UploadFile = File(...)):
    if not file.filename.endswith(".twbx"):
        return {"error": "Only .twbx Tableau files are supported."}

    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    try:
        metadata = extract_metadata_from_twbx(temp_file_path)
        doc_markdown = documentation_chain.run(dashboard_meta=metadata)
        return {"documentation": doc_markdown}
    except Exception as e:
        return {"error": str(e)}
    finally:
        os.remove(temp_file_path)

# --- RUN SERVER ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
