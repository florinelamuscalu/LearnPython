# Comentarii

'''
dsfdsf
sdsafsa
'''

#                  **********************************************

# Try/except
#try:
    #value = 10/0
#    number = int(input("Enter a number: "))
#    print(number)
#except ZeroDivisionError:
#    print("Diveded by zero")
#except ValueError:
#    print("Invalid input!")


#try:
#    answer = 10/0
#    number = int(input("Enter a number: "))
#    print(number)
#except ZeroDivisionError as err:
#    print(err)
#except ValueError:
#    print("Invalid input!")

#               *****************************


# Citire fisiere

# open = deschide fisierul
# "r" = citeste fisierul
# "a" = adaugi noi informatii
# "r+" = citesti si scri
# "w" = poti sa scri
# close = inchide fisierul

#employee_file = open("employees.txt", "r")

# readable = spune daca se poate citit
#print(employee_file.readable())
# read = afiseaza tot
#print(employee_file.read())
# readline = afiseaza prima linie, daca pui de doua ori iti afiseaza si a
# doua linie
#print(employee_file.readline()[])
# readlines = afiseaza tot sub forma de lista
#print(employee_file.readlines()[1])

# afiseaza fiecare linie
#for employee in employee_file.readlines():
#    print(employee)
#employee_file.close()

#               ****************************************************

# Scriere in fisiere

#employee_file = open ("employees.txt", "w")
#employee_file = open("employee.txt", "w")
#print(employee_file.read())
#employee_file.write("Cristina")
#employee_file.write("\nOana")
#employee_file = open("employees1.txt", "w")
#employee_file.close()

#html = open("index.htm", "w")
#html.write("Ana are mere")
#html.close()


#              ************************************

# Modules and pip

# importam fisiere externe

#import tools

#print(tools.roll_dice(10))

# pentru mai multe informatii cauti pe net: list of python modules

# instalare librarii care nu le gasesc in External Libraries

# daca cauti pe pagina python docx
# pip install pyhton-docx il scri in terminal
# easy_install python-docx

# pentru dezinstalare pip uninstall

#                          **************************************

# OOP

# cream un obiect

#from Student import Student

#student1 = Student("Ana", "CTI", 9.8, True)

#print(student1.gpa)


#                     *******************************************

# Intrebari cu raspunsuri multiple
'''

from Questions import Question

question_prompts =[
    "Ce are Ana?\n(a) Mere\n(b) Prune\n(c) Cartofi\n\n",
    "Ce zi este azi?\n(a) scoala online\n(b) nu vreau la scoala\n(c) murim\n\n",
    "Cati pisoi vrea?\n(a) toti\n(b) niciunul\n(c) pe bebe\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

'''

#                      ***************************

# Class function
'''
from Studentv2 import Student

student1 = Student("Ana", "CTI", 4.2)
student2 = Student("Ioana", "Info", 1.3)

print(student1.on_honor_roll())

'''

#          ******************************************

# Mostenirea Inheritance

#pui in paranteza clasa mostenita

'''
from Roman import Roman
from RomanSF import RomanSF

roman1 = Roman()
roman1.titlu()

roman3 = RomanSF()
roman3.coperta()
'''


