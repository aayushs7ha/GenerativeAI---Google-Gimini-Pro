import sqlite3
# Assuming 'db' is the path to your SQLite database file
db = "employee.db"

# Create a connection to the SQLite database
connection = sqlite3.connect(db)
# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table EMPLOYEE(NAME VARCHAR(25),DEPT VARCHAR(25),
ROLE VARCHAR(25),SALARY DOUBLE);

"""
cursor.execute(table_info)

## Insert Some more records
cursor.execute('''Insert Into EMPLOYEE values('Aayush','Analytics','Data Scientist',77)''')
cursor.execute('''Insert Into EMPLOYEE values('Purbi','Marketing','Branding',33)''')
cursor.execute('''Insert Into EMPLOYEE values('Ronaldo','Football','UCL',07)''')
cursor.execute('''Insert Into EMPLOYEE values('Kohli','Cricket','Sports',18)''')
cursor.execute('''Insert Into EMPLOYEE values('Sanjay','Bank','Manager',09)''')
cursor.execute('''Insert Into EMPLOYEE values('Anju','Home','Head of table',13)''')
cursor.execute('''Insert Into EMPLOYEE values('Dhoni','Cricket','Captain',07)''')
cursor.execute('''Insert Into EMPLOYEE values('Bruce','MMA','Legend',20)''')
cursor.execute('''Insert Into EMPLOYEE values('Avinash','Finance','VP',06)''')
cursor.execute('''Insert Into EMPLOYEE values('Neelu','Finance','VP',13)''')
cursor.execute('''Insert Into EMPLOYEE values('Flash','Fun','Foodie',19)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from EMPLOYEE''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()