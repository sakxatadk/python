import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password="@sakshyat.11",
    database = "student"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE IF NOT EXISTS student")

# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

# mycursor.execute("CREATE TABLE IF NOT EXISTS std (name VARCHAR(50), rollno INT PRIMARY KEY ,marks INT NOT NULL)")
# mycursor.execute("SHOW TABLES")
# for i in mycursor:
#     print(i)

# sql = "INSERT INTO std (name,rollno,marks) VALUES (%s,%s,%s)"
# val = [
#     ("Ankit",12,95),
#     ("Rohan",13,89),
#     ("Aman",14,92),
#     ("Rahul",15,85)
#     ]

# mycursor.executemany(sql,val)

# mydb.commit()

# mycursor.execute("SELECT * FROM std WHERE name LIKE '%an%'")
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

# sql = "UPDATE std SET marks = 92 WHERE name = 'Ankit'"
# mycursor.execute(sql)
# mydb.commit()

# mycursor.execute("SELECT * FROM std LIMIT 4 OFFSET 2")
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

# mycursor.execute("SELECT * FROM std ORDER BY marks DESC")
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

sql = "DELETE FROM std WHERE rollno = 15"
mycursor.execute(sql)
mydb.commit()