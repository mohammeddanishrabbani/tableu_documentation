# Tableau Dashboard Documentation Generator

This project provides an automated solution for generating business-friendly documentation for Tableau dashboards (.twbx files). It extracts metadata from Tableau workbooks and uses Google Gemini Pro (via LangChain) to generate detailed markdown documentation. The project also includes an AI-powered evaluator to assess and improve the quality of generated documentation.

## Features
- **Automated Extraction:** Unzips Tableau .twbx files and parses embedded .twb XML for metadata.
- **AI-Powered Documentation:** Uses Google Gemini Pro LLM to generate clear, structured documentation.
- **Documentation Evaluation:** Evaluates and improves generated documentation for completeness, clarity, and accuracy using an LLM-based evaluator.
- **Customizable Prompts:** Easily modify prompt templates for different documentation or evaluation styles.
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
    evaluator.py         # Evaluates and improves documentation quality
  prompts/
    doc_prompt.txt       # Prompt template for documentation
    doc_prompt_v2.txt    # Alternate prompt template
    evaluator.txt        # Prompt template for documentation evaluation
extracted/               # Temporary extraction directory for .twbx contents
generated_documents/     # Output markdown documentation
```

## Installation
1. Clone the repository.
2. Install dependencies:
   ```zsh
   pip install -r requirements.txt
   ```
3. Set your Google API key as an environment variable:
   ```zsh
   export GOOGLE_API_KEY=your_api_key_here
   ```

## Usage
Run the main script to generate and evaluate documentation from a Tableau .twbx file:
```zsh
python src/main.py -input path/to/dashboard.twbx -output path/to/output.md
```
- `-input`: Path to the Tableau .twbx file
- `-output`: Path to the output markdown file

The script will:
1. Extract metadata from the Tableau .twbx file
2. Generate business-friendly documentation using an LLM
3. Evaluate and improve the documentation for completeness and clarity
4. Save the final markdown to the specified output path

## Documentation Evaluation
The evaluator checks for:
- Presence of all required sections (Overview, Purpose, Business Questions, Audience, Data Sources, etc.)
- Clarity and business-friendliness
- Accuracy of metrics and definitions
- Mention of visuals/examples where appropriate
- Assumptions and limitations

Prompt templates for evaluation can be found in `src/prompts/evaluator.txt`.

## Example Output
See the `generated_documents/` folder for sample documentation files, including both initial and evaluated versions.

## Customization
- **Prompt Templates:** Edit `src/prompts/doc_prompt.txt`, `doc_prompt_v2.txt`, or `evaluator.txt` to change the documentation or evaluation style.
- **LLM Model:** The model can be changed in `src/llm/generator.py` and `src/llm/evaluator.py`.

## Requirements
- Python 3.9+
- Google Gemini Pro API access (API key)

## License
MIT License
