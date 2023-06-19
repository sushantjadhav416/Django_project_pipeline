class Building:
    floors=[]

class School(Building):
    def __init__(self,n):
        floors=[]
        for i in range(1,n):
            floors.append(0)
        print("A schoole is being constructed!!")

    def Floors_completed(self,fnum):
        if(fnum <= self.n):
            self.floors[fnum-1]=1
            print(f"Construction for floor number {fnum} completed in school.")
        else:
            print(f"Floor number {fnum} does not exist in school.")
    
    def PrintStatus(self,):
        if(self.fnum>self.floors.length):
            print(f"Floor number {self.fnum}does not exist in school"); 
        elif(self.floors[self.fnum-1]==1): 
           print(f"Construction for floor number {self.fnum} completed in school"); 
        elif(self.floors[self.fnum-1]==0): 
           print(f"Construction for floor number {self.fnum} not completed in school"); 
 
    def printFloors(self):
        print(f"Total {len(self.floors)} in this building")



if __name__=="__main__":
    b1 = School(11)
    b1.printFloors()

 
        