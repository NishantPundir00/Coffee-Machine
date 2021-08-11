# menu of coffee Machine
menu = {
    "black" : {
        "ingredients" : {
            "water": 50,
            "milk" : 0,
            "coffee" : 18,
        },
        "cost" : 20
    },
    "normal" : {
        "ingredients" : {
            "water": 150,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 30
    },
    "cappuccino" : {
        "ingredients" : {
            "water": 250,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 50
    }
}

# resources of coffee Machine
resources = {
    "water": 800,
    "milk" : 500,
    "coffee" : 100,
    "money" : 0
}

# function to check is resource is sufficient or not
def is_sufficient(ingredients):
    for i in ingredients:
        if(ingredients[i] > resources[i]):
            print(f"{i} is not sufficient")
            return False
    return True

# function to buy coffee and add or remove resources and money
def buy(coffee):
    if(is_sufficient(coffee["ingredients"])):
    
    #Payment time    
        pay = int(input(f'''
    cost of your coffee is {coffee["cost"]}
    Enter money : '''))

    # when enter money is not sufficient
        if(pay < coffee["cost"]):
            while pay<coffee["cost"]:
                more_pay = input(f'''
    Enter "exit" to cancle order
    need {coffee['cost']-pay} more money : ''')
                if(more_pay == 'exit'):
                    print(f'''
    Good Luck for next Time!!!!
    money refund {pay}
    ''')
                    break
                else:
                    pay+=int(more_pay)

    # when enter money is sufficient
        if(pay >= coffee["cost"]):
            #reduce all resources
            resources["coffee"] -= coffee["ingredients"]["coffee"]
            resources["water"] -= coffee["ingredients"]["water"]
            resources["milk"] -= coffee["ingredients"]["milk"]
            #add money in machine
            resources["money"] += coffee["cost"]
            print(f'''
    Enjoy your coffee!!!!
    money refund {pay-coffee['cost']}
    ''')



# main code..................
is_on = True
while is_on:
    choice = input('''
    What would you like?
    1. black coffee          2. normal coffee
    3. cappuccino            4. report
    5. exit
    ''')
    if(choice == "black coffee" or choice == "1"):
        buy(menu["black"])
    
    elif(choice == "normal coffee" or choice == "2"):
        buy(menu["normal"])

    elif(choice == "cappuccino" or choice == "3"):
        buy(menu["cappuccino"])

    elif(choice == "report" or choice == "4"):
        print(f'''
    -------------------------
            REPORT
    -------------------------
      water      :    {resources['water']} ml
      milk       :    {resources['milk']} ml
      coffee     :    {resources['coffee']} mg
      money      :    Rs {resources['money']}
    -------------------------
      ''')

    elif(choice == "exit" or choice == "5"):
        is_on = False

    else:
        print("Invalid choice............")
