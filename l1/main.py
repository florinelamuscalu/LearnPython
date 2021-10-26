# afisarea
print("Hello World")

# afisare forma
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# afisare varabile
limbaj_programare = "python"
adjectiv = "importante"
print("acesta este un text si il voi afisa in consola")
print("sunt la inceput si invat" + limbaj_programare)
limbaj_programare = "java"
print("trebuie sa invat sa lucrez in " + limbaj_programare)
print("el este unul dintre cele mai " + adjectiv +" limbaje")

# afisare stringuri
fraza = "Buna siua"
print(fraza + " lume ")
#lower lit --> lit mici
print(fraza.lower())
#upper lit -> lit mari
print(fraza.upper())
#isupper ret true/false in functie de cum sunt lit
print(fraza.isupper())
print(fraza.upper().isupper())
#len cate caractere sunt
print(len(fraza))
#afisare primul caracter din string
print(fraza[0])
#index functiun unde este un anumit caracter
print(fraza.index("u"))
print(fraza.index("ua"))
#replace pune o valoare unde vreau
print(fraza.replace("Buna", "Cur"))
#afisare linie noua, ghilimele,"/"
print("Buna\nsiua")
print("Buna\"siua")
print("Buna\siua")

#afisare numere
print(-2.0975)
print(3+4.5)
print(2-1)
print(3*3)
print(25/5)
print((3+7)*2)
print(10 % 3)

my_num = 5
print(my_num)
#convert number to string
print(str(my_num) + " my favorite number")
#absolute valule of number = modulul
my_num = -12
print(abs(my_num))
# ridicarea la putere
print(pow(3 , 2))
# maximul
print(max(4,6))
#minimul
print(min(4,6))
#rotunjirea
print(round(3.2))
# librarie pentru chestii de matematica
from math import *
#rotunjire jos
print(floor(2.9888 ))
#rotunjire sus
print(ceil(2.112))
#radical
print(sqrt(25))

#citirea de la tastatura
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

# calcule cu nr citite de la tastatura
num1 = input("Enter a number:")
num2 = input("Enter another number:")
# convert stings in numar
# result = int(num1) + int(num2)
result = float(num1) + float(num2)
print(result)








