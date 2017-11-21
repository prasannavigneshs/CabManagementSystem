import sqlite3

def log():

    db=sqlite3.connect("cabmanagement")

    cursor=db.cursor()
    try:
        mobno=int(input("Enter your mobile no: "))
    except:
        print("Enter only numbers\n")
        return "Invalid"
    email=input("Enter your email: ")

    cursor.execute("SELECT * FROM users where phone='%d' and email='%s'" % (mobno,email))

    res=cursor.fetchall()
    if len(res)==0:
        f="Invalid"
    else:
        for i in res:
            f=i[0]

    db.close()

    return f

