#  4,You are building a small student grade system.
#     Write a function:
#               get_grade(student_grades, student_name)
#     It should:
#     Try to return the student’s grade from a dictionary
#      If the student does not exist, catch the exception and return:
#     "Student not found in the system"
def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
        if student_name not in student_grades:
            raise KeyError("Student not found in the system")   
    except KeyError:
        return "Student not found in the system"