import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = ["balcon" , "ballon" , "boules" , "suiver" , "viseur" , "abruti", "calque", "stereo" , "textes" , "argent"]
mot=random.choice(listeMot)
#print(random.choice(listeMot)) #choisir un mot random parmis la listeMot
propMot = input ("faites une propositions de mots (six lettres max)")

for i in range (len(mot)) :
        if propMot == mot :
            print (Fore.RED + mot)
        elif propMot [0] != mot [0]:
            print (Fore.BLUE + mot)
        elif propMot [1] != mot [1]:
            print (Fore.BLUE + mot)
        elif propMot [2] != mot [2]:
            print (Fore.BLUE + mot)
        elif propMot [3] != mot [3]:
            print (Fore.BLUE + mot)
        elif propMot [4] != mot [4]:
            print (Fore.BLUE + mot)
        elif propMot [5] != mot [5]:
            print (Fore.BLUE + mot)
input ()
