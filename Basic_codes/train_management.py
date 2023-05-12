class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def status(self):
        print("**************************************")
        print(f"The Train name : {self.name}") 
        print(f"The Train seats available : {self.seats}"+"\n")

    def BooK_ticket(self):
        if(self.seats > 0):
           print("Your ticket is booked !!!!!")
           self.seats = self.seats - 1
        else:
            print("sorry, All seats are booked !")


t1 = Train("Pune to Banglore",1000,100)
t1.status()
t1.BooK_ticket()
t1.status()



        
