import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to add 'leader_of' field to each entry
def add_leader_of_field(input_file, output_file):
    # Load the JSON data
    data = load_json(input_file)

    # Iterate through each entry and add the 'leader_of' field
    for entry in data:
        # Initialize the 'leader_of' field as an empty list (or you can set it to any default value)
        entry['researchTopic_name'] = ["Language Diversity"]

    # Save the updated data back to the file
    save_json(output_file, data)

# Example usage
input_file = 'Aligned-KRG-UNITN-research-products-LanguageDiversity.json'  # JSON file with the original data
output_file = 'researchProduct2.json'  # JSON file to save the updated data

add_leader_of_field(input_file, output_file)
