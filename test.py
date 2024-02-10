import json
import difflib

# Function to compare instructions
def compare_instructions(instruction1, instruction2):
    similarity_ratio = difflib.SequenceMatcher(None, instruction1, instruction2).ratio()
    return similarity_ratio

# Read data from JSONL file
filePath = 'prompts/alpha.jsonl'
data = []
with open(filePath, 'r') as file:
    for line in file:
        data.append(json.loads(line))

# Compare instructions for each pair of cases
similar_cases = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        instruction1 = data[i]['instruction']
        instruction2 = data[j]['instruction']
        similarity_ratio = compare_instructions(instruction1, instruction2)
        if similarity_ratio > 0.8:  # Adjust the threshold as needed
            similar_cases.append((i, j, similarity_ratio))

# Print similar cases
if similar_cases:
    print("Similar cases found:")
    for case in similar_cases:
        print(f"Cases {case[0]+1} and {case[1]+1} have a similarity ratio of {case[2]}")
else:
    print("No similar cases found.")
