# Crearea unui calculator mai bun

#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter  second number: "))
#op = input("Enter  operator: ")

#if op == "+":
    #print(num1 + num2)
#elif op == "-":
    #print(num1 - num2)
#elif op == "/":
    #print(num1 / num2)
#elif op == "*":
    #print(num1 * num2)
#else:
    #print("Invalid operator: ")

#    ************************

# Dictionar

# convret acronime in nume specifice

#monthConversion ={
#    "Jan": "January",
#    "Feb": "February",
#    "Mar": "March",
#    "Apr": "April",
#    "May": "May",
#    "Jun": "June",
#    "Jul": "July",
#    "Aug": "August",
#    "Sep": "September",
#    "Oct": "Octomber",
#    "Nov": "November",
#    "Dec": "December",
#}
#cheile sunt acronimele, putem folosi orice valoare in loc de string

#print(monthConversion["Nov"])
#print(monthConversion.get("Jun"))
#print(monthConversion.get("Luv", "Not a valid key"))

#                      ************************

# While loop

#i = 1
#while i <=10:
    #print(i)
    #i +=1

#print("Done whit loop")

#             *************************


# Joc de ghicit

# vrem sa cream un joc prin care sa dam user-ului niste hint-uri legate de
# cuvantul secret pe care trebuie sa il ghiceasca

#sectret_word = "giraffe"
#guess = ""
#guess_cont = 0
#guess_limit = 3
#out_of_guesses = False


#while guess != sectret_word and not(out_of_guesses):
#    if guess_cont < guess_limit:
#     guess = input("Enter guss: ")
#     guess_cont += 1
#    else:
#         out_of_guesses = True

#if out_of_guesses:
#     print("Out of Guesses, You lose!")
#else:
#    print("You win!")

#               ***************

# FOR loop

#for letter in "Giraffe Academy":
#    print(letter)

#friends = ["Jim", "Karen", "Kevin"]
#for friend in friends:
#    print(friend)

# range iti afiseaza toate nr pe care le ceri in afara de ultimul
# ex range(3): 0 1 2 -> se va incepe de la 0
#for index in range(3, 10):
    #print(index)

#colors = ["red", "blue", "green"]
# len iti da un nr intre 0 si numarul de elemente din lista
# in cazul nostru 3, deaorece ai 3 culori
# colors[index] = colors[0], colors[1], colors[2]
#for index in range(len(colors)):
#    print(colors[index])
#print(colors)

#for index in range(5):
#    if index == 0:
#        print("First Iteration")
#    else:
#        print("Not firs")

#                    ***************************


# Functia exponentiala

# 2^3
#print(2**3)

#def raise_to_power(base_num, pow_num):
#    result = 1
#    for index in range(pow_num):
#        result = result * base_num
#    return result

#print(raise_to_power(2,3))


#                  ******************


# 2D Lists & Nested Loops

# fiecare element din lista o sa fie o lista

#number_grid = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9],
#    [0]
#]

# accesare fiercare element idividual
# e un fel de matrice

#print(number_grid[0][0])

# nested for loop
# e un for cum sa te plimbi prin 2D list

#for row in number_grid:
#    print(row)
#    for col in row:
#        print(col)


#                    ************************************

# Un traducator

# o sa trasformam fiecare vocala in litera g din fiecare cuvant pe care noi il dam
# vowels = vocal

def transalte(pharese):
    translation = ""
    for letter in pharese:
        if letter.lower() in "aeiou":
            if letter.isupper():
             translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(transalte(input("Enter a pharse: ")))
