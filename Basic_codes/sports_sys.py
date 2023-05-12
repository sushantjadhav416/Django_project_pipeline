class Sport:
    def __init__(self):
            pass
    def CalculateAvgage(ages):
          pass
    def retierdPlayer(id):
          pass
    
class Cricket(Sport):
    playerid=[]
    
    def  __init__(self):
       self.playerid.append(1)
       print("The new cricket team is formed:")
    def CalculateAvgage(ages):
          sum=0
          for i in ages:
               sum+=ages[i]
          avg = sum/len(ages)
          print(f"The average age of the team is: {avg}")
    
    def retierdPlayer(self,id):
        if(self.playerid[id-1]!=-1):
              self.playerid[id-1]=-1
              print(f"The palyer with id {id} is retierd!!!")
        else:
              print("The palyer is retired already !!!!!")

class Football(Sport):
     




        
          
