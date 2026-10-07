n=input("Enter the numbers").split()

max1=0
min1=0
max=n[0]
min=n[0]
for i in range(0,len(n)):
    if n[i]>max:
        max1=max
        max=n[i]
    if n[i]<min:
        min1=min
        min=n[i]
    
print("The Maxmium number is ",max)
print("The Second maxmium number is ",max1)
print("The Min number is ",min)
print("The Second min is ",min1)