#! C:\Users\Hp\Appdata\Local\Programs\Python\Python35\python.exe


import cgi
import cgitb
import mysql.connector as conn

cgitb.enable()
def connectDB():
    db = conn.connect(host = 'localhost', user = 'root', password='')
    cursor = db.cursor()
    return db,cursor
def createDB(db,cursor):
    sql = "create database Busesdb"
    cursor.execute(sql)
    db.commit()
def createEntity(db,cursor):
    sql = "use Busesdb"
    cursor.execute(sql)
    sql = """ create table Bus
             (BusID int not null auto_increment, CompanyName varchar(20) not null, primary key(BusID)"""
    cursor.execute(sql)
    db.commit()

#main program
if __name__ == "__main__":
    try:
        db,cursor = connectDB()
        createDB(db,cursor)
        createEntity(db,cursor)
        cursor.close
    except:
        cgi.print_exception()
