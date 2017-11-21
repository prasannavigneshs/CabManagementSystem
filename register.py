from validate_email import validate_email
import sqlite3

def reg():
    name=input("Enter your Name: ")

    mobno=input("Enter your mobile number: ")
    if len(mobno)<10:
        while True:
            mobno=input("Enter a valid Mobile number: ")
            if len(mobno)>=10:
                break
    mobno=int(mobno)

    email=input("Enter your email address: ")
    if not validate_email(email):
        while True:
            email=input("Enter a valid email address: ")
            if validate_email(email):
                break

    db=sqlite3.connect("cabmanagement")
    cursor=db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, phone INTEGER, email TEXT)")
    if cursor.execute("INSERT INTO users(name, phone, email) VALUES('%s', '%d', '%s')" % (name,mobno,email)):
        print("Registration Successful")
        db.commit()
    db.close()
    return name
