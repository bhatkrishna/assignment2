# 2. Write an if statement to determine whether a variable holding a year is
# a leap year.
a=int (input("enter input:"))
if a%4==0 and a%100 !=0:
    print(a," is leap year")
elif a%100==0:
    print(a,'is not leap year')
elif a%4==0:
    print(a,"is leap year")
else:
    print("given year is not leap year")