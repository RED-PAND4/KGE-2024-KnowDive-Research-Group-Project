import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to substitute identifier
def substitute_identifier(source_file, target_file):
    # Load source and target JSON files
    source_data = load_json(source_file)
    target_data = load_json(target_file)

    # Iterate through the source JSON to get the identifier
    for source_entry in source_data:
        source_name = source_entry["name"]
        source_surname = source_entry["surname"]
        source_identifier = source_entry["identifier"]

        # Find the matching person in the target file by name and surname
        for target_entry in target_data:
            target_name = target_entry["name"]
            target_surname = target_entry["surname"]

            if source_name == target_name and source_surname == target_surname:
                # Substitute the identifier in the target entry
                target_entry["identifier"] = source_identifier
                print(f"Updated identifier for {source_name} {source_surname}")
                break

    # Save the updated target JSON
    save_json(target_file, target_data)

# Example usage
source_file = 'person.json'  # JSON file containing identifiers
target_file = 'member.json'  # JSON file where identifiers need to be substituted

substitute_identifier(source_file, target_file)
