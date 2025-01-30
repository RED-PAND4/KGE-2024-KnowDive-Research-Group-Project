import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to retain only 'identifier' and 'endDate' fields
def filter_fields(input_file, output_file):
    # Load the JSON data
    data = load_json(input_file)

    # Iterate over the data and keep only 'identifier' and 'endDate' fields
    filtered_data = []
    for entry in data:
        filtered_entry = {key: entry[key] for key in ['identifier', 'endDate'] if key in entry}
        filtered_data.append(filtered_entry)

    # Save the filtered data back to the file
    save_json(output_file, filtered_data)

# Example usage
input_file = 'alumni.json'  # JSON file with original data
output_file = 'alumni2.json'  # JSON file to save the filtered data

filter_fields(input_file, output_file)
