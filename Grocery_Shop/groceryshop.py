groceryData=[{"categoryname":"vegetables","itemName":"onions","quantity":60.0, "units":"kg", "price":30.0},
             {"categoryname":"vegetables","itemName":"potato","quantity":10.0, "units":"kg", "price":40.0},
             {"categoryname":"fruits","itemName":"grapes","quantity":10.0, "units":"kg", "price":100.0},
             {"categoryname":"fruits","itemName":"papaya","quantity":10.0, "units":"pcs", "price":60.0}]
class myexception(Exception):
    pass
def addItems():
    try:
        itemsdict={"categoryname":"","itemName":"","quantity":0.0, "units":"", "price":0.0}
        ctgy=input("Enter category name: ")
        item=input("Enter the item to add: ")
        for itemDetails in groceryData:
            if itemDetails.get("itemName")==item:
                raise myexception("The {} is/are already there. If you want to update the quantity enter 3!".format(item))
        amount=(input("Enter the Quantity of {} with units: ".format(item))).split(" ")
        if float(amount[0])<0:
            print("Please enter correct quantity!")
            addItems()
            return
        cost=float(input(f"Enter price per {amount[1]}: "))
        itemsdict["itemName"]=item
        itemsdict["categoryname"]=ctgy
        itemsdict["quantity"]=float(amount[0])
        itemsdict["price"]=cost
        itemsdict["units"]=amount[1]
        groceryData.append(itemsdict)
        print("{} added successfully!".format(item))
    except myexception as e:
        print(e)
    


def viewItems():
    try:
        if len(groceryData)==0:
            raise myexception("Items not yet added!")
        categories=set(item["categoryname"] for item in groceryData)
        # print("Items :" + " "*5+"quantity")
        for c in categories:
            print(f"{c}")
            for itemDetails in groceryData:
                if itemDetails["categoryname"]==c:
                    print("{} :     {} {} :    {}rs/{}".format(itemDetails["itemName"],itemDetails["quantity"],itemDetails["units"],itemDetails["price"],itemDetails["units"]))
            print()
    except myexception as e:
        print(e)
def updateItems():
    try:
        # ctgy=input("Enter category name: ")
        item=input("Enter the item name to update: ")
        for itemDetails in groceryData:
            if item==itemDetails.get("itemName"):
                print("1. add quantity")
                print("2. remove Quantity")
                print("3. change price")
                x=int(input("Enter your option: "))
                if x==1 or x==2:
                    amount=(input("Enter the Quantity: ")).split(" ")
                    if float(amount[0])<0:
                        raise myexception("Please enter correct quantity!")
                elif x==3:
                    p=float(input("Enter new price: "))
                    if p<=0:
                        raise myexception("Please enter positive numbers!!!")
                if x==1:
                    itemDetails["quantity"]+=float(amount[0])
                elif x==2 and itemDetails["quantity"]-float(amount[0])<=0:
                    groceryData.remove(itemDetails)
                    print("{} deleted from records".format(item))
                    return
                elif x==2:
                    itemDetails["quantity"]-=float(amount[0])
                elif x==3:
                    itemDetails["price"]=p
                print("{} updated successfully".format(item))
                return
        raise myexception("{} is/are not added yet. If you want to add enter option 1!".format(item))
    except myexception as e:
        print(e)

def deleteItems():
    item=input("Enter the item name to delete: ")
    for itemDetails in groceryData:
        if item==itemDetails.get("itemName"):
            groceryData.remove(itemDetails)
            print("{} is/are deleted from the records!".format(item))
            return
    print("{} is/are not added yet. If you want to add enter option 1!".format(item))
    return

def groceryShop():
    print("welcome to Grocery shop")
    while True:
        try:
            print("1. Add items")
            print("2. View items")
            print("3. Update items")
            print("4. Delete items")
            print("5. Exit")
            ch=int(input("Enter your option: "))
            match ch:
                case 1: addItems()
                case 2: viewItems()
                case 3: updateItems()
                case 4: deleteItems()
                case 5: break
        except ValueError:
            print("Enter valid option")
#groceryShop()
