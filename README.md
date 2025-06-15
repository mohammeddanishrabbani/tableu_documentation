# Tableau Dashboard Documentation Generator

This project provides an automated solution for generating business-friendly documentation for Tableau dashboards (.twbx files). It extracts metadata from Tableau workbooks and uses Google Gemini Pro (via LangChain) to generate detailed markdown documentation.

## Features
- **Automated Extraction:** Unzips Tableau .twbx files and parses embedded .twb XML for metadata.
- **AI-Powered Documentation:** Uses Google Gemini Pro LLM to generate clear, structured documentation.
- **Customizable Prompts:** Easily modify prompt templates for different documentation styles.
- **Markdown Output:** Produces ready-to-use markdown files for sharing or publishing.

## Project Structure
```
requirements.txt
src/
  main.py                # Entry point for CLI usage
  extractors/
    tableu_parser.py     # Extracts and parses Tableau workbook metadata
  llm/
    generator.py         # Handles LLM-based documentation generation
  prompts/
    doc_prompt.txt       # Prompt template for documentation
    doc_prompt_v2.txt    # Alternate prompt template
extracted/               # Temporary extraction directory for .twbx contents
generated_documents/     # Output markdown documentation
```

## Installation
1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set your Google API key as an environment variable:
   ```sh
   export GOOGLE_API_KEY=your_api_key_here
   ```

## Usage
Run the main script to generate documentation from a Tableau .twbx file:
```sh
python src/main.py -input path/to/dashboard.twbx -output path/to/output.md
```

- `-input`: Path to the Tableau .twbx file
- `-output`: Path to the output markdown file

## Requirements
- Python 3.9+
- Google Gemini Pro API access (API key)

## Example Output
See the `generated_documents/` folder for sample documentation files.

## Customization
- **Prompt Templates:** Edit `src/prompts/doc_prompt.txt` or `doc_prompt_v2.txt` to change the documentation style or structure.
- **LLM Model:** The model can be changed in `src/llm/generator.py`.

## License
MIT License
