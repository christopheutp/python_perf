# # try except le plus basique
# try:
#     age = int(input("Saisir votre Age : "))
# except: # correspond à "except Exception:" car toutes les exceptions héritent du type Exception
#     print("Saisie invalide !")


# try except avec vérification du type d'exception et else
# try:
#     age = int(input("Saisir votre Age : "))
# except ValueError: # ici on vérifie le type de l'exception
#     print("Saisie invalide !")
# except Exception: # on peut avoir autant de'except que l'on veut pour tester d'autre types d'Exceptions
#     print("Une autre exception a été levée")
# else:
#     print("Saisie valide !")

# try except avec stockage de l'exception
# try:
#     age = int(input("Saisir votre Age : "))
# except Exception as ex: #ici, on stocke l'exception levée dans une variable ex
#     print(ex) #lorsque l'on affiche ex, on aura le message correspondant à l'exception
#     print("Saisie invalide !")
# else:
#     print("Saisie valide !")

# try except avec stockage de l'exception et finally
try:
    age = int(input("Saisir votre Age : "))
except:
    print("Saisie invalide !")
else:
    print("Saisie valide !")
finally:
    print("après le try, avec ou sans exeception levées")