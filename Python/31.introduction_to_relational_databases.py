# SQL = structure query language *****
# Import necessary module
from sqlalchemy import create_engine
# Create engine: engine
engine =  create_engine('sqlite:///Chinook.sqlite')


# Import necessary module
from sqlalchemy import create_engine
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Save the table names to a list: table_names
table_names = engine.table_names()
# Print the table names to the shell
print(table_names)

# 1. Import packages **** 搜尋SQL有幾個步驟
from sqlalchemy import create_engine 

# Create engine: engine 2. create the database engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Open engine connection: con 3. connect to the engine
con = engine.connect()
# Perform query: rs 4. querry the database
rs = con.execute('SELECT * FROM Album') # *號是代表全部row，這邊讀取全部Album的內容
# Save results of the query to DataFrame: df 5. save query result to a DataFrame
df = pd.DataFrame(rs.fetchall()) #fetchall() 將全部rs裡的row都讀取
# Close connection 6. close connection
con.close()
# Print head of DataFrame df
print(df.head())


# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con: # -> con = engine.connect()
    rs = con.execute('SELECT LastNametle FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3)) #讀其中3行row
    df.columns = rs.keys()
# Print the length of the DataFrame df
print(len(df))
# Print the head of the DataFrame df
print(df.head())

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6') #WHERE 後面set條件
    df = pd.DataFrame(rs.fetchall()) #print 出來是沒有變項名的
    df.columns = rs.keys() #把rs的key作為df的column
# Print the head of the DataFrame df
print(df.head())

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate') #透過BirthDate來排序
    df = pd.DataFrame(rs.fetchall())
    # Set the DataFrame's column names
    df.columns = rs.keys()
# Print head of DataFrame
print(df.head())

# 有另外一種方法會更簡單地啟動engine
# Import packages
from sqlalchemy import create_engine
import pandas as pd
# Create engine: engine 
engine = create_engine('sqlite:///Chinook.sqlite')
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine) #(比較簡單)
# Print head of DataFrame
print(df.head())


# Open engine in context manager and store query result in df1 
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album") #(比較複雜)
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()
# Confirm that both methods yield the same result
print(df.equals(df1)) #可以測式兩個結果是否一樣


#有條件式的讀取
# Import packages
from sqlalchemy import create_engine
import pandas as pd
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeID >= 6 ORDER BY BirthDate', engine) #透過BirthDate來排序
# Print head of DataFrame
print(df.head())


#假設有兩個表，他們有共同的地方，我們要找出共同的地方並把兩個表合併在一起方便看，就可以這樣做
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con: # con = engine.connect()
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID") #
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
# Print head of DataFrame df
print(df.head())

#加條件
# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    "SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",
    engine
)
# Print head of DataFrame
print(df.head())