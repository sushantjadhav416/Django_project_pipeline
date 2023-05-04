def greatestnum(a,b,c):
    if(a>b and a>c):
        print(f'{a} is greater!!!!!')
    elif(b>a and b>c):
        print(f"{b} is greater!!!!!")
    else:
        print(f"{c} is greater!!!!!")

n1=int(input("Enter the number1:"))
n2=int(input("Enter the number2:"))
n3=int(input("Enter the number3:"))
greatestnum(n1,n2,n3)