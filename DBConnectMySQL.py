import pymysql.cursors  
 
# Function return a connection.
def getConnection():
     
    # You can change the connection arguments.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password=''          
                                db='pythondb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection