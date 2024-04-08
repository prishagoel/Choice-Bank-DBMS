import mysql.connector
import os

password = os.environ.get("MYSQL_PASSWORD")

f = mysql.connector.connect(host = "localhost", user = "root", passwd = password)
mycur = f.cursor()
mycur.execute("create database BankManager;")
print("Database Created")
f.commit()
f.close()
mycur.close()

f = mysql.connector.connect(host = "localhost", user = "root", passwd = password, database = "BankManager")
mycur = f.cursor()
mycur.execute("use BankManager;")
mycur.execute("create table Bank(ID varchar(15) NOT NULL primary key, Bname varchar(20), Location varchar(30));")
print("Bank table created")
f.commit()

mycur.execute("create table Branch(BID varchar(15) NOT NULL primary key, BranchName varchar(20), Blocation varchar(30));")
print("Branch table created")
f.commit()

mycur.execute("create table Customer(CID varchar(15) NOT NULL primary key, Cname varchar(20), Address varchar(30), Email varchar(25));")
print("Customer table created")
f.commit()

mycur.execute("create table Mobiles(CID varchar(15), MobileNumber varchar(15), foreign key(CID) references Customer(CID));")
print("Mobiles table created")
f.commit()

mycur.execute("create table Account(ANO varchar(20) NOT NULL primary key, Type varchar(30), Balance integer, CID varchar(15), BID varchar(15), foreign key(CID) references Customer(CID), foreign key(BID) references Branch(BID));")
print("Account table created")
f.commit()

mycur.execute("create table Employee(EID varchar(15) NOT NULL primary key, DateofJoin date, DateofLeave date, Ename varchar(20), Phone varchar(15), Eaddress varchar(30), Salary integer, BID varchar(15), foreign key(BID) references Branch(BID));")
print("Employee table created")
f.commit()

#Type: Remove/Insert(REM/INS)
mycur.execute("create table Transactions(TID varchar(15) NOT NULL primary key, Amount integer, ANO varchar(15), foreign key(ANO) references Account(ANO), Type varchar(10) check (Type IN ('REM', 'INS')));")
print("Transactions table created")
f.commit()

mycur.execute("create table Loan(LID varchar(15) NOT NULL primary key, Type varchar(20), Amount integer, CID varchar(15), foreign key(CID) references Customer(CID));")
print("Loan table created")
f.commit()

mycur.execute("create table PaymentPeriod(LID varchar(15), Period varchar(20), foreign key(LID) references Loan(LID));")
print("PaymentPeriod table created")
f.commit()


mycur.execute("INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('1', 'John Doe', '123 Main St', 'john@example.com')")
mycur.execute("INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('2', 'Jane Smith', '456 Elm St', 'jane@example.com')")
mycur.execute("INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('3', 'Alice Johnson', '789 Oak St', 'alice@example.com')")
mycur.execute("INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('4', 'Bob Williams', '101 Pine St', 'bob@example.com')")
mycur.execute("INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('5', 'Eve Davis', '202 Cedar St', 'eve@example.com')")
f.commit()

mycur.execute("INSERT INTO Mobiles (CID, MobileNumber) VALUES ('1', '123-456-7890')")
mycur.execute("INSERT INTO Mobiles (CID, MobileNumber) VALUES ('1', '987-654-3210')")
mycur.execute("INSERT INTO Mobiles (CID, MobileNumber) VALUES ('2', '555-123-4567')")
mycur.execute("INSERT INTO Mobiles (CID, MobileNumber) VALUES ('3', '777-888-9999')")
mycur.execute("INSERT INTO Mobiles (CID, MobileNumber) VALUES ('4', '333-444-5555')")
mycur.execute("INSERT INTO Mobiles (CID, MobileNumber) VALUES ('4', '777-777-7777')")
mycur.execute("INSERT INTO Mobiles (CID, MobileNumber) VALUES ('5', '888-888-8888')")
mycur.execute("INSERT INTO Mobiles (CID, MobileNumber) VALUES ('5', '999-999-9999')")
f.commit()

mycur.execute("INSERT INTO Bank (ID, Bname, Location) VALUES ('1', 'Choice Bank', 'Crystal Valley')")
f.commit()

mycur.execute("INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('101', 'Downtown Branch', 'City Center')")
mycur.execute("INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('102', 'Suburb Branch', 'Green Valley')")
mycur.execute("INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('103', 'Westside Branch', 'Sunny Hills')")
mycur.execute("INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('104', 'East End Branch', 'Riverfront')")
mycur.execute("INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('105', 'Northside Branch', 'Mountain View')")
f.commit()

mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A101', 'Savings', 1000, '1', '101')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A102', 'Checking', 500, '2', '102')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A103', 'Savings', 2500, '3', '103')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A104', 'Checking', 800, '4', '104')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A105', 'Savings', 3500, '5', '105')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A106', 'Checking', 1200, '1', '101')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A107', 'Savings', 2200, '2', '102')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A108', 'Checking', 1600, '3', '103')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A109', 'Savings', 4200, '4', '104')")
mycur.execute("INSERT INTO Account (ANO, Type, Balance, CID, BID) VALUES ('A110', 'Checking', 1800, '5', '105')")
f.commit()

mycur.execute("INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E101', '2022-01-15', NULL, 'John Smith', '123-456-7890', '123 Main St', 50000, '101')")
mycur.execute("INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E102', '2021-03-20', NULL, 'Jane Doe', '987-654-3210', '456 Elm St', 60000, '102')")
mycur.execute("INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E103', '2022-05-10', NULL, 'Alice Johnson', '555-123-4567', '789 Oak St', 55000, '103')")
mycur.execute("INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E104', '2020-12-05', NULL, 'Bob Williams', '777-888-9999', '101 Pine St', 70000, '104')")
mycur.execute("INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E105', '2023-02-18', NULL, 'Eve Davis', '333-444-5555', '202 Cedar St', 52000, '105')")
f.commit()

mycur.execute("INSERT INTO Transactions (TID, Amount, ANO, Type) VALUES ('T101', 500, 'A101', 'REM')")
mycur.execute("INSERT INTO Transactions (TID, Amount, ANO, Type) VALUES ('T102', 1000, 'A102', 'INS')")
mycur.execute("INSERT INTO Transactions (TID, Amount, ANO, Type) VALUES ('T103', 750, 'A103', 'REM')")
mycur.execute("INSERT INTO Transactions (TID, Amount, ANO, Type) VALUES ('T104', 300, 'A104', 'INS')")
mycur.execute("INSERT INTO Transactions (TID, Amount, ANO, Type) VALUES ('T105', 1200, 'A105', 'REM')")
f.commit()

mycur.execute("INSERT INTO Loan (LID, Type, Amount, CID) VALUES ('L101', 'Personal Loan', 10000, '1')")
mycur.execute("INSERT INTO Loan (LID, Type, Amount, CID) VALUES ('L102', 'Home Loan', 50000, '2')")
mycur.execute("INSERT INTO Loan (LID, Type, Amount, CID) VALUES ('L103', 'Auto Loan', 20000, '3')")
f.commit()

mycur.execute("INSERT INTO PaymentPeriod (LID, Period) VALUES ('L101', 'Monthly')")
mycur.execute("INSERT INTO PaymentPeriod (LID, Period) VALUES ('L102', 'Quarterly')")
mycur.execute("INSERT INTO PaymentPeriod (LID, Period) VALUES ('L103', 'Monthly')")
f.commit()
print("Values Inserted")

f.close()
mycur.close() 