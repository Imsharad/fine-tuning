import json
import re
import csv

def extract_soql_queries(file_path):
    soql_queries = []
    
    with open(file_path, 'r') as file:
        for line in file:
            try:
                data = json.loads(line)
                messages = data.get('messages', [])
                for message in messages:
                    if message['role'] == 'assistant':
                        content = message['content']
                        # Use regex to find SOQL queries
                        queries = re.findall(r'SELECT\s+.+?(?=\s*$)', content, re.IGNORECASE | re.DOTALL)
                        soql_queries.extend(queries)
            except json.JSONDecodeError:
                continue
    
    return soql_queries

# Usage
file_path = 'SOQL_samples.md'
queries = extract_soql_queries(file_path)

# Save queries to CSV file
output_file = 'soql_queries.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['soql'])  # Write header
    for query in queries:
        writer.writerow([query.strip()])

print(f"SOQL queries have been saved to {output_file}")