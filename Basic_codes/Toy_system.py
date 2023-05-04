class Toy:
    def __init__(self,Tid,Ttyp,Tprice):
        self.Tid = Tid
        self.Ttyp = Ttyp
        self.Tprice = Tprice 

class store:
    def __init__(self,Tlist,Typlist):
        self.Tlist = Tlist
        self.Typlist = Typlist

    def fun(self):
        for i in self.Tlist:
            if i.Toytyps.lower() in self.Typlist.lower():
                r=self.Typlist[i.Ttyp.lower()]
                dis=i.price*(r/100)
                i.discount=dis



if __name__=="__main__":
    n=int(input())
    toys=[]
    Toytyps=[]
    for i in range(n):
        Tid=int(input())
        Ttyp=int(input())
        Tprice=int(input())
        toys.append(Toy(Tid,Ttyp,Tprice))
    
    for i in range(3):
        ttype=input()
        amount=int(input())
        Toytyps[ttype.lower()]=amount
    
    S=store(toys,Toytyps)
    S.fun()
    S.Tlist.sort(key=lambda x:x.discount,reverse = True)
    for i in S.Tlist:
        dp= i.price - i.discount
        print(i.id,i.price,dp)
    





        

