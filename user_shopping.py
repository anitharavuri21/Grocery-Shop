from grocery import groceryData
from grocery import viewItems
from grocery import myexception
cart=[]
def viewandadd():
    viewItems()
    viewItemsuser()

def viewItemsuser():
    try:
        while True:
                ch=input("Do you want anything to add to your cart(Y/N): ").strip()
                if ch=='N' or ch=='n':
                    break
                elif ch=='Y' or ch=='y':
                    itemn=input("Enter the item name: ").strip()
                    flag=0
                    for i in groceryData:
                        if i.get("itemName")==itemn:
                            itemQ=input("Enter the quantity of item that you want to buy with units: ").split(" ")
                            if len(itemQ)<=1:
                                print("Please Enter quantity with units!!!")
                                viewItemsuser()
                                return
                            dic={"itemname":"","quantity":"","units":"","price":0.0}
                            if i.get("quantity")>=float(itemQ[0]) and float(itemQ[0])>=0:
                                for x in cart:
                                    if x.get("itemname")==itemn:
                                        x["quantity"]+=float(itemQ[0])
                                        x["price"]+=float(itemQ[0])*i["price"]
                                        flag=1
                                if flag==0:
                                    dic["itemname"]=itemn
                                    dic["quantity"]=float(itemQ[0])
                                    dic["price"]=float(itemQ[0])*i["price"]
                                    dic["units"]=itemQ[1]
                                    cart.append(dic)
                                    flag=1
                            elif i.get("quantity")<float(itemQ[0]):
                                print("No sufficient Quantity! please select from available quantity ")
                                viewItemsuser()
                                return
                            elif float(itemQ[0])<0:
                                print("Please enter valid quantity!!")
                                viewItemsuser()
                                return
                    if flag==0:
                        print("No such item! Please select from available!!")
                else:
                     raise myexception("Enter valid option!")        
    except myexception as e:
        print(e)
def updateCart():  
    while True:
        try:
            viewCartd()
            print("1. Remove items")
            print("2. Update quantity")
            print("3. close")
            ch=int(input("Enter your option: ").strip())
            flag=0
            match ch:
                case 1: 
                    n=input("Enter item name: ").strip()
                    for x in cart:
                        if x.get("itemname")==n:
                            cart.remove(x)
                            flag=1
                            print("your cart has been updated!!")
                            # viewCart()
                    if flag==0:
                        print(f"Your cart has no item called {n}")
                case 2:
                    n=input("Enter item name: ").strip()
                    for i in cart:
                        if i.get("itemname")==n:
                            # q=float(input("Enter Quantity: "))
                            print("1. add quantity")
                            print("2. remove quantity")
                            x=int(input("Enter your option: ").strip())
                            q=float(input("Enter Quantity: ").strip())
                            flag=0
                            if x==1:
                                i["quantity"]+=q
                                flag=1
                            elif x==2:
                                i["quantity"]-=q
                                flag=1
                            else:
                                raise myexception("Enter valid option!!")
                    if flag==0:
                            myexception("No such item in the cart!!")
                case 3:
                    break
        except myexception as e:
            print(e)
        except ValueError:
            print("Enter valid option!!")
def viewCartd():
    totalprice=0
    if len(cart)==0:
            print("Your cart is empty!! keep shopping")
            viewandadd()
            return
    print("________Your Cart________")
    for i in cart:
            print(f"{i["itemname"]}      {i["quantity"]}{i["units"]}      {i["price"]}rs")
            totalprice+=i["price"]
    print(f"Total Price: {totalprice}")

def viewCart():
    
        viewCartd()
        # updateCart()
        while True:
            x=int(input("Enter 0 to return!! "))
            if x==0:
                return

    
def buy():
    viewCartd()
    try:
        if len(cart)==0:
            return
        ch=input("do you want to continue to buy? (Y/N): ").strip()
        if ch=='Y' or ch=='y':
            for i in cart:
                for g in groceryData:
                    if i.get("itemname")==g.get("itemName"):
                        g["quantity"]-=i["quantity"]
                    # cart.remove(i)
            cart.clear()
            print("------your order confirmed--------")
            print("Thanks for shopping!!")
        elif ch=='N' or ch=='n':
            return
    except ValueError:
        print("Enter valid option!!")
    
def usershopping(un):
    print(f"Welcome {un}")
    while True:
        try:
            print("1. View/add Items")
            print("2. view cart")
            print("3. update cart")
            print("4. Buy")
            print("5. exit")
            ch=int(input("Enter your choice: "))
            match ch:
                case 1: viewandadd()
                case 2: viewCart()
                case 3: updateCart()
                case 4: buy()
                case 5:break
        except ValueError:
            print("Enter valid option!!")
#usershopping('anitha')
