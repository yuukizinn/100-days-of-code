from data import MENU, resources

now_resources = {"water": 0,
                 "milk": 0,
                 "coffee": 0,
                 "cost": 0}
power_flag = True


def get_resources():
    now_resources["water"] = resources["water"]
    now_resources["milk"] = resources["milk"]
    now_resources["coffee"] = resources["coffee"]


def insert_coins():
    print("please insert coins")
    quarter = int(input("quarter\n"))
    dime = int(input("dime\n"))
    nickel = int(input("nickel\n"))
    penny = int(input("penny\n"))
    sum_money = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
    print(f"sum:{sum_money}")
    return sum_money


def calc_cost(choose):
    now_water = now_resources["water"]
    now_milk = now_resources["milk"]
    now_coffee = now_resources["coffee"]
    req_water = MENU[choose]["ingredients"]["water"]
    req_milk = MENU[choose]["ingredients"]["milk"]
    req_coffee = MENU[choose]["ingredients"]["coffee"]
    req_cost = MENU[choose]["cost"]
    if now_water >= req_water and now_milk >= req_milk and now_coffee >= req_coffee:
        sum_money = insert_coins()
        if sum_money > req_cost:
            now_resources["cost"] += req_cost
            now_resources["coffee"] -= req_coffee
            now_resources["water"] -= req_water
            now_resources["milk"] -= req_milk
            print("ok, you got coffee")
        else:
            print("require more money")
    else:
        print("sry, few resources")

get_resources()
while power_flag == True:
    choose = input('please select "espresso", or "latte", or "cappuccino"\n')
    if choose == "off":
        exit()
    elif choose == 'check':
        print(now_resources)
    else:
        calc_cost(choose)
