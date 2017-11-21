import sqlite3
from validate_email import validate_email

db = sqlite3.connect("cabmanagement")
cursor = db.cursor()


def validate_admin(email,username):
    cursor.execute("SELECT * FROM users WHERE name='%s' and email='%s'" %(username,email))
    res=cursor.fetchall()
    if len(res)==0:
        return False
    else:
        return True

def start_admin_activity():
    print()
    print("1.List users")
    print("2.List drivers")
    print("3.Add driver")
    print("4.Remove Driver")
    print("5.Logout")
    ch=input("Enter choice: ")
    return int(ch)

def list_user():
    print()
    cursor.execute("SELECT * FROM users")
    res=cursor.fetchall()
    print("Name".ljust(30,' ')+"PhoneNo".ljust(12,' ')+"Email".ljust(40,' '))
    print("".ljust(82,'-'))
    for i in res:
        if i[0]!='admin':
            print(i[0].ljust(30, ' ') + str(i[1]).ljust(12, ' ') + i[2].ljust(40, ' '))
def list_drivers():
    print()
    cursor.execute("SELECT * FROM drivers")
    res = cursor.fetchall()
    print("Name".ljust(20, ' ') + "PhoneNo".ljust(12, ' ') + "Email".ljust(30, ' ')+"Cab Number".ljust(20,' ')+"Cab Type".ljust(10,' ')+"Rating".ljust(8,' ')+"Status".ljust(9,' '))
    print("".ljust(109,'-'))
    for i in res:
        if i[0] != 'admin':
            print(i[0].ljust(20, ' ') + str(i[1]).ljust(12, ' ') + i[2].ljust(30, ' ') + i[3].ljust(20,' ')+i[4].ljust(10,' ')+str(round((i[5]/i[6]*5),2)).ljust(8,' ') +i[7].ljust(9,' ') )
def add_drivers():
    cursor.execute("CREATE TABLE IF NOT EXISTS drivers (name TEXT, phone INTEGER, email TEXT, cabno TEXT, cabtype TEXT, rating INTEGER, total_rating INTEGER, status TEXT)")

    name = input("Enter driver Name: ")
    mobno = input("Enter driver mobile number: ")
    if len(mobno) < 10:
        while True:
            mobno = input("Enter a valid Mobile number: ")
            if len(mobno) >= 10:
                break
    mobno = int(mobno)

    email = input("Enter driver email address: ")
    if not validate_email(email):
        while True:
            email = input("Enter a valid email address: ")
            if validate_email(email):
                break

    cabno=input("Enter the cab number: ")
    cabtype=input("Enter cabtype: ")
    if cursor.execute("INSERT INTO drivers(name, phone, email, cabno, cabtype, rating, total_rating, status) VALUES('%s', '%d', '%s', '%s', '%s', '%d' ,'%d', '%s')" % (name, mobno, email,cabno,cabtype, 4, 5, "yes")):
        print("Registration Successful")
        db.commit()

def del_driver():
    print()
    name=input("Enter the driver name to be removed")
    cursor.execute("SELECT * FROM drivers WHERE name='%s'"%(name))
    res=cursor.fetchall()
    if len(res)==0:
        print("Driver not found!!")
        return
    else:
        if cursor.execute("DELETE FROM drivers WHERE name='%s' "%(name)):
            print("Driver removed successfully")
            db.commit()
            return

