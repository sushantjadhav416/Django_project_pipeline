n  = int(input())
p = n
with open("mul_table.txt","w") as f:
   f.write(f"The table of {n}:")
   for j in range(1,11):
            f.write(f"\n {n} X {j} : {p*j}\n")
            


