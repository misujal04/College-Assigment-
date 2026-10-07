n=input("Enter the numbers: ").split()
for i in range(0,len(n)):
    if int(n[i])%2==0:
        print(n[i],"The number is Even")
    else:
        print(n[i],"The number is Odd")