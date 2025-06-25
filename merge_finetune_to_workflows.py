import csv
import os

WORKFLOWS_CSV = 'workflows.csv'
FINETUNE_CSV = 'finetune_dataset.csv'
OUTPUT_CSV = 'workflows.csv'  # Overwrite workflows.csv with merged data

# Read workflows from a CSV file
def read_workflows(csv_path):
    workflows = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get('workflow_name')
            code = row.get('json_code')
            if name and code:
                workflows[name] = code
    return workflows

# Read both CSVs
def main():
    workflows = {}
    if os.path.exists(WORKFLOWS_CSV):
        workflows.update(read_workflows(WORKFLOWS_CSV))
    if os.path.exists(FINETUNE_CSV):
        workflows.update(read_workflows(FINETUNE_CSV))

    # Write merged workflows back to workflows.csv
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['workflow_name', 'json_code'])
        writer.writeheader()
        for name, code in workflows.items():
            writer.writerow({'workflow_name': name, 'json_code': code})
    print(f"Merged {len(workflows)} unique workflows into {OUTPUT_CSV}")

if __name__ == '__main__':
    main() 