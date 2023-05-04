def volley(n,Str):
    level=volley=0
    for i in Str:
        if i == 'U':
            level+=1
        elif i == 'D':
             if level == 1:
                 volley+=1
             level-=1
    return volley

steps=int(input())
Str = input()
print()


