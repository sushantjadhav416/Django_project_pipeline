n = int(input())
info =[]

for i in range(n):
    info.append(input())

data=tuple(info)
mydata=[]

for i in data:
    mydata.append(data.count(i))

print(mydata)
