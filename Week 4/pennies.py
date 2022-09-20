Input = int(input("Please enter the amount of pennies you have: "))
Penny = 1
Nickel = 5
Dime = 10
Quarter = 25
Dollar = 100

check1 = int(Input % Dollar)
check2 = int(check1 % Quarter)
check3 = int(check2 % Dime)
check4 = int(check3 % Nickel)
check5 = int(check4 % Penny)

bar1 = int((Input - check1)/Dollar)
bar2 = int((check1 - check2)/Quarter)
bar3 = int((check2 - check3)/Dime)
bar4 = int((check3 - check4)/Nickel)
bar5 = int((check4 - check5)/Penny)

if bar1 > 0 :
    print("Dollars:",bar1)
if bar2 > 0:
    print("Quarters:",bar2)
if bar3 > 0:
    print("Dimes:",bar3)
if bar4 > 0:
    print("Nickels:",bar4)
if bar5 > 0:
    print("Pennies",bar5)