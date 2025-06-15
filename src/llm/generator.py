from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.globals import set_debug
import logging
# set_debug(True)  # Enable debug mode for detailed logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DocumentationGenerator:
    def __init__(self):
        logger.info("Initializing DocumentationGenerator with Google Gemini Pro model.")
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
        )

        logger.info("Loading prompt template for documentation generation.")
        prompt_template = PromptTemplate(
            input_variables=["metadata"],
            template=open("src/prompts/doc_prompt.txt").read()
        )
        self.chain  = prompt_template | self.llm | StrOutputParser()

    def generate(self, metadata: dict) -> str:
        logger.info("Generating documentation from metadata.")
        if not metadata:
            logger.error("Metadata is empty. Cannot generate documentation.")
            return "No metadata provided to generate documentation."
        response = self.chain.invoke({"metadata": metadata})
        logger.info(f"Generated response: {response}")
        return response
