def student_name(name): # Validates the name of the student
    return all(char.isalpha() or char in ["'", " ", "."] for char in name) and name.strip() != ""

def student_grade(grade): # Validate the grade of the student
    if grade.isdigit():
        grade = int(grade)
        if 0 <= grade <= 100:
            return True
    else:
        return False

class_record = []

while True:
    # A loop that will continue asking until a valid name is input
    while True:
        name = input("Please enter the student's name: ")

        if student_name(name):
            break
        else:
            print("Invalid Name. Please enter a valid name.")

    # A loop that will continue asking until a valid grade is input
    while True:
        grade = input("Please enter the student's grade: ")
        valid_grade = student_grade(grade)

        if valid_grade:
            break
        else:
            print("Invalid Grade. Please enter a valid grade.")

    class_record.append({"name": name, "grade": int(grade)})

    # A loop that for adding another student
    while True:
        another = input("Do you want to add another student? Yes or No: ")
        if another.lower() == "yes" or another.lower() == "no":
            if another in ["Yes", "No"]:
                break
            else:
                print("Invalid")
        else:
            print("Invalid input. Please type Yes or No.")

    if another == "No":
        break

if class_record:
    top_student = class_record[0]  # Assume the first student has the highest grade
    for student in class_record:
        if student["grade"] > top_student["grade"]:
            top_student = student  # Update top_student if current student has a higher grade
    print(f"The student with the highest grade is {top_student['name']} with a grade {top_student['grade']}.")
else:
    print("No data collected.")

if class_record:
    lowest_student = class_record[0]
    for student in class_record:
        if student["grade"] < lowest_student["grade"]:
            lowest_student = student
    print(f"The student with the lowest grade is {lowest_student['name']} with a grade {lowest_student['grade']}.")
else:
    print("No data collected.")

total_grades = sum(student["grade"] for student in class_record)
average_grade = total_grades / len(class_record)

print(f"The average grade of all students is {average_grade:.2f}")


