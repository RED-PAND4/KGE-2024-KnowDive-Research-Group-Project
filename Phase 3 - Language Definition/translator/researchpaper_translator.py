import json
def drop_fields(source_json):
    # Open and load the target JSON file
    # with open(json_file, 'r') as file:
    #    data = json.load(file)

    with open(source_json, 'r') as file:
        data = json.load(file)

    new_data = []
    for entry in data:
        new_entry = {
            "name": entry["titolo"],
            "type": entry["tipo"],
            "year": entry["anno"],
            "language": entry["lingua"],
            "author": entry["autori"],
            "file": entry["file"]
        }
        new_data.append(new_entry)

    return new_data


# Function to save the filtered data to a new file
def save_filtered_data(filtered_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)

# Function to integrate and translate multiple jsons
def combine_and_translate (source_name, years):
    final_data = []
    for year in years:
        new_source_name = source_name + year + ".json"
        data_list = drop_fields(new_source_name)
        for entry in data_list:
            final_data.append(entry)

    return final_data



# Example usage
sources = [
    "./Cleaned-DU-UNITN-esearch-prducts-ArtHumCog-",
    "./Cleaned-DU-UNITN-esearch-prducts-HumMacSymb-",
    "./Cleaned-DU-UNITN-esearch-prducts-KnowDiver-",
    "./Cleaned-DU-UNITN-esearch-prducts-LangDiver-"
]
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]

outputs = [
    "./Translated-DU-UNITN-research-products-ArtificialHumanCognition.json",
    "./Translated-DU-UNITN-research-products-HumanMachineSymbiosis.json",
    "./Translated-DU-UNITN-research-products-KnowledgeDiversity.json",
    "./Translated-DU-UNITN-research-products-LanguageDiversity.json"
]

for i in [0,1,2,3]:
    to_save = combine_and_translate(sources[i], years)
    save_filtered_data(to_save, outputs[i])
    print("Saved"+str(i))

