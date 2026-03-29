'''
Variables, Dictionaries and Functions ----------------------------------------------------------------------------
'''
interface = True
#DICTIONARY ------------------------------------------------------------
students = {
    "Albert": { #name of student is the key of said students' data
        "year": 12, #The year level of the student
        "credits": [11, 35, 43] #The credits the student has, in order from Achieved, Merit, and Excellence.
    },
    "Jerald":{
        "year": 11,
        "credits": [24, 14, 9]
    },
    "Sarah":{
        "year": 11,
        "credits": [15, 24, 50]
    }
}
#FUNCTION --------------------------------------------------------------
#Validify intergers, otherwise return with a 0
def validation(value): 
    try:
        valid = int(value)
        return valid
    except ValueError:
        return 0

'''
Adds new student entry to the dictionary
name is the name of the student, and it becomes the key for the students' data.
year is the year level of the student.
A list with 3 values is used for credits. Another function is called in the interface section of the code which sets the values for the student credits.
'''
def add_student(name, year): 
    students[name] = {"year": year, "credits": [0, 0, 0]}

'''
When called, this will add the 'amount' to the specified part of the list in the students' credits. 
lists holds the value of the selected student that is having their credits edited
grade is the grade that is being updated. 0 means achieved, 1 means merit, and 2 means excellence.
amount is the amount of credits is being added to the selected student.
'''
def add_student_credits(lists, grade, amount):
    lists[grade] += amount

#This code is used in loops to get the correct grade name corrosponding to the grade being printed. Easier to understand in areas where it's used.
def grade_loop(loopcount):
    if loopcount == 0:
        return "Achieved"
    elif loopcount == 1:
        return "Merit"
    elif loopcount == 2:
        return "Excellence"
   

    
'''
INTERFACE CODE -----------------------------------------------------------------------
'''
while interface == True: #loops infinitally, unless 'task' gets a value of 4, which sets interface to False and ends the loop.
    task = validation(input("What would you like to do? \n1. View students | 2. Add student | 3. Edit student | 4. End task " )) #input
    if task == 1: #View student groups
        category = validation(input("Do you want to view only a set group of students? \n1. View all students | 2. View students who passed | 3. View students with endorsed merit | 4. View students with endorsed excellence | 5. View students from a year level "))
        if category == 1: #prints all students
            for student, status in students.items():
                print(f"{student} | year {status['year']}, credits {status['credits']}")
                #Prints the student name, followed by their year level and all of their credits
        elif category == 2: #prints all students with total credits from all grades at least 80 or more
            for student, status in students.items():
                total = sum(status['credits'])
                if total >= 80:
                    print(f"{student} | year {status['year']}, credits {status['credits']}")
        elif category == 3: #prints all students with total credits from merit and excellence, adding up to 50 or more
            for student, status in students.items():
                total = sum(status['credits'])
                merits = total - status['credits'][0]
                if merits >= 50:
                    print(f"{student} | year {status['year']}, credits {status['credits']}")
        elif category == 4:#prints all students with at least 50 excellence credits
            for student, status in students.items():
                excellence = status['credits'][2]
                if excellence >= 50:
                    print(f"{student} | year {status['year']}, credits {status['credits']}")
        elif category == 5: #prints students in specific year groups
            yeargroup = 0 #defaulted to 0 in order to loop. validation returns with 0 if invalid.
            while yeargroup > 13 or yeargroup < 11: #year group ranges between 11 to 13
                yeargroup = validation(input("What year group? Year 11, 12 or 13? ")) 
                if yeargroup > 13 or yeargroup < 11: 
                    print("Invalid year level")
            
            for student, status in students.items(): #checking for student in the selected year group. Ignores students outside of year group
                if status['year'] == yeargroup:
                    print(f"{student} | year {status['year']}, credits {status['credits']}")
        else:print("Invalid")               

    elif task == 2: #Adds a new student
        name = input('What name is the new student? ').capitalize() 
        if name in students: #invalidates new names if a student with the same name exists
            print("That student already exists. Please put an extra letter or symbol to their name.")
        else:
            year = 0
            while year > 13 or year < 11:
                year = validation(input("What year level is the new student? "))
                if year > 13 or year < 11:print("Invalid")
            add_student(name, year)
            for i in range(3):
                add_student_credits(students[name]['credits'], i, validation(input(f"How many {grade_loop(i)} credits does {name} have? Put anything that isn't a number if you want to leave it as 0: ")))
                #name is the new students' name. This gets the new students' credits list from the dictionary. i is the loop count, going from 0 to 2. Perfect for the credits list length. last value is the users' input for how much credits the student has.
                #this step repeats 3 times for achieved credits, merit credits, and excellence credits. Since validation returns 0, putting an invalid input will default the credits to 0.

    elif task == 3: #Edits the credits of a student
        selected = input("Which student do you want to add credits?").capitalize() #asking name of student
        if selected in students: #checks if the student exists or not
            print(f"Current credits of {selected}: ") #prints the student name, followed by their credits. It also seperates the list to make it easier to read, although it takes up more lines.
            for i in students[selected]['credits']:
                print(f"{grade_loop(students[selected]['credits'].index(i))} credits: {i}")
            category = 0
            while category == 0:
                category = validation(input("Which grade do you want to add credits? \n1. Achieved | 2. Merit | 3. Excellence")) #asks whether achieved, merit or excellence credits are to be added.
            add_student_credits(students[selected]['credits'], category - 1, validation(input("How many credits do you want to add?")))
            #gets the selected students' credits list, followed by the selected grade that is getting edited, and then the amount of credits to be added. if an invalid input is added, then it defaults to 0.
        else:print("That student does not exist.")
        
    elif task == 4:interface = False #ends the loop
    else:print("Invalid input") 
