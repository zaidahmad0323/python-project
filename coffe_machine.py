def completeShop():
    global userBalace
    # here is the list of tools required to make coffee
    reqTools= {
        # Available amount of tools 
        "Coffee beans":1000,#grams
        "Sugar" : 10000,#grams
        "Water" : 10000, #ml
        "Milk" : 10000, #ml
    }

    #available types of coffees
    types = ["latte","cappuccino","macchiato"]

    #price of each coffe per cup
    prices = {
        "latte":300, 
        "cappuccino":200, 
        "macchiato":150,
    }

    def latte(coffeeBeans,sugar,water,milk):    
        global userBalace
        cups = int(input("How many cups would you want to order ?"))        
        if userBalace <cups * prices["latte"] :
            print("Your balance is to low to take this order")     
        if reqTools["Coffee beans"] >= cups * 12 and reqTools["Sugar"] >= cups * 100  and reqTools["Water"]>=cups * 350 and reqTools["Milk"] >= cups * 250 and userBalace >= cups * prices["latte"]:
            reqTools["Coffee beans"] -= cups * 12 
            reqTools["Coffee beans"] -= cups * 12 
            reqTools["Sugar"] -= cups * 100
            reqTools["Water"] -= cups * 350 
            reqTools["Milk"] -= cups * 250 
            userBalace -= prices["latte"] * cups
        else:
                print(f"Sorry cannot prepare {cups} cups for you 😌")

    def cappuccino(coffeeBeans,sugar,water,milk):    
        global userBalace
        cups = int(input("How many cups would you want to order ?"))  
        if userBalace <cups * prices["cappuccino"] :
            print("Your balance is to low to take this order")     
        elif reqTools["Coffee beans"] >= cups * 12 and reqTools["Sugar"] >= cups * 100 and reqTools["Water"]>= cups * 250 and reqTools["Milk"] >= cups * 250 :
            reqTools["Coffee beans"] -= cups * 12 
            reqTools["Sugar"] -=  cups * 100  
            reqTools["Water"] -= cups * 250 
            reqTools["Milk"] -= cups * 250
            userBalace -= cups * prices["cappuccino"]
        else:
            print(f"Sorry cannot prepare {cups} cups for you 😌")    

    def macchiato(coffeeBeans,sugar,water,milk):    
        global userBalace
        cups = int(input("How many cups would you want to order ?"))
        if userBalace <cups * prices["macchiato"] :
            print("Your balance is to low to take this order")             
        if reqTools["Coffee beans"] >= cups * 12 and reqTools["Sugar"] >= cups * 100 and reqTools["Water"]>= cups * 250 and reqTools["Milk"] >= cups * 250 and userBalace >=cups * prices["macchiato"]:
            reqTools["Coffee beans"] -= cups * 12 
            reqTools["Sugar"] -= cups * 100  
            reqTools["Water"] -= cups * 250 
            reqTools["Milk"] -= cups * 250 
            userBalace -= cups * prices["macchiato"]
        else:
            print(f"Sorry cannot prepare {cups} cups for you 😌")    
    def orderCoffe():         
        print("Enter 1,2 or 3")           
        coffeType = input("Whic coffe would you want to take (1:latte/2:cappuccino/3:macchiato) ? ").lower()
        if coffeType == "1" : 
            latte(reqTools["Coffee beans"],reqTools["Sugar"],reqTools["Water"],reqTools["Milk"])            
        elif coffeType == "2":
            cappuccino(reqTools["Coffee beans"],reqTools["Sugar"],reqTools["Water"],reqTools["Milk"])   
        elif coffeType == "3":
            macchiato(reqTools["Coffee beans"],reqTools["Sugar"],reqTools["Water"],reqTools["Milk"])   
        else:
            print("Wrong entry please select an available coffee from the given")   
            orderCoffe()
    orderCoffe()  
    print(reqTools)
    print(f"Your current balance is {userBalace}")      
    more = input("Would you want anything more (yes/no)? ").lower()
    if more == "yes":
        completeShop()  
userBalace = int(input("Enter your account balance : "))        
completeShop()          
        
        