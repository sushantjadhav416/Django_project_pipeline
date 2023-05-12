class Account:
    def __init__(self,Name,num,bal):
        self.Name = Name
        self.num = num
        self.bal=bal

    @staticmethod 
    def deposite(self,amt):
        self.bal = self.bal-amt
        return f"The amount {amt} is deposited form your account: {self.bal}"
    

if __name__=="__main__":
 act = Account("Sushant",2213324,200000)
 print(act.deposite(200))