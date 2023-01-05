import mysql.connector as sql
connect= sql.Connect(
    host='localhost',
    user='root',
    password='q1w2e3r4t5y6u7@',
    database='medical_store_record')
if connect.is_connected:
    print("successfully connected")
cursor=connect.cursor()
cursor.execute ('drop table account_details')
cursor.execute ('Create table account_details('
                'User_Name varchar(30) primary key,'
                'password varchar(30) unique)')
cursor.execute ('drop table customers_details')
cursor.execute ('Create table customers_details('
                'account_number int primary key,'
                'patient_name varchar(30),'
                'age int,address varchar(50),'
                'phone_number bigint(11),balance_amount float)')
cursor.execute ('drop table medicines_details')
cursor.execute('create table medicines_details('
               'medicine_name varchar(30),'
               'medicine_code int,'
               'gst float,sgst float,'
               'total_cost float)')
cursor.execute ('drop table Patient_bill')
cursor.execute('create table Patient_bill('
               'medicine_name varchar(30),'
               'medicine_code int ,cgst float,'
               'sgst float,cost_per_item float,'
               'quantity int,'
               'discount_on_balance_amount float,'
               'total_amount float)')
print('table created')
import sys
import mysql.connector as sql
connect= sql.Connect(
    host='localhost',
    user='root',
    password='q1w2e3r4t5y6u7@',
    database='medical_store_record')
cursor=connect.cursor()
from time import gmtime, strftime
a=strftime("%a ,%d %b %y %H:%M:%S",gmtime())
if connect.is_connected:
    print(" YOUR WELLWISHER MEDICAL STORE ")
    print(a)
    print("1. Login")
    print("2. Exit")
    print()
    option=int(input("Enter your choice : "))
    if option==1:
        print()
        user=input('User Name(Enter in Upper Case) : ')
        user=user.upper()
        cursor.execute("select * from account_details where User_Name like '" +user+ "'")
        datas=cursor.fetchall()
        for i in datas:
            value_1=()
            value_2="WELLWISHER"
        if user==value_1:
            password=input('Password : ')
            password=password.upper()
            if password==value_2:
                print()
                print('Login successfull')
                print()
                print("11.Customers Account")
                print("12.Medicine Cost")
                print("3.Bill")
                print()
                option = int(input("enter a option:"))
                if option == 11:
                    account_number = int(input("enter your acct_number:"))
                    patient_name = input("enter your name:")
                    age = int(input("enter your age:"))
                    address = input("enter your address:")
                    phone_number = int(input("enter your number:"))
                    balance_amount = float(input("enter your amount:"))
                    x = "insert into customers_details values(" + str(
                        account_number) + ",'" + patient_name + "'," + str(age) + ",'" + address + "'," + str(
                        phone_number) + "," + str(balance_amount) + ")"
                    print(x)
                    cursor.execute(x)
                    print("Account created congrats")
                    connect.commit()
            import mysql.connector as sql

            conn = sql.connect(host='localhost', user='root', password='manager', database='medical_store')
            cursor = conn.cursor()
            choice = int(input("enter your choice:"))
            if choice == 2:
                cursor.execute("insert into medicines_details values('paracetamal 250mg',325674,1.5,1,5)")
                cursor.execute("insert into medicines_details values('amoxylin',647890,1,1,4)")
                cursor.execute("insert into medicines_details values('zinc sulphide',546783,1.5,0.5,3.5)")
                cursor.execute("insert into medicines_details values('polodb 500mg',568903,3,2.5,10)")
                cursor.execute("insert into medicines_details values('paracetamal 500mg',325679,2,1.5,6)")
                cursor.execute("insert into medicines_details values('vicks action 500',250348,1,0.5,5)")
                cursor.execute("insert into medicines_details values('dolo 500mg',789541,3,2.5,10)")
                cursor.execute("insert into medicines_details values('ferric sulphide',546784,1.5,0.5,3.5)")
                print("Records Created")
                conn.commit()

                if option == 3:
                    print(a)
                    patient_name = input("enter the patient_name :")
                    no = int(input('enter the number of medicine:'))
                    print('customer name:', patient_name)
                    for i in range(no):
                        med_name = input('enter medicine name : ')
                        cursor.execute(
                            "select medicine_code,gst,sgst,total_cost from medicines_details where medicine_name like '" + str(
                                med_name) + "'")
                        data = cursor.fetchall()
                        for row in data:
                            print('medicine_code of', med_name, ':', row[0])
                            print('gst of', med_name, ':', row[1])
                            print('sgst of', med_name, ':', row[2])
                            print('cost_per_item of', med_name, ':', row[3])
                            connect.commit()
                            account_number = input('enter account_number:')
                            cursor.execute("select balance_amount from customers_details where account_number like'" + str(
                                account_number) + "'")
                            datas = cursor.fetchall()
                            datas = list(datas[0])
                            datas = datas[0]
                            print(datas)
                            connect.commit()
                            print("rows affected:", cursor.rowcount)
                            connect.commit()
                            quantity = int(input("enter the quantity:"))
                            total_amount = row[3] * quantity
                            print("total_amount of", med_name, ':', total_amount)
v_sql_insert = "insert into Patient_bill (medicine_name," \
               "medicine_code,cgst," \
               "sgst," \
               "cost_per_item," \
               "quantity,discount_on_balance_amount," \
               "total_amount)values('{}',{},{},{},{},{},{},{})".format(
    med_name, row[0], row[1], row[2], row[3], quantity, datas, total_amount)
print(v_sql_insert)
cursor.execute(v_sql_insert)
if connect.commit():
    print("Records added")
elif():
    print('Invalid Password')
    print('Tryagain')
elif (option==2):
    print("              THANK YOU                  ")
sys.exit()









