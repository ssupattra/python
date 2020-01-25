import mysql.connector

con = mysql.connector.connect(
user = "", #need to input later
password = "",#need to input later
host = "",#need to input later
database = ""#need to input later
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