import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Function to map person identifier to their projects
def map_person_to_projects(projects_file):
    projects_data = load_json(projects_file)
    person_projects = {}

    # Iterate through each project
    for project in projects_data:
        project_name = project["name"]
        members = project.get("member_id", [])
        coordinator = project.get("projectCoordinator_id", "")

        # Add project to members and coordinator
        for person in members + [coordinator]:  
            if person:  # Ensure it's not empty
                if person in person_projects:
                    person_projects[person].append(project_name)
                else:
                    person_projects[person] = [project_name]

    return person_projects

# Function to update people.json with project names
def add_projects_to_people(people_file, projects_file, output_file):
    # Load people and projects data
    people_data = load_json(people_file)
    person_to_projects = map_person_to_projects(projects_file)

    # Update people's project_name field
    for person in people_data:
        person_id = person["identifier"]
        if person_id in person_to_projects:
            person["project_name"] = person_to_projects[person_id]
        else:
            person["project_name"] = []

    # Save the updated data
    save_json(output_file, people_data)

# Example usage
people_file = 'person.json'  # JSON file containing people details
projects_file = 'project.json'  # JSON file containing project details
output_file = 'person2.json'  # Output JSON with project names added

add_projects_to_people(people_file, projects_file, output_file)
