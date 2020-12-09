import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = ["balcon" , "ballon" , "boules" , "suiver" , "viseur" , "abruti", "calque", "stereo" , "textes" , "argent"]
mot=random.choice(listeMot)
#print(random.choice(listeMot)) #choisir un mot random parmis la listeMot
propMot = input ("faites une propositions de mots (six lettres max)")


input()