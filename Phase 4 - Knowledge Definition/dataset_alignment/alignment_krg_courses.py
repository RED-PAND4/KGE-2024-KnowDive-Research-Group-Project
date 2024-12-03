import json


# Function to save the filtered data to a new file
def save_filtered_data(filtered_data, output_file):
    target_file = output_file + ".json"
    with open(target_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)

def drop_fields(source_json):
    # Open and load the target JSON file
    # with open(json_file, 'r') as file:
    #    data = json.load(file)

    with open(source_json, 'r') as file:
        data = json.load(file)

    new_data = []
    for entry in data:
        new_entry = {
            "name": entry["Course Name"],
            "teacher": entry["Teachers"],
            "year": entry["Year"],
            "University": entry["University"],
            "website": entry["Webpage"]
        }
        new_data.append(new_entry)

    return new_data

def combine_and_translate (source_name, suffix):
    final_data = []
    for suff in suffix:
        new_source_name = source_name + suff + ".json"
        data_list = drop_fields(new_source_name)
        for entry in data_list:
            final_data.append(entry)

    return final_data

# Example usage
sources = [
    "./KRG-UNITN-courses"
]
suffix = [""]

outputs = [
    "./Aligned-KRG-UNITN-courses"
]

if len(sources) == len(outputs):
    for i in range(len(sources)):
        to_save = combine_and_translate(sources[i], suffix)
        save_filtered_data(to_save, outputs[i])
        print("Saved"+str(i))