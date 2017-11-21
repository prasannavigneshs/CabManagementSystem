import sqlite3
from time import gmtime,strftime,sleep
from calculatefare import calculate_fare
db=sqlite3.connect("cabmanagement")
cursor=db.cursor()

def start_user_activities():
    print()
    print("1.List earlier rides")
    print("2.Book a ride")
    print("3.Logout")
    ch=input("Enter your choice: ")
    return int(ch)

def list_rides(name):
    print()
    cursor.execute("SELECT * FROM rides WHERE username='%s'" %(name))
    res=cursor.fetchall()
    if len(res)==0:
        print("No rides found!!")
    else:
        print()
        print("Date".ljust(12,' ')+"From".ljust(10,' ')+"To".ljust(12,' ')+'Driver Name'.ljust(15,' ')+"Cab Type".ljust(10,' ')+"Phone number".ljust(15,' ')+'Ride Fare'.ljust(10,' '))
        print("".ljust(84,'-'))
        for i in res:
            print(i[1].ljust(12,' ') + i[2].ljust(10, ' ') + i[3].ljust(12, ' ') + i[4].ljust(15, ' ') + i[5].ljust(10,' ')+str(i[6]).ljust(15, ' ')+str(i[7]).ljust(10,' '))

def book_cab(name):
    print()
    cursor.execute("CREATE TABLE IF NOT EXISTS rides (username TEXT, date TEXT, frm TEXT, t0 TEXT, drivername TEXT,cabtype TEXT, phone INTEGER,ridefare INTEGER)")

    frm=input("Enter pickup location: ")
    to=input("Enter drop location: ")

    cabtype=input("1.Sedan\n2.Mini\n3.SUV\nEnter cabtype: ")
    if cabtype=='1':
        cabtype='sedan'
    elif cabtype=='2':
        cabtype='mini'
    elif cabtype=='3':
        cabtype='suv'
    date=strftime("%d-%m-%Y",gmtime())
    cursor.execute("SELECT * FROM drivers WHERE cabtype='%s'"%(cabtype))
    res=cursor.fetchall()


    drivername=""
    phonenumber=0

    for i in res:
        if i[7]=='yes':
            drivername=i[0]
            phonenumber=i[1]
            cursor.execute("UPDATE drivers SET status='no' WHERE name='%s' " %(drivername))
            db.commit()
            break
    else:
        print("No Rides Available Right now!!")
        return

    fare=calculate_fare(frm,to,cabtype)

    print("FROM: "+frm+"\tTo: "+to)
    print("Driver name: "+drivername)
    print("Driver Number: ",phonenumber)
    print("Cab Type: "+cabtype)
    print("Total Fare: ",fare)

    cursor.execute("INSERT INTO rides VALUES('%s', '%s', '%s' , '%s' ,'%s' , '%s', '%d', '%d')" %(name, date,frm,to,drivername,cabtype,phonenumber,fare))
    db.commit()

    sleep(3)

    rating=input("Enter rating for the driver (1-5) : ")
    rating=int(rating)
    print()
    cursor.execute("UPDATE drivers SET rating=rating+%d ,total_rating=total_rating+5 WHERE name='%s' "%(rating,drivername))
    db.commit()

def logout():
    cursor.execute("UPDATE drivers SET status='yes' WHERE status='no'")
    db.commit()
    print("Succesfully logged out\n")
    return

