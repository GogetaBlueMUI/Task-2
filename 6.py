num=input("Enter a number to find its factorial: ")
num=int(num)
fac=1
for i in range (1, num+1):
    fac*=i
print("Factorial: ", fac)