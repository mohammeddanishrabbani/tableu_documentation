import streamlit as st
import os
from src.extractors.tableu_parser import TableauTWBXExtractor
from src.llm.generator import DocumentationGenerator
from src.llm.evaluator import Evaluator
import tempfile

st.set_page_config(page_title="Tableau Documentation Generator", layout="wide")
st.title("📊 Tableau Dashboard Documentation Generator & Evaluator")

st.markdown("""
Upload a Tableau `.twbx` file to automatically generate and evaluate business-friendly documentation using Google Gemini Pro.
""")

api_key = st.text_input("Enter your Google API Key", type="password", value=os.environ.get("GOOGLE_API_KEY", ""))
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key

uploaded_file = st.file_uploader("Upload Tableau .twbx file", type=["twbx"])

if uploaded_file and api_key:
    with tempfile.TemporaryDirectory() as tmpdir:
        twbx_path = os.path.join(tmpdir, uploaded_file.name)
        with open(twbx_path, "wb") as f:
            f.write(uploaded_file.read())
        
        st.info("Extracting dashboard metadata...")
        parser = TableauTWBXExtractor(twbx_path, extract_dir=os.path.join(tmpdir, "extracted"))
        parser.unzip_twbx()
        metadata = parser.extract_metadata()
        st.success("Metadata extracted.")

        st.info("Generating documentation with Gemini Pro...")
        doc_gen = DocumentationGenerator()
        documentation = doc_gen.generate(metadata)
        st.success("Documentation generated.")

        st.info("Evaluating documentation...")
        evaluator = Evaluator()
        evaluated_doc = evaluator.evaluate(documentation, metadata)
        st.success("Documentation evaluated and improved.")

        st.subheader("📄 Evaluated Documentation")
        st.markdown(evaluated_doc)

        st.download_button(
            label="Download Markdown",
            data=evaluated_doc,
            file_name="tableau_documentation.md",
            mime="text/markdown"
        )
else:
    st.warning("Please provide your Google API Key and upload a .twbx file.")
