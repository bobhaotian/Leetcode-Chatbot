import csv
import json

# Define the input and output file names
input_csv = 'leetcode_python.csv'
output_json = 'data.json'

# Open the CSV file and the output JSON file
with open(input_csv, mode='r') as csvfile, open(output_json, mode='w') as jsonfile:
    csvreader = csv.DictReader(csvfile)
    
    # Iterate over the first 90 rows
    for idx, row in enumerate(csvreader):
        if idx >= 90:
            break
        
        # Construct the message list for each row
        message = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a programmer who needs to answer programming questions in Python"
                },
                {
                    "role": "user",
                    "content": f"{row['Question']}\n{row['Examples']}"
                },
                {
                    "role": "assistant",
                    "content": row['Solution']
                }
            ]
        }
        
        # Write each message as a separate JSON object
        jsonfile.write(json.dumps(message, indent=4))
        jsonfile.write('\n')

print(f"Data successfully written to {output_json}")
