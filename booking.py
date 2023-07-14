import mysql.connector as a 
con = a.connect(host= 'localhost',user='root',passwd='Jatin129e', database="booking")

def checkin():
    d = input("Days : ")
    n = input("Name : ")
    i = input("ID : ")
    no = int(input("Id Number : "))
    data = (d,n,i,no)
    c = con.cursor()
    sqlQ = "Insert into checkin values(%s,%s,%s,%s)"
    c.execute(sqlQ,data)
    con.commit()
    print("Data entry was successful. ")
    main()
    
def checkout():
    d = int(input("Days : "))
    n = input("Name : ")
    p = d*1000
    data = (d,n,p)
    c = con.cursor()
    sqlQ = "Insert into checkout values(%s,%s,%s)"
    c.execute(sqlQ,data)
    con.commit()
    print("Data entry was successful. ")
    main()
    
def main():
    print(" 1. Check In")
    print(" 2. Check Out")
    ch = int(input("Enter your choice :"))
    if(ch ==1):
        checkin()
    elif(ch == 2):
        checkout()
    else:
        print("Select correct option")
        main()
main()