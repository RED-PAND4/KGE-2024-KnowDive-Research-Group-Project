import json

# Function to extract names from the source JSON
def extract_names(source_json):
    # Open and load the source JSON file
    with open(source_json, 'r') as file:
        data = json.load(file)
    
    # Extract the list of names (assuming each entity has 'name' and 'surname' fields)
    names = [f"{item['Name']}" for item in data]
    return names

# Function to filter the target JSON by matching name
def filter_by_names(target_json, names_list):
    # Open and load the target JSON file
    with open(target_json, 'r') as file:
        data = json.load(file)
    
    # Extract the 'data' list from the 'value' field
    data_list = data['value']['data']
    
    # Filter entities that match any name in the names_list
    filtered_data = [
        item for item in data_list
        if f"{item['titolo']}" in names_list
    ]

    #filtered_data = []
    #for item in data_list:
        # Check if any author in the 'autori' field matches a name in names_list
    #    if any(f"{author['nome']} {author['cognome']}" in names_list for author in item.get('autori', [])):
    #        filtered_data.append(item)
    
    # Update the 'data' field with the filtered list
    data['value']['data'] = filtered_data
    
    return data

def drop_fields(data):

    # Open and load the target JSON file
    #with open(json_file, 'r') as file:
    #    data = json.load(file)

    # Extract the 'data' list from the 'value' field
    data_list = data['value']['data']

    new_data = []
    for entry in data_list:
        new_entry = {
            "titolo" : entry["titolo"],
            "tipo" : entry["tipo"],
            "anno" : entry["anno"],
            "lingua" : entry["lingua"],
            "autori" : entry["autori"],
            "file" : entry["file"]
        }
        new_data.append(new_entry)

    return new_data

# Function to save the filtered data to a new file
def save_filtered_data(filtered_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)

# Example usage
source_json = '/home/deborah/Documenti/uni magistrale/KGE/KGE-Project/Phase 2 - Information Gathering/Data values dataset/KRG-UNITN-research-products/KRG-UNITN-research-products-KnowDiver.json'  # JSON file with names
target_json = '/home/deborah/Documenti/uni magistrale/KGE/KGE-Project/Phase 2 - Information Gathering/Data values dataset/not-cleaned dataset/Research paper/DU-UNITN-mindprod-2016.json'  # JSON file to be filtered
output_file = '/home/deborah/Documenti/uni magistrale/KGE/KGE-Project/Phase 2 - Information Gathering/Data values dataset/Cleaned Research paper/Cleaned-DU-UNITN-esearch-prducts-KnowDiver-2016.json'  # File to save filtered data

# Extract names from the source file
names_list = extract_names(source_json)
#print(names_list)


# Filter the target data based on the names
filtered_data = filter_by_names(target_json, names_list)
#print(filtered_data)
new_data = drop_fields(filtered_data)

# Save the filtered data to the output file
save_filtered_data(new_data, output_file)

print(f"Filtered data has been saved to {output_file}")
