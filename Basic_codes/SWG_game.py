import random
print("!!!!!! Welcome to The Snack-Water-Gun game !!!!!!!")
def game(a,b):
   if b!='s' and b!='w' and b!='g':
        print("invalid input!!")
   elif a=='s' and b'w':  
        return False
   elif a=='s' and b=='g':
        return True
   elif a=='w' and b=='s':
        return True
   elif a=='w' and b=='g':
        return False
   elif a=='g' and b=='w':
        return True
   elif a=='g' and b=='s':
        return False
   elif a==b:
        return None

if __name__=="__main__":
     
 Rnum = random.randint(1,3)

 if(Rnum==1):
      com='s'
 elif(Rnum==2):
      com='w'
 elif(Rnum==3):
      com ='g'

 player = input("Enter your input:")
 result = game(com,player)
 print("Computer entered: ",com)
 print("You entered: ",player)

 if(result==True):
      print("Congratulations you wone !")
 elif(result==False):
      print("You losse !")
 else:
      print("None")


    

     
