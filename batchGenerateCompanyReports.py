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

# Today's date in YYYY-MM-DD format
today = datetime.datetime.now().strftime("%Y-%m-%d")

for company in company_names:
    # Prepare substitutions
    substitutions = [f"CORPORATE_NAME={company}", f"TARGET_DATE={today}"]
    # Build the command
    cmd = [
        "python",
        "generateDocxCompanyReport.py",
        "--prompt", template_prompt,
        "--sub"
    ] + substitutions
    print(f"Generating report for {company}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
