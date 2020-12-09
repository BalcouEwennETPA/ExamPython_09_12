import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = ["balcon" , "ballon" , "boules" , "suiver" , "viseur" , "abruti", "calque", "stereo" , "textes" , "argent"]
mot=random.choice(listeMot)
print(mot) #choisir un mot random parmis la listeMot

propMot = input ("faites une propositions de mot (six lettres max)")

if (propMot [0] == mot [0]) :
    print (Back.RED + propMot[0],end="")
elif(propMot [0] == mot[0]or propMot [0] == mot[1]or propMot [0] == mot[2]or propMot [0] == mot[3]or propMot [0] == mot[4]) or propMot[0] == mot[5]:
    print (Back.YELLOW + propMot[0],end="")
else:
    print (Back.BLUE + propMot[0],end="")

if (propMot [1] == mot [1]) :
    print (Back.RED + propMot[1],end="")
elif(propMot [1] == mot[0]or propMot [1] == mot[1]or propMot [1] == mot[1]or propMot [1] == mot[3]or propMot [1] == mot[4]) or propMot[1] == mot[5]:
    print (Back.YELLOW + propMot[1],end="")
else:
    print (Back.BLUE + propMot[0],end="")

if (propMot [2] == mot [2]) :
    print (Back.RED + propMot[2],end="")
elif(propMot [2] == mot[0]or propMot [2] == mot[1]or propMot [2] == mot[1]or propMot [2] == mot[3]or propMot [2] == mot[4]) or propMot[2] == mot[5]:
    print (Back.YELLOW + propMot[2],end="")
else:
    print (Back.BLUE + propMot[2],end="")

if (propMot [3] == mot [3]) :
    print (Back.RED + propMot[3],end="")
elif(propMot [3] == mot[0]or propMot [3] == mot[1]or propMot [3] == mot[1]or propMot [3] == mot[3]or propMot [3] == mot[4]) or propMot[3] == mot[5]:
    print (Back.YELLOW + propMot[3],end="")
else:
    print (Back.BLUE + propMot[3],end="")

if (propMot [4] == mot [4]) :
    print (Back.RED + propMot[4],end="")
elif( propMot [4] == mot[1]or propMot [4] == mot[1]or propMot [4] == mot[3]or propMot [4] == mot[4]) or propMot[4] == mot[5]:
    print (Back.YELLOW + propMot[4],end="")
else:
    print (Back.BLUE + propMot[4],end="")

if (propMot [5] == mot [5]) :
    print (Back.RED + propMot[5],end="")
elif(propMot [5] == mot[0]or propMot [5] == mot[1]or propMot [5] == mot[3]or propMot [5] == mot[4]) or propMot[5] == mot[5]:
    print (Back.YELLOW + propMot[5],end="")
else:
    print (Back.BLUE + propMot[5],end="")
# les deux dernieres lettres apparaissent toujours en jaune sans meme que je sache pourquoi    

input()
