import json

# Function to transform data
def transform_data(input_file, output_file):
    try:
        # Load the input JSON file
        with open(input_file, "r") as f:
            data = json.load(f)

        # Transform the data
        transformed = []
        for entry in data:
            new_entry = {
                "identifier": entry.get("identifier", ""),
                "support_role": entry.get("support_role", ""),
                "researchTopic_name": entry.get("researchTopic", ""),
                "email": entry.get("Email", ""),
                "courses_id": ""
            }
            transformed.append(new_entry)

        # Save the transformed data to the output JSON file
        with open(output_file, "w") as f:
            json.dump(transformed, f, indent=4)

        print(f"Transformed data saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{input_file}' is not a valid JSON file.")

# Specify input and output file paths
input_file = "zoldmember.json"  # Replace with the path to your input JSON file
output_file = "member2.json"  # Replace with the desired path for the output JSON file

# Execute the transformation
transform_data(input_file, output_file)
