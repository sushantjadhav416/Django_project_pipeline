class complex:
    def __init__(self,real,img):
         self.real=real
         self.img=img

    def __add__(self,c):
         return complex(self.real+c.real,self.img+c.img)
    
    def __str__(self):
         return f"{self.real}i+{self.img}j"
         
if __name__=="__main__":
     num1=complex(7,8)
     num2=complex(9,7)
     print(num1+num2)
     
