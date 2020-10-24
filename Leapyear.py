year=int(input("Enter a year : "))
if(year%400==0 or (year%100!=0 and year%4==0)):
    print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")
