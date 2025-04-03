import pymysql

# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='Akhil', database='subscribers_db')
cursor = conn.cursor()

# Test if subscribers table exists
cursor.execute("SHOW TABLES LIKE 'subscribers'")
result = cursor.fetchone()
assert result, "ERROR: subscribers table does not exist!"

print("All tests passed successfully!")

conn.close()
