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

elif propMot [0] != mot [0]:
    print (Back.BLUE + propMot)
    print(Style.RESET_ALL)
    print("essaye encore")


#   if (propMot [0] == mot [0]) :
#       print (Back.RED + propMot[0],end="")
#    elif(propMot [0] == mot[1]or propMot [0] == mot[2]or propMot [0] == mot[3]or propMot [0] == mot[4]or propMot [0] == mot[5]):
#        print (Back.GREEN + propMot[0],end="")
#    else:
#        print (Back.BLUE + propMot[0],end(""))
#
#    if (propMot [1] == mot [1]) :
#        print (Back.RED + propMot[1],end="")
#    elif(propMot [1] == mot[1]or propMot [1] == mot[2]or propMot [1] == mot[3]or propMot [1] == mot[4]or propMot [1] == mot[5]):
#        print (Back.GREEN + propMot[1],end="")
#    else:
#        print (Back.BLUE + propMot[1],end(""))
# j'ai essayé cela mais je n'ai pas reussi a le faire fonctionner sur online gdb



            
input () 


            
input ()
