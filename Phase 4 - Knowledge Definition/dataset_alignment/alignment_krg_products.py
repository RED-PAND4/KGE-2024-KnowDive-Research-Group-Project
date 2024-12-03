import json


# Function to save the filtered data to a new file
def save_filtered_data(filtered_data, output_file):
    with open(output_file, 'w') as file:
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
            "name": entry["Name"],
            "howpublished": entry["Publication"],
            "author": entry["Authors"],
            "file": entry["Note/Links"]
        }
        new_data.append(new_entry)

    return new_data

def combine_and_translate (source_name, suffix):
    final_data = []
    for year in suffix:
        new_source_name = source_name + year + ".json"
        data_list = drop_fields(new_source_name)
        for entry in data_list:
            final_data.append(entry)

    return final_data

# Example usage
sources = [
    "./KRG-UNITN-research-prducts-ArtHumCog",
    "./KRG-UNITN-research-products-HumMacSymb",
    "./KRG-UNITN-research-products-KnowDiver",
    "./KRG-UNITN-research-products-LangDiver"
]
suffix = [""]

outputs = [
    "./Aligned-KRG-UNITN-research-products-ArtificialHumanCognition.json",
    "./Aligned-KRG-UNITN-research-products-HumanMachineSymbiosis.json",
    "./Aligned-KRG-UNITN-research-products-KnowledgeDiversity.json",
    "./Aligned-KRG-UNITN-research-products-LanguageDiversity.json"
]

if len(sources) == len(outputs):
    for i in range(len(sources)):
        to_save = combine_and_translate(sources[i], suffix)
        save_filtered_data(to_save, outputs[i])
        print("Saved"+str(i))