from src.extractors.tableu_parser import TableauTWBXExtractor
from src.llm.generator import DocumentationGenerator
from src.llm.evaluator import Evaluator
import os
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

# Set the Google API key as an environment variable

os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"  # Replace with your actual API key


def main(twbx_path, output_path):
    logger.info("📥 Extracting dashboard metadata...")
    parser = TableauTWBXExtractor(twbx_path)
    parser.unzip_twbx()
    metadata = parser.extract_metadata()
    logger.info("✅ Metadata Extracted")

    logger.info("🤖 Generating documentation using Gemini Pro...")
    doc_gen = DocumentationGenerator()
    documentation = doc_gen.generate(metadata)
    logger.info("✅ Documentation Generated")

    if not documentation:
        logger.warning("⚠️ No documentation generated. Please check the input metadata.")
        return
    
    logger.info("Starting evaluation of generated documentation.")

    evaluator = Evaluator()
    evaluated_documentation = evaluator.evaluate(documentation, metadata)
    if evaluated_documentation:
        logger.info("🔍 Evaluation Result:")
        logger.info(evaluated_documentation)


    with open(output_path, "w") as f:
        f.write(evaluated_documentation)
    logger.info(f"📄 Documentation written to '{output_path}'")
    parser.cleanup()
    logger.info("✅ Cleanup completed. Process finished successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Tableau dashboard documentation.")
    parser.add_argument("-input", help="Path to the Tableau TWBX file")
    parser.add_argument("-output", help="Path to output markdown file")
    args = parser.parse_args()
    main(args.input, args.output)
