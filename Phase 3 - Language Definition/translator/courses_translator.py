import json
def translate(source_json):
    # Open and load the target JSON file
    # with open(json_file, 'r') as file:
    #    data = json.load(file)

    with open(source_json, 'r') as file:
        data = json.load(file)

    new_data = []
    for entry in data:
        new_entry = {
            "name": entry["nome"],
            "description": entry["descrizione"],
            "teacher": entry["docenti"],
            "assistants": entry["assistenti"],
            "holder": entry["titolari"],
            "webpage" : entry["sitoWeb"]
        }
        new_data.append(new_entry)

    return new_data


# Function to save the filtered data to a new file
def save_filtered_data(filtered_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)



# Example usage
sources = "./Cleaned-DU-UNITN-courses.json"

outputs = "./Translated-DU-UNITN-courses.json"

to_save = translate(sources)
save_filtered_data(to_save, outputs)