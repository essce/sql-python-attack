import mysql.connector

cnx = mysql.connector.connect(user='genomep', password='password',
	host='genome-mysql.cse.ucsc.edu',
	database='hgcentral')

'''
cursor = cnx.cursor()
query = ("SELECT * FROM students")
cursor.execute(getAll)

for (firstname, lastname, age) in cursor:
	print("{}, {} is age {:%d %b %Y}".format(firstname, lastname, age))
'''
cursor = cnx.cursor()     # get the cursor


#cursor.execute("USE hgcentral") # select the database
#cursor.execute("SHOW TABLES")

#tables = cursor.fetchall()       # return data from last query

cursor.execute("SELECT * FROM gbNode LIMIT 10")

for table_name in cursor:
	print(table_name)

cursor.close()
cnx.close()

