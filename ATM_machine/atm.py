data = [{
    "name":"madhav",
    "accNo":"1212",
    "pin":"1234",
    "balance":10000
},{
    "name":"anitha",
    "accNo":"1213",
    "pin":"9876",
    "balance":1000
},{
    "name":"deepika",
    "accNo":"1214",
    "pin":"9999",
    "balance":1000
},{
    "name":"kavya",
    "accNo":"1215",
    "pin":"9988",
    "balance":1000
},{
    "name":"durga prasad",
    "accNo":"1216",
    "pin":"8877",
    "balance":1000
}]
 
atmBalance = {
    "hundreds":10,
    "tHundreds":10,
    "fHundreds":10,
    "tThousands":10,
    "Tbalance":28000
} 
def withdraw(data,user):
    amount = int(input("Enter amount:"))
    if user["balance"] <= amount or amount<=0:
        print(user["Incorrect or insufficient funds"])
    else:
        atmBalance["Tbalance"]-=amount
        user["balance"]-=amount
        x=amount//2000
        if amount>=2000 and x<=atmBalance["tThousands"]:
            amount=amount-(2000*x)
            print("The numbers of 2000 notes withdrawn: "+str(x))
            atmBalance["tThousands"]-=(x)
        x=amount//500
        if amount>=500 and x<=atmBalance["fHundreds"]:
            amount=amount-(500*(x))
            print("The numbers of 500 notes withdrawn: "+str(x))
            atmBalance["fHundreds"]-=(x)
        x=amount//200
        if amount>=200 and x<=atmBalance["tHundreds"]:
            amount=amount-(200*(x))
            print("The numbers of 200 notes withdrawn: "+str(x))
            atmBalance["tHundreds"]-=(x)
        x=amount//100
        if amount>=100 and amount//100<=atmBalance["hundreds"]:
            amount=amount-(100*(x))
            print("The numbers of 100 notes withdrawn: "+str(x))
            atmBalance["hundreds"]-=(x)
        callATM()
 
def callATM():
    print("The available new balances in Each Denamination: ")
    print("100: "+str(atmBalance["hundreds"]))
    print("200: "+str(atmBalance["tHundreds"]))
    print("500: "+str(atmBalance["fHundreds"]))
    print("2000: "+str(atmBalance["tThousands"]))
    print("Total Balance in ATM: "+str(atmBalance["Tbalance"]))
 
def deposit(data,user):
   hund=int(input("Enter number of hundred notes"))
   THund=int(input("Enter number of Two Hundred notes"))
   FHund=int(input("Enter number of Five Hundred notes"))
   TThousand=int(input("Enter number of Two Thousands notes"))
   if hund<0 or THund<0 or FHund<0 or TThousand<0:
       print("Incorrect deposit amount")
       return
   if hund==0 and THund==0 and FHund==0 and TThousand==0:
       print("Deposit amount cannot be Zero")
       return
   atmBalance["hundreds"]+=hund
   atmBalance["tHundreds"]+=THund
   atmBalance["fHundreds"]+=FHund
   atmBalance["tThousands"]+=TThousand
   atmBalance["Tbalance"]+=(100*hund+200*THund+500*FHund+2000*TThousand)
   user["balance"]+=(100*hund+200*THund+500*FHund+2000*TThousand)
   callATM()
 
def checkBalance(data,user):
    print("The available balance of your account: "+str(user["balance"]))
 
def atm(data):
    print("ATM Service")
    acNO =(input("Enter account Number: "))
    try:
        user = next(user for user in data if user["accNo"]==acNO)
    except StopIteration:
        print('no data found')
        return
    if user:
        pi = (input("Enter PIN:"))
        if pi == user["pin"]:
            while True:
                print("1.Withdraw")
                print("2.Deposit")
                print("3.Balance Enquiry")
                print("4.Exit")
                op = int(input("Enter your option:"))
                match op:
                    case 1:
                        withdraw(data,user)
                    case 2:
                        deposit(data,user)
                    case 3:
                        checkBalance(data,user)
                    case 4:
                        break
        else:
            print("Incorrect Pin")
    else:
        print("Account number doesn't exist")
 
atm(data)
