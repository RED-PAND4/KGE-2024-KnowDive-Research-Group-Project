import json

#function to drop fields from the Research Topic dataset
def drop_fields(json_file):

    # Open and load the target JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    new_data = []
    for entry in data:
        new_entry = {
            "Name" : entry["Name"],
            "Lead by" : entry["Lead by"],
            "Members" : entry["Members"],
            "Projects" : entry["projects"]
        }
        new_data.append(new_entry)

    return new_data

# Function to save the filtered data to a new file
def save_filtered_data(filtered_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)


input_file = "./KRG-UNITN-research-topics.json"
output_file = "./KRG-UNITN-research-topics_cleaned.json"

new_data = drop_fields(input_file)
save_filtered_data(new_data, output_file)
