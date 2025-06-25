import os
import csv
import json

# Set the root directory to the current directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_CSV = os.path.join(ROOT_DIR, 'workflows.csv')

workflows = []

for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    for filename in filenames:
        if filename.lower().endswith('.txt'):
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Try to parse as JSON
                    try:
                        json.loads(content)
                    except Exception:
                        continue  # Skip files that are not valid JSON
                    # Escape double quotes for CSV
                    content_escaped = content.replace('"', '""')
                    workflow_name = os.path.splitext(filename)[0]
                    workflows.append({
                        'workflow_name': workflow_name,
                        'json_code': content_escaped
                    })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

# Write to CSV with proper quoting
with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['workflow_name', 'json_code']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for wf in workflows:
        writer.writerow(wf)

print(f"Exported {len(workflows)} valid workflows to {OUTPUT_CSV}") 