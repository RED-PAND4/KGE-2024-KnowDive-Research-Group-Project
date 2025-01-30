import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Function to create a mapping from author name to identifier
def create_author_mapping(authors_file):
    authors_data = load_json(authors_file)
    name_to_id = {}

    # Build a dictionary with author name as key and identifier as value
    for entry in authors_data:
        full_name = f"{entry['surname']+" "+ entry['name'][0] }"
        name_to_id[full_name] = entry["identifier"]

    return name_to_id

# Function to replace author names with identifiers
def replace_authors_with_identifiers(publications_file, authors_file, output_file):
    # Load publications data
    publications_data = load_json(publications_file)

    # Create author-to-identifier mapping
    author_to_id = create_author_mapping(authors_file)

    # Iterate through publications and replace author names
    for publication in publications_data:
        publication["author"] = [author_to_id.get(author, author) for author in publication["author"]]

    # Save updated publications data
    save_json(output_file, publications_data)

# Example usage
publications_file = 'researchProduct6.json'  # JSON file containing publication details
authors_file = 'person.json'  # JSON file containing author names and identifiers
output_file = 'researchProduct7.json'  # Output file with replaced author names

replace_authors_with_identifiers(publications_file, authors_file, output_file)
