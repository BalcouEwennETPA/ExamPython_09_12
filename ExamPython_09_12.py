import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = ["balcon" , "ballon" , "boules" , "suiver" , "viseur" , "abruti", "calque", "stereo" , "textes" , "argent"]

print(random.choice(listeMot)) #choisir un mot random parmis la listeMot
propMot = input ("faites une propositions de mots (six lettres max)")
mot=random.choice(listeMot)
for i in range (len(mot)) :
        if propMot == mot :
            print (Fore.RED + propMot)
            print ("vous avez gagné")
        elif propMot [0] != mot [0]:
            print (Fore.BLUE + propMot)
            print("essaye encore")
        elif propMot [1] != mot [1]:
            print (Fore.BLUE + propMot)
            print("essaye encore")
        elif propMot [2] != mot [2]:
            print (Fore.BLUE + propMot)
            print("essaye encore")
        elif propMot [3] != mot [3]:
            print (Fore.BLUE + propMot)
            print("essaye encore")
        elif propMot [4] != mot [4]:
            print (Fore.BLUE + propMot)
            print("essaye encore")
        elif propMot [5] != mot [5]:
            print (Fore.BLUE + propMot)
            print("essaye encore")
            
input ()
