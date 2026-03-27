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
    
def caps(value):
    value.lower()
    value.capitalize()
    

def add_student(name, year): 
    students[name] = {"year": year, "credits": [0, 0, 0, 0]}

def add_student_credits(lists, grade, amount):
    lists[grade] += amount

def grade_loop(loopcount):
    if loopcount == 0:
        return "Not achieved"
    elif loopcount == 1:
        return "Achieved"
    elif loopcount == 2:
        return "Merit"
    elif loopcount == 3:
        return "Excellence"
    

def display_info():
    for student, status in students.items():
        print(student)
        for info in status.values():
            print(info)

'''
INTERFACE CODE -----------------------------------------------------------------------
'''
while interface == True:
    task = validation(input("What would you like to do? \n1. View students | 2. Add student | 3. Edit student | 4. End task " ))
    if task == 1:
        display_info()
    elif task == 2:
        name = caps(input('What name is the new student? '))
        year = validation(input("What year level is the new student? "))
        add_student(name, year)
        for i in range(4):
            add_student_credits(students[name]["credits"], i, validation(input(f"How many {grade_loop(i)}s does {name} have? ")))
    elif task == 3:
        selected = caps(input("Which student do you want to edit?"))
        if selected in students:
            for detail in students.get(selected).values():
                print(detail)
        else:
            print("That student does not exist.")
    elif task == 4:interface = False
    else:print("Invalid input")
