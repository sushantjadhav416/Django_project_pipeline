class Sport:
    def __init__(self):
          pass
    def CalculateAvgage(self,ages):
          pass
    def retierdPlayer(self,id):
          pass
class Cricket(Sport):
    playerid=[]
    def  __init__(self):
       for i in range(11):
         self.playerid.append(i)
       print("The new cricket team is formed:")

    def CalculateAvgage(self,ages):
          sum=0
          for i in range(len(ages)):
               sum+=ages[i]
          avg = sum/len(ages)
          print(f"The average age of the Cricket team is: {avg}")
    
    def retierdPlayer(self,id):
        if(self.playerid[id-1]!=-1):
              self.playerid[id-1]=-1
              print(f"The palyer with id {id} is retierd from cricket team!!!")
        else:
              print("The palyer is retired already !!!!!")
class Football(Sport):
    playerid=[]
    def  __init__(self):
       for i in range(11):
          self.playerid.append(i)
       print("The new cricket team is formed:")

    def CalculateAvgage(self,ages):
          sum=0
          for i in ages:
               sum+=ages[i]
          avg = sum/len(ages)
          print(f"The average age of the football team is: {avg}")
    
    def retierdPlayer(self,id):
        if(self.playerid[id-1]!=-1):
              self.playerid[id-1]=-1
              print(f"The palyer with id {id} is retierd form football team!!!")
        else:
              print("The palyer is retired already !!!!!")

if __name__=="__main__":
     c1 = Cricket()
     f1 = Football()
     ages = [23,34,43,21,23,32,32,23,43,12,21]
     id  = int(input("Enter the id:"))
     c1.CalculateAvgage(ages)
     f1.retierdPlayer(id)







     








        
          
