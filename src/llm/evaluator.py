from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.globals import set_debug
import logging
# set_debug(True)  # Enable debug mode for detailed logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Evaluator:
    def __init__(self):
        logger.info("Initializing Evaluator with Google Gemini Pro model.")
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
        )

        logger.info("Loading prompt template for documentation generation.")
        prompt_template = PromptTemplate(
            input_variables=["metadata"],
            template=open("src/prompts/evaluator.txt").read()
        )
        self.chain  = prompt_template | self.llm | StrOutputParser()

    def evaluate(self, documentation: str, metadata: dict) -> str:
        logger.info("Evaluating documentation against metadata.")
        if not documentation or not metadata:
            logger.error("Documentation or metadata is empty. Cannot evaluate.")
            return "No documentation or metadata provided for evaluation."
        response = self.chain.invoke({"metadata": metadata, "documentation": documentation})
        logger.info(f"Evaluation response: {response}")
        return response