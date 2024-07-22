num1=input("Enter first number: ")
num1=float(num1)
num2=input("Enter second number: ")
num2=float(num2)
print("Sum= ", num1+num2)
print("Difference= ", num1-num2)
print("Product= ", num1*num2)
if num2==0:
    print("Error! Division cant be done.")
else:
    print("Division= ", num1/num2)