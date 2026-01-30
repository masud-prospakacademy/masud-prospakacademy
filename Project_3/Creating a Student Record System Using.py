
student_records = {}

def add_student(student_id, name, major, gpa):
    student_details = {
        "name": name, 
        "major": major, 
        "gpa": gpa
    }
    student_records[student_id] = student_details
    print(f"Student {name} (ID: {student_id}) added successfully.")

def view_student(student_id):
    if student_id in student_records:
        student = student_records[student_id]
        print(f"\n--- Student Details for ID: {student_id} ---")
        print(f"Name:  {student['name']}")
        print(f"Major: {student['major']}")
        print(f"GPA:   {student['gpa']:.2f}")
    else:
        print(f"Error: Student ID '{student_id}' not found.")

def update_gpa(student_id, new_gpa):
    if student_id in student_records:
        student_records[student_id]["gpa"] = new_gpa
        print(f"Updated: Student {student_id} GPA is now {new_gpa:.2f}.")
    else:
        print(f"Error: Student ID '{student_id}' not found.")

def list_all_students():
    if not student_records:
        print("No student records available.")
        return

    print("\n--- All Student Records ---")
    for s_id, details in student_records.items():
        print(f"ID: {s_id} | Name: {details['name']:<15} | GPA: {details['gpa']:.2f}")
    print("-" * 35)

add_student("S001", "Masud", "Web Development", 3.8)
add_student("S002", "Asmau", "MicroBiology", 3.2)
add_student("S003", "Sulaiman", "Arts", 3.9)

view_student("S001")
update_gpa("S002", 3.5)

list_all_students()
