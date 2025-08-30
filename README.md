# Corporate Res### Single Company Report

```bash
python runOpenAIPromptForDocx.py --prompt "template.txt" --sub "CORPORATE_NAME=Apple Inc." "TARGET_DATE=August 30, 2025" --model "gpt-3.5-turbo"
```

Note: The batch script automatically formats dates as "Month DD, YYYY" (e.g., "August 30, 2025") for optimal readability in the generated report.

Arguments:eport Generator

This tool generates detailed company reports using OpenAI's GPT model, with support for both single and batch report generation.

## Features

- Generate formatted DOCX reports with Markdown-style formatting
- Support for batch processing multiple companies
- Customizable prompts with variable substitution
- Smart logging with daily log files
- Configurable OpenAI model selection
- Duplicate report detection and skipping

## Usage

### Single Company Report

```bash
python generateDocxCompanyReport.py --prompt "template.txt" --sub "CORPORATE_NAME=Apple Inc." "TARGET_DATE=08302025" --model "gpt-3.5-turbo"
```

Arguments:
- `--prompt`: Template file or string to send to OpenAI (supports variable substitution)
- `--sub`: Key-value pairs for variable substitution in the format:
  - `CORPORATE_NAME`: Company name (e.g., "Apple Inc.")
  - `TARGET_DATE`: Date in MMDDYYYY format (e.g., "08302025" for August 30, 2025)
- `--prompt`: Template file or string to send to OpenAI (supports variable substitution)
- `--sub`: Key-value pairs for variable substitution (format: "KEY=value")
- `--model`: OpenAI model to use (default: gpt-3.5-turbo)

### Batch Processing

```bash
python batchGenerateCompanyReports.py
```

The batch script:
- Reads a list of companies to process
- Calls the main report generator for each company
- Handles any errors during batch processing
- Maintains the same formatting and structure across all reports

## Output

Reports are generated in the `out` directory with the naming format: `company_report_COMPANY_NAME.docx`

Logs are written to the `logs` directory with daily rotation: `report_log_YYYY-MM-DD.txt`

## Markdown Support

The report generator supports:
- Headers (H1-H3) using #, ##, ###
- Bold text using **bold**
- Bulleted lists using -
- Automatic page breaks before Appendix and References sections

## Environment Setup

1. Install required packages:
```bash
pip install openai python-docx python-dotenv
```

2. Set up your OpenAI API key in a `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

## Project Structure

- `runOpenAIPromptForDocx.py` - Main report generation script
- `batchGenerateCompanyReports.py` - Batch processing script
- `out/` - Generated DOCX reports
- `logs/` - Daily log files
