import csv
import json

# Read the CSV file
csv_file = 'prompts.csv'
csv_contents = []
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        csv_contents.append(row)

# Convert the CSV contents to JSON
json_content = []
for row in csv_contents:
    json_content.append({
        'key': row[0],
        'value': row[1]
    })

# Export to JSON file
json_file = 'prompts.json'
with open(json_file, 'w') as file:
    json.dump(json_content, file, indent=2)
