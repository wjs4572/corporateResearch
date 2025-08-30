import subprocess
import datetime
import os

# List of company names to generate reports for
# company_names = [
# "Apple Inc.",
# "Microsoft Corporation",
# "Alphabet Inc.",
# "Amazon.com, Inc.",
# "Meta Platforms, Inc."
# ]
company_names = [
 "Apple Inc.",
]

# Path to the template file
template_path = os.path.join(os.path.dirname(__file__), "prompts", "corporateReport-Template.pgsql")

# Read the template prompt
with open(template_path, "r", encoding="utf-8") as f:
    template_prompt = f.read()

# Format today's date in a natural language format that works well in the prompt
today = datetime.datetime.now().strftime("%B %d, %Y")  # e.g., "August 30, 2025"

for company in company_names:
    # Prepare substitutions
    substitutions = [f"CORPORATE_NAME={company}", f"TARGET_DATE={today}"]
    # Build the command
    cmd = [
        "python",
        "runOpenAIPromptForDocx.py",
        "--prompt", template_prompt,
        "--sub"
    ] + substitutions
    print(f"Generating report for {company}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
