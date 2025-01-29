import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Function to create a mapping from name to identifier
def create_name_to_identifier_mapping(source_file):
    source_data = load_json(source_file)
    name_to_id = {}

    # Build a dictionary with full name as key and identifier as value
    for entry in source_data:
        full_name = entry["name"] + " " + entry["surname"]
        name_to_id[full_name] = entry["identifier"]

    return name_to_id

# Function to replace names with identifiers in the project data
def substitute_names_with_identifiers(projects_file, people_file, output_file):
    # Load project data
    projects_data = load_json(projects_file)

    # Create name-to-identifier mapping
    name_to_id = create_name_to_identifier_mapping(people_file)

    # Iterate through projects and replace names with identifiers
    for project in projects_data:
        # Replace projectCoordinator if found in the mapping
        if project["projectCoordinator"] in name_to_id:
            project["projectCoordinator"] = name_to_id[project["projectCoordinator"]]

        # Replace members in the 'member' list
        project["member"] = [name_to_id.get(member, member) for member in project["member"]]

    # Save updated project data
    save_json(output_file, projects_data)

# Example usage
projects_file = 'project.json'  # JSON file containing project details
people_file = 'person.json'  # JSON file containing people details (name + identifier)
output_file = 'project2.json'  # Output JSON with replaced identifiers

substitute_names_with_identifiers(projects_file, people_file, output_file)
