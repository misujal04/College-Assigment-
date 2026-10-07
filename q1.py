n=input("Enter the numbers").split()
n=list(map(int,n))
total=0
for i in range(0,len(n)):
    total=total + int(n[i])
print(total)
n=list(map(int,n))
print(sum(n))
print(n)