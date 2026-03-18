'''
SETUP CODE ----------------------------------------------------------------------------
'''
interface = True
#DICTIONARY ------------------------------------------------------------
students = {#student names
    "Albert": {
        "year": 12,
        "credits": [0, 4, 9, 7] #not achieved, achieved, merit, excelence
    },
    "Jerald":{
        "year": 11,
        "credits": [11, 3, 1, 2]
    },
    "Sarah":{
        "year": 11,
        "credits": [2, 5, 6, 5]
    }
}
#FUNCTION --------------------------------------------------------------
def validation(value):
    try:
        valid = int(value)
        return valid
    except ValueError:
        return "X"

def add_student(name, year, credits): 
    students[name] = {"year": year, "credits": credits}

def add_student_credits(NA, A, M, E):
    credits = [NA, A, M, E]
    return credits

def display_info():
    for student, info in students.items():
        print(student)
        for detail in info:
            print(detail)

'''
INTERFACE CODE -----------------------------------------------------------------------
'''
while interface == True:
    task = validation(input("What would you like to do? \n1. View students | 2. Add student | 3. End task"))
    if task == 1:
        display_info()

    elif task == 3:
        interface == False
    else:print("Invalid number")