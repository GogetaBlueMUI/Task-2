year=input("Enter yea to check if its leap year or not: ")
year=int(year)
if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            print("It is a leap year.")
        else:
            print("It is not a leap year")
    else:
            print("It is a leap year")
else:
            print("It is not a leap year")