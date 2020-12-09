import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = ["balcon" , "ballon" , "boules" , "suiver" , "viseur" , "abruti", "calque", "stereo" , "textes" , "argent"]
mot=random.choice(listeMot)
#print(mot) #choisir un mot random parmis la listeMot

propMot = input ("faites une propositions de mot (six lettres max)")

if propMot [0] == mot [0] :
    print (Back.RED + propMot)
    print(Style.RESET_ALL)
    print ("vous avez gagné")
    print(Style.RESET_ALL)
elif propMot [0] != mot [0]:
    print (Back.BLUE + propMot)
    print(Style.RESET_ALL)
    print("essaye encore")
    print(Style.RESET_ALL)


            
input ()
