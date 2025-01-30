import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Function to create a mapping from research topics to research product names
def create_research_product_mapping(research_product_file):
    research_products = load_json(research_product_file)
    topic_to_products = {}

    # Build dictionary with research topic as key and list of research product names as values
    for product in research_products:
        product_name = product["name"]
        for topic in product.get("researchTopic_name", []):
            if topic not in topic_to_products:
                topic_to_products[topic] = []
            topic_to_products[topic].append(product_name)

    return topic_to_products

# Function to add research product names to each research topic
def add_research_products_to_topics(research_topic_file, research_product_file, output_file):
    # Load research topics data
    research_topics = load_json(research_topic_file)

    # Create research topic-to-product mapping
    topic_to_products = create_research_product_mapping(research_product_file)

    # Update each research topic's `researchProduct_name` field
    for topic in research_topics:
        topic_name = topic["name"]
        topic["researchProduct_name"] = topic_to_products.get(topic_name, [])

    # Save updated research topics data
    save_json(output_file, research_topics)

# Example usage
research_topic_file = 'researchTopic.json'  # JSON file containing research topics
research_product_file = 'researchProduct.json'  # JSON file containing research products
output_file = 'researchTopic2.json'  # Output file with added research product names

add_research_products_to_topics(research_topic_file, research_product_file, output_file)
