import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Function to create a mapping from person identifier to research product names
def create_identifier_to_product_mapping(products_file):
    products_data = load_json(products_file)
    identifier_to_products = {}

    # Build dictionary with identifier as key and list of research products as values
    for product in products_data:
        product_name = product["name"]
        for participant in product.get("author", []):
            if participant not in identifier_to_products:
                identifier_to_products[participant] = []
            identifier_to_products[participant].append(product_name)

    return identifier_to_products

# Function to add research product names to each person
def add_research_products_to_people(people_file, products_file, output_file):
    # Load people data
    people_data = load_json(people_file)

    # Create identifier-to-research-product mapping
    identifier_to_products = create_identifier_to_product_mapping(products_file)

    # Update each person's `researchProduct_name`
    for person in people_data:
        person_id = person["identifier"]
        person["researchProduct_name"] = identifier_to_products.get(person_id, [])

    # Save updated people data
    save_json(output_file, people_data)

# Example usage
people_file = 'person.json'  # JSON file containing people
products_file = 'researchProduct.json'  # JSON file containing research products
output_file = 'person2.json'  # Output file with added research product names

add_research_products_to_people(people_file, products_file, output_file)
