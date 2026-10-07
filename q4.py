n=input("Enter the number").split()
num=input("which number u have to check")
flag=0
for i in range(0,len(n)):
    if n[i]==num:
        print("This number is present on ",i,"Index")
        flag=1
if flag==0:
    print("This Number is not present ")
    
        