def student_name(name): # Validates the name of the student
    return all(char.isalpha() or char in ["'", " "] for char in name) and name.strip() != ""

def student_grade(grade): # Validate the grade of the student
    if grade.isdigit():
        grade = int(grade)
        if 0 <= grade <= 100:
            return True
    else:
        return False

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

    if student_grade(grade):
        break
    else:
        print("Invalid Grade. Please enter a valid grade.")