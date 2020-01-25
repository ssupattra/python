import mysql.connector

con = mysql.connector.connect(
user = "", #need to inpurt later
password = "",#need to inpurt later
host = "",#need to inpurt later
database = ""#need to inpurt later
)

cursor = con.cursor()

word=input("Enter a word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")