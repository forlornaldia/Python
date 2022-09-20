Input = int(input("Please enter da cash man: "))
Penny = 1
Nickel = Penny * 5
Dime = Penny * 10
Quarter = Penny * 25
Dollar = Penny * 100

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

print("Dollars:",bar1)
print("Quarters:",bar2)
print("Dimes:",bar3)
print("Nickels:",bar4)
print("Pennies",bar5)