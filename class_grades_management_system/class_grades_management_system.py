def student_name(name): # Validates the name of the student
    return all(char.isalpha() or char in ["'", " "] for char in name) and name.strip() != ""

def student_grade(grade): # Validate the grade of the student
    if not grade.isdigit():
        return False

name = input("Please enter the student's name: ")
grade = input("Please enter the student's grade: ")