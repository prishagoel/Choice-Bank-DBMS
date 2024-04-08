import mysql.connector
import os

password = os.environ.get("MYSQL_PASSWORD")

f = mysql.connector.connect(host = "localhost", user = "root", passwd = password, database = "BankManager")
mycur = f.cursor()
mycur.execute("use BankManager;")
f.commit()
'''mycur.execute("drop table Bank;")
mycur.execute("drop table PaymentPeriod;")
mycur.execute("drop table Loan;")
mycur.execute("drop table Transactions;")
mycur.execute("drop table Employee;")
mycur.execute("drop table Account;")
mycur.execute("drop table Mobiles;")
mycur.execute("drop table Customer;")
mycur.execute("drop table Branch;")'''
mycur.execute("drop database BankManager;")
f.commit()
print("EVERYTHING IS DELETED")
