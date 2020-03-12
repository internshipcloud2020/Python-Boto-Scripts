import mysql.connector
from mysql.connector import errorcode
config = {
  'host':'satyaserver.mysql.database.azure.com',
  'user':'Pavan@satyaserver',
  'password':'######',
  'database':'testsample1'
}
#print(config["database"])
try:
   conn = mysql.connector.connect(**config)
   print("Connected Successfully")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Invalid Credentials")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  cursor = conn.cursor()
  tableName=input("Enter Table Name: ")
  cursor.execute("DROP TABLE IF EXISTS "+tableName+";")
  print("Finished dropping table (if existed).")
  cursor.execute("CREATE TABLE "+tableName+" (candidate_id serial PRIMARY KEY, name VARCHAR(50), courses_completed INTEGER);")
  print("Finished creating table.")
  cursor.execute("SELECT * FROM "+tableName+";")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")
  print(rows)
  print("Enter 1.Insert , 2.Update , 3.Delete")
  n=int(input())
  if(n==1):
      cursor.execute("INSERT INTO "+tableName+" (candidate_id,name, courses_completed) VALUES (%s, %s, %s);", (int(input("Enter Candidate IdL ")),input("Enter Your Name: "), int(input("Enter No of Courses Completed: "))))
      print("Inserted",cursor.rowcount,"rows of data.")
      cursor.execute("SELECT * FROM "+tableName+";")
      rows = cursor.fetchall()
      print("Read",cursor.rowcount,"row(s) of data.")
      print(rows)  
  elif n==2:
      cursor.execute("UPDATE "+tableName+" SET courses_completed = %s WHERE name = %s;", (int(input("Enter No of Courses Completed: ")), input("Enter Your Name: ")))
      print("Updated",cursor.rowcount,"row(s) of data.")
      print("Updated Rows are ",rows)
      cursor.execute("SELECT * FROM "+tableName+";")
      rows = cursor.fetchall()
      print("Read",cursor.rowcount,"row(s) of data.")
      print(rows)
  elif n==3:
     cursor.execute("DELETE FROM "+tableName+" WHERE name=%(param1)s;", {'param1':input("Enter Your Name: ")})
     print("Deleted",cursor.rowcount,"row(s) of data.")
     cursor.execute("SELECT * FROM "+tableName+";")
     rows = cursor.fetchall()
     print("Read",cursor.rowcount,"row(s) of data.")
     print(rows)
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")