def prime(n):
    temp=False
    for i in range(2,n):
        if n%i==0:
            temp=True
        if temp==False:
           return 1
        else:
            return 0

def composite_prime(Lst):
    List=[]
    c_list=[]
    prime_l=[]

    for i in Lst:
        if prime(i)==1:
            prime_l.append(i)
        else:
            c_list.append(i)

    for i in prime_l:
        List.append(i)
    for i in c_list:
        List.append(i)
        
    return List




if __name__=="__main__":
    inp=[]
    n=int(input())
    for i in range(n):
        inp.append(int(input()))

    print(composite_prime(inp))
    
