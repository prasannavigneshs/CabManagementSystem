from register import reg
from login import log
from admin import validate_admin,start_admin_activity,list_user,add_drivers,list_drivers,del_driver
from useractivites import start_user_activities,list_rides,book_cab,logout

def clear():
    print()

res=""

def main():
    print("WELCOME TO CAB BOOKING SYSTEM".center(100,'*'))
    print("1.Register as a new user")
    print("2.Login to an existing account")
    print("3.Admin Login")
    print("4.Exit the application")
    ch=input("Enter your choice: ")
    if ch=='1':
        res=reg()
        user_activities(res)

    elif ch=='2':
        res=log()
        if res=="Invalid":
            print("Invalid credentials\n")
            while True:
                res=log()
                if res!="Invalid":
                    clear()
                    print("Welcome "+res)
                    user_activities(res)

        else:
            clear()
            print("Welcome "+res)
            user_activities(res)

    elif ch=='3':
        name=input("Enter username: ")
        email=input("Enter email: ")
        if not validate_admin(email,name):
            while True:
                name = input("Enter username: ")
                email = input("Enter email: ")
                if validate_admin(email,name):
                    admin_activities()

        else:
            admin_activities()

    elif ch=='4':
        quit()

    else:
        print("Enter a valid Choice")
        main()

def admin_activities():
    while True:
        ch=start_admin_activity()

        if ch==1:
            list_user()

        elif ch==2:
            list_drivers()

        elif ch==3:
            add_drivers()

        elif ch==4:
            del_driver()

        elif ch==5:
            main()

        else:
            print("Enter valid choice:")

def user_activities(res):
    while True:
        ch=start_user_activities()

        if ch==1:
            list_rides(res)

        elif ch==2:
            book_cab(res)

        elif ch==3:
            logout()
            main()

        else:
            print("Enter valid choice: ")

if __name__ == "__main__":
    main()
