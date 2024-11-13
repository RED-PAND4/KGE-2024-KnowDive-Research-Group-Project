import json
import re

# Function to extract names from the source JSON
def extract_names(source_json):
    # Open and load the source JSON file
    with open(source_json, 'r') as file:
        data = json.load(file)
    
    # Extract the list of names (assuming each entity has 'name' and 'surname' fields)
    #names = [f"{item['Course name']}" for item in data]
    names = [re.sub(r"\s*\(.*?\)", "", item['Course Name']).strip()for item in data]
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
        if f"{item['nome']}" in names_list
    ]
    
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
            "nome" : entry["nome"],
            "descrizione" : entry["descrizione"],
            "docenti" : entry["docenti"],
            "assistenti" : entry["assistenti"],
            "titolari" : entry["titolari"],
            "sitoWeb" : entry["sitoWeb"]
        }
        new_data.append(new_entry)

    return new_data

# Function to save the filtered data to a new file
def save_filtered_data(filtered_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)

# Example usage
source_json = '/home/deborah/Documenti/uni magistrale/KGE/KGE-Project/Phase 2 - Information Gathering/Data values dataset/KRG-UNITN-courses.json'  # JSON file with names
target_json = '/home/deborah/Documenti/uni magistrale/KGE/KGE-Project/Phase 2 - Information Gathering/Data values dataset/not-cleaned dataset/DU-UNITN-courses.json'  # JSON file to be filtered
output_file = '/home/deborah/Documenti/uni magistrale/KGE/KGE-Project/Phase 2 - Information Gathering/Data values dataset/Cleaned-DU-UNITN-courses.json'  # File to save filtered data

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
