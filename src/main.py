from src.extractors.tableu_parser import TableauTWBXExtractor
from src.llm.generator import DocumentationGenerator
import os
import argparse
# Set the Google API key as an environment variable

os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"  # Replace with your actual API key


def main(twbx_path, output_path):
    print("📥 Extracting dashboard metadata...")
    parser = TableauTWBXExtractor(twbx_path)
    parser.unzip_twbx()
    metadata = parser.extract_metadata()
    print("✅ Metadata Extracted")

    print("\n🤖 Generating documentation using Gemini Pro...")
    doc_gen = DocumentationGenerator()
    documentation = doc_gen.generate(metadata)
    print("✅ Documentation Generated")

    with open(output_path, "w") as f:
        f.write(documentation)
    print(f"📄 Documentation written to '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Tableau dashboard documentation.")
    parser.add_argument("-input", help="Path to the Tableau TWBX file")
    parser.add_argument("-output", help="Path to output markdown file")
    args = parser.parse_args()
    main(args.input, args.output)
