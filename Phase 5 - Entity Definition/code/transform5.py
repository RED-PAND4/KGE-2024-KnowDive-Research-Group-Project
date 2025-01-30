import json

# Function to load JSON from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to save JSON to a file
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to add course ids to teachers
def add_courses_to_teachers(courses_file, teachers_file):
    # Load the courses and teachers data
    courses_data = load_json(courses_file)
    teachers_data = load_json(teachers_file)

    # Create a dictionary for easy lookup of courses by their id
    courses_by_id = {course['id']: course for course in courses_data}

    # Iterate over the teachers and add the course ids to the 'courses_id' field
    for teacher in teachers_data:
        # Initialize an empty list for courses_id if not already present
        teacher['courses_id'] = []

        # Iterate over each course in the courses data
        for course in courses_data:
            # If the teacher's identifier is in the course's teacher list, add the course id to courses_id
            if teacher['identifier'] in course.get('teacher_id', []):
                teacher['courses_id'].append(course['id'])
        
        # Print the teacher's name and their associated course ids
        #print(f"Added courses for {teacher['name']} {teacher['surname']}: {teacher['courses_id']}")

    # Save the updated teachers data with the courses_id field
    save_json(teachers_file, teachers_data)

# Example usage
courses_file = 'courses.json'  # JSON file containing course details
teachers_file = 'member.json'  # JSON file containing teacher details

add_courses_to_teachers(courses_file, teachers_file)
