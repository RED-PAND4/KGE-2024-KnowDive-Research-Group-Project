import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to create a mapping from teacher name to identifier
def create_teacher_id_mapping(source_file):
    # Load the source JSON containing the identifiers
    source_data = load_json(source_file)
    teacher_to_id = {}

    # Build a dictionary where the key is the teacher name and the value is the identifier
    for entry in source_data:
        teacher_name = entry["name"] + " " + entry["surname"]
        teacher_identifier = entry["identifier"]
        teacher_to_id[teacher_name] = teacher_identifier

    return teacher_to_id

# Function to substitute teacher names with identifiers in the course data
def substitute_teacher_names(course_file, source_file):
    # Load course data and teacher-to-id mapping
    course_data = load_json(course_file)
    teacher_to_id = create_teacher_id_mapping(source_file)

    # Iterate through each course and replace teacher names with their identifiers
    for course in course_data:
        teacher_ids = course["teacher_id"]

        # Replace teacher names with identifiers
        course["teacher_id"] = [teacher_to_id.get(teacher, teacher) for teacher in teacher_ids]

        print(f"Updated teacher ids for course: {course['name']}")

    # Save the updated course data
    save_json(course_file, course_data)

# Example usage
course_file = 'courses.json'  # JSON file containing courses
source_file = 'person.json'  # JSON file containing teachers with their identifiers

substitute_teacher_names(course_file, source_file)
