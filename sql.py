import mysql.connector as a
co = a.connect(host = "localhost", user = "root", passwd = "Jatin129e")
c = co.cursor()
sql1 = "create database Booking"
c.execute(sql1)
sql2 = "use Booking"
c.execute(sql2)
sql3 = "create table checkin (Days int(20), Name varchar(20), ID varchar(20), ID_Number int(20))"
c.execute(sql3)
sql4 = "create table checkout (Days int(20), Name varchar(20), Price float(20))"
c.execute(sql4)
co.commit()