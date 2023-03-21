import mysql.connector
import pandas as pd
connection = mysql.connector.connect(host = 'localhost', #mysql的位置 看mysql裡connection的伺服器上會有寫
                                    port = '3306', #連接的通道 看mysql裡connection的伺服器上會有寫
                                    user = 'root', #連接的使用者名稱
                                    password = 'zJ19900817'
                                    database = 'sql_tutorial') #使用者密碼

#開始使用
cursor = connection.cursor() 

#創建資料庫 #括號裡的就是sql指令
#cursor.execute("CREATE DATABASE qq;") 

# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall() #要多打這個才回回傳結果出來
# for r in records:
#     print(r)

cursor.execute("USE `sql_tutorial`;")
cursor.execute("SELECT * FROM `employee`;")
a = cursor.fetchall()
data = pd.DataFrame(a)
print(data)

#我們可以在python改動mysql的資料，但在最後就需要打
connection.commit()

#關掉
cursor.close()
connection.close()