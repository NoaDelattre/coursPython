#LANGLACE v2
# La variable est écrite sans espace en camelCase
# Elle commence par une lettre minuscule et chaque mot suivant commence par une majuscule

maValeur = input("Veuillez saisir votre nom : ")

# Une variable peut contenir un nombre entier 
jeSuisUneVariable1 = 1
print("La valeur est : " + str(jeSuisUneVariable1))

# Une variable peut contenir une chaîne de caractères
jeSuisUneVariable2 = "Coucou"

# Une variable peut contenir un booléen 
jeSuisUneVariable3 = True 

# Une variable peut contenir un flottant
jeSuisUneVariable4 = 3.14

# Une variable peut contenir un tableau, une liste
jeSuisUneVariable5 = [1,2,3,4,5] 
jeSuisUneVariable6 = ["Eleve1","Eleve2","Eleve3","Eleve4","Eleve5"]
jeSuisUneVariable7 = ["Eleve1", 12, 1.2, True, "Eleve5", ["Eleve6", 12, 1.2, True, "Eleve10"]]

# Une variable peut contenir un objet
jeSuisUneVariable8 = {"Nom":"Dupont","Prenom":"Jean","Age":33}

age = 33


TOTO = 1 

# Constante écrite en majuscules
PI = 3.14

jeSuisUneAutreVariable = 3 


# Les opérateurs arithmétiques sont : +, -, *, /, %, **, //
uneVariable1 = 10
uneVariable2 = 3
total = uneVariable1 + uneVariable2
print("Le total est : " + str(total))

# résultat de 13//2
print("Le résultat de 13//2 est :" + str(13//2))
# résultat de 13/2
print("Le résultat de 13/2 est :" + str(13/2))

# comparer 2 variables
# les test sont : ==, !=, <, >, <=, >=
# /!\ on met == pour tester une égalité 

if uneVariable1 == uneVariable2:
    # si vrai
    print("Les deux variables sont égales.")
else:
    # si faux
    print("Les deux variables sont différentes.")

a = 2
b = 3
if a == b:
    # si vrai
    print("Les deux variables sont égales.")
else:
    # si faux
    print("Les deux variables sont différentes.")