N1 = int(input())
N2 = int(input())

class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        return self.num + num2.num
    
    def __sub__(self,num2):
        return self.num - num2.num
    def __mul__(self,num2):
        return self.num * num2.num

n1 = Number(N1)
n2 = Number(N2)


add = n1+n2
print(add)



    
        