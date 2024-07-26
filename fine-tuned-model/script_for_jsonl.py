import json

# Read the file content
with open('data.json', 'r') as file:
    content = file.read()

# Step 1: Split the content
split_content = content.split('}\n{')
split_content = [section if i == 0 else '{' + section + '}' for i, section in enumerate(split_content)]

# Step 2: Parse each section and format as JSONL
jsonl_lines = []
for section in split_content:
    try:
        json_obj = json.loads(section)
        jsonl_lines.append(json.dumps(json_obj))
    except json.JSONDecodeError:
        print(f"Failed to parse section: {section[:50]}...")

# Step 3: Write to a new JSONL file
with open('data.jsonl', 'w') as jsonl_file:
    for line in jsonl_lines:
        jsonl_file.write(line + '\n')

# Indicate the process completion and provide the path to the new JSONL file
print("Processing completed. The JSONL file is available at: data.jsonl")
