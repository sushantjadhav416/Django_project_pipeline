Str = input()

for i in reversed(range(len(Str))):
    print(Str[i],end="")

print("\n")
mystr = list(Str)

mystr.reverse()
s=""
for i in mystr:
    s=s+i

print(s)


