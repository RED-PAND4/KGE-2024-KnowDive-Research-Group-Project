import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Function to create a mapping from researchTopic_name to project_name
def create_research_topic_to_project_mapping(projects_file):
    projects_data = load_json(projects_file)
    topic_to_project = {}

    # Build dictionary with researchTopic_name as key and project_name as values
    for project in projects_data:
        for topic in project.get("researchTopic_name", []):
            if topic not in topic_to_project:
                topic_to_project[topic] = []
            topic_to_project[topic].append(project["name"])

    return topic_to_project

# Function to add project_name field to research topics
def add_project_names_to_research_topics(research_topics_file, projects_file, output_file):
    # Load research topics data
    research_topics_data = load_json(research_topics_file)

    # Create research topic to project mapping
    topic_to_project = create_research_topic_to_project_mapping(projects_file)

    # Update each research topic entry with project names
    for research_topic in research_topics_data:
        topic_name = research_topic["name"]
        research_topic["project_name"] = topic_to_project.get(topic_name, [])

    # Save updated research topics data
    save_json(output_file, research_topics_data)

# Example usage
research_topics_file = 'researchTopic.json'  # JSON file containing research topics
projects_file = 'project.json'  # JSON file containing project details
output_file = 'researchTopic2.json'  # Output file with added project names

add_project_names_to_research_topics(research_topics_file, projects_file, output_file)
