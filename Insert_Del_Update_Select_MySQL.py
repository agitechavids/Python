import pymysql.cursors  
 
# Function return a connection.
def getMySQLConnection():
     
    # You can change the connection arguments.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='',                             
                                 db='pythondb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection



'''
# INSERT EXAMPLE

import pymysql.cursors 
 
connection = getMySQLConnection()
print ("Connection successful!")

roll = eval(input("Enter Roll No   "))
name = input("Enter Name   ")
addr = input("Enter Address   ")
mobno = input("Enter Mobile No   ")

try :
    cursor = connection.cursor()
     
    sql =  "insert into student(roll, name, address, mobno) values (%s, %s, %s, %s) "
     
    # Execute sql, and pass 4 parameters.
    cursor.execute(sql, (roll, name, addr, mobno))
     
    connection.commit() 
except:
	print("INSERT PROBLEM...SQL ERROR....")
finally: 
    connection.close()
'''


'''
# UPDATE EXAMPLE

import pymysql.cursors 
 
connection = getMySQLConnection()
print ("Connection successful!")

roll = eval(input("Enter Roll No   "))
addr = input("Enter New Address   ")
mobno = input("Enter New Mobile No   ")

try :
    cursor = connection.cursor()
     
    sql = "Update student set address = %s, mobno = %s where roll = %s " 
     
    # Execute sql, and pass 3 parameters.
    rowCount = cursor.execute(sql, (addr, mobno, roll ) )
     
    connection.commit() 
     
    print ("Updated! ", rowCount, " rows")
 
finally:
    # Close connection.
    connection.close()
'''


'''
# Delete Example

connection = getMySQLConnection()
print ("Connect successful!")

roll = eval(input("Enter Roll No For Delete   "))
 
try :
    cursor = connection.cursor()
     
    sql = "delete from student where roll = %s" 
     
    # Execute sql, and pass 1 parameters.
    rowCount = cursor.execute(sql, ( roll ) )
     
    connection.commit() 
     
    print ("Deleted! ", rowCount, " rows")
 
finally:
    # Close connection.
    connection.close()
'''



# SELECT EXAMPLE

connection = getMySQLConnection()
print ("Connect successful!")

roll = eval(input("Enter Roll No    "))

try :
	cursor = connection.cursor()
	
	sql = "Select roll, name, address, mobno from student where roll = %s "
	
	# Execute sql, and pass 1 parameter.
	cursor.execute(sql, ( roll ) )
	
	print ("cursor.description: ", cursor.description)
	
	print()
	
	for row in cursor:
		print (" ----------- ")
		print("Row: ", row)
		print ("Roll: ", row["roll"])
		print ("Name: ", row["name"])
		print ("Address: ", row["address"] , type(row["address"]) )
		print ("Mobile No: ", row["mobno"])
finally:
	# Close connection.
	connection.close()


