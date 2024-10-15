import grocery
import usergrocery
user=[{"username":"Anitha", "password":"123*"}]
admin=[{"adminname":"Anitha","password":"*123"}]
def login():
    un=input("Enter User name: ")
    for u in user:
        if u.get("username")==un:
            pw=input("Enter password: ")
            if u.get("password")==pw:
                print("login successful")
                usergrocery.usershopping(un)
                return 
            else:
                print("incorrect password")
                return
    print("user doesn't exist!")
    x=input("Do you want to signup(Y/N): ")
    if x=='Y':
        signup()
        return
    elif x=='N':
        return
def Alogin(an):
    for a in admin:
        if a.get("adminname")==an:
            apw=input("Enter password: ")
            if a.get("password")==apw:
                print("login Successful")
                grocery.groceryShop()
                return
            else:
                print("incorrect password!")
                Alogin(an)
                return
    print("admin name doesn't exist!")
    return
def signup():
    udict={"username":"","password":""}
    udict["username"]=input("Enter user name: ")
    for u in user:
        if u["username"]==udict["username"]:
            print("user already exist! please login")
            x=input("do you want to login(Y/N): ")
            if x=='Y':
                login()
                return
            else:
                return
    udict["password"]=input("Enter password: ")
    user.append(udict)
    print("signup successful")
    usergrocery.usershopping(udict["username"])

def loginpage():
    print("Welcome to grocery shop")
    while True:
        ch=input("Are you an admin or user(A/U/E): ")
        if ch=='U':
                print("1. sign up")
                print("2. login")
                print("3. close")
                ch1=int(input("Enter your option: "))
                match ch1:
                    case 1:
                        signup()
                    case 2:
                        login()
                    case 3: break
        elif ch=='A':
            an=input("Enter admin name: ")
            Alogin(an)
        else:
            return
loginpage()
