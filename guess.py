import random
import sys
x = random.randint(0,500)
essai = 4
num = input("Entrer un nombre entre 0 et 500:  ")
if num.isdigit:
    while essai >0 :
        if int(num) == x :
            print (" Vous avez trouvez le bon nombre ")
            break
        else:
            if int(num) > x :
                print ("nombre trop grand")
            else:
                print ("nombre trop petit")
            print (" IL t reste " , essai  ,"essaies")
            num = input ("  Reesayer ")
            essai = essai - 1
    


else:
     print (" ce n'est pas un nombre ")

