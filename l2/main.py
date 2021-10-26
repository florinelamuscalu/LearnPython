# partea a doua
# MAD LIBS GAME

# de aici incepem o sa schimbam cateva cuvine ca sa le putem adauga de la tastatura

#print("Rose are red")
#print("Violets are blue")
#print("I love you")


#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")

#print("Rose are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)


#                            ******************************


#liste

#friends = ["Luiza", "Andreea", "Alina", "Alina", "Ioana", "Maria", "Costinela"]
#print(friends[-1])

# daca vrem elementele de la stanga la dreapta vom incepe cu 0 pana la
# " nr maxim de elemete", dar daca vrem elementele de la de la dreapta
# vom incepe cu -1 pana la "-nr maxim de elemente"

# pentru mai multe elemente ne folosim de primul index pana la urmatorul
# exemplu
#print(friends[1:4])

# daca vrem sa inlocuim un element o sa punem pur si simplu peste el
# exemplu
#friends[1] = "Bonbonica"
#print(friends[1])



#                    *********************************

# functii de liste

#lucky_number = [42, 8, 15, 16, 23, 4]
#print(lucky_number)

# extend function = uneste doua liste
#friends.extend(lucky_number)
#print(friends)

# append adauga la final
#friends.append("Magura")
#print(friends)

# adugare la mijloc
#friends.insert(1, "Rom")
#print(friends)

# stergere
#friends.remove("Magura")
#print(friends)

# sterge tot
#friends.clear()

# pop = sterge ultimul element
#friends.pop()

# verificare pe ce index se afla anumit element
#print(friends.index("Alina"))

# daca nu se afla primim eroare
#print(friends.index("Miruna"))

# nr de cate ori se alfa un element
#print(friends.count("Alina"))

# sortarea unei liste
#lucky_number.sort()
#print(lucky_number)

# intoarece lista
#lucky_number.reverse()
#print(lucky_number)

# creare unei copy
#friends2 = friends.copy()
#print(friends2)


#                      ************************************


# TUPLES
# tuples in python un lef de lista, are unele funtii diferite
# aceste nu pot fi modificate sa se adauge sa sa se stearga

#coordinates = (4, 5)

# nu se pot modifica
# coordinates[1] = 10;
#print(coordinates[1])

# o lista de tuples

#coordinates2 = [(1, 2), (6, 7), (8, 9)]

#               *******************************

# Functii
# colectii de cod

# cream o functie care saluta user-ul

# def este cuvantul cheie pentru functii
# def name_function ():

#def say_hi (name, age):
     #print("Hello " + name + ", you are " + str(age))

# chemarea functie pentru a fi executata
#say_hi("Robert", 5)
#say_hi("Luiza", 8)


#                ***********************

# Return Statement

# returneaza informatii despre functiile python
#def cube(num):
    #return num * num * num


# nu returneaza nimic deoarce noi nu returnam nimic ( fara return)
#print(cube(3))

#result = cube (4)
#print(result)

#nr = input("Ente a number: ")
#resulte = cube(int(nr))
#print(resulte)

#                 ********************************

# if Statement

#is_male =True
#is_tall = True
#s_eyes = "blue"

#if is_male == True:
    #print("You ar a male")
    #if is_tall == True and is_eyes == "brown":
        #print("I will take you home")
    #elif not(is_tall) and is_eyes == "green":
        #print("Stay at home, you are a short male")
    #elif is_tall and is_eyes == "blue" :
        #print("You are nice to a friend")
#else:
    #print("You are a female and beautiful")


#                      *******************************

# if Statement & Comparison

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,2,1))








