import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to create a mapping from name to identifier
def create_name_to_identifier_mapping(source_file):
    # Load the source JSON containing identifiers
    source_data = load_json(source_file)
    name_to_id = {}

    # Build the dictionary with name as the key and identifier as the value
    for entry in source_data:
        name = entry["name"] + " " + entry["surname"]
        identifier = entry["identifier"]
        name_to_id[name] = identifier

    return name_to_id

# Function to substitute names with corresponding identifiers
def substitute_names_with_identifiers(target_file, source_file):
    # Load the target JSON (the one with names to substitute)
    target_data = load_json(target_file)

    # Create a mapping from names to identifiers
    name_to_id = create_name_to_identifier_mapping(source_file)

    # Iterate through the target data and substitute names
    for entry in target_data:
        # Substitute the 'Leader' field
        if entry['Leader'] in name_to_id:
            entry['Leader'] = name_to_id[entry['Leader']]

        # Substitute the 'member' list
        entry['member'] = [name_to_id.get(member, member) for member in entry['member']]

    # Save the updated target data back to the file
    save_json(target_file, target_data)

# Example usage
target_file = 'researchTopic.json'  # JSON file containing projects with names to substitute
source_file = 'person.json'    # JSON file containing people with names and identifiers

substitute_names_with_identifiers(target_file, source_file)
