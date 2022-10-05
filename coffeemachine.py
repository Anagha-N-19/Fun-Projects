from coffemachinedata import MENU
from coffemachinedata import resources
import os

def make_coffee(k,resources):
    if k in MENU:
        for i in resources:
            if resources[i] - MENU[k]["ingredients"][i] >= 0:
                c = MENU[k]["cost"]
            else:
                print("Not enough resources")
                return resources
    print("cost", c)
    change = coin(c)
    if change < 0:
        print("try again")
        return resources
    else:
        if k in MENU:
            for i in resources:
                resources[i] -= MENU[k]["ingredients"][i]
        print("your change is",change)
        return resources
            # print(MENU[k][0][i])
    #for i in resources:
        #print(i, ":", resources[i])


def coin(c):
    print('Insert coins')
    q = int(input('enter no of quarters '))
    d = int(input('enter no of dimes '))
    n = int(input('enter no of nickels '))
    p = int(input('enter no of pennies '))
    total = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    change = total - c
    if change < 0:
        print("Sorry, that's not enough money. Money refunded")
        return -1
    else:
        return round(change,2)


print("Welcome to coffe making machine")
k = input("What would you like? (espresso/latte/cappuccino): ")
if k == "report":
        for i in resources:
            print(i, ":", resources[i])
else:
        resources = make_coffee(k,resources)
while input("Do you want to continue y/n ") != "n":
    os.system('cls')
    k = input("What would you like? (espresso/latte/cappuccino): ")
    if k == "report":
        for i in resources:
            print(i, ":", resources[i])
    else:
        resources = make_coffee(k,resources)


