#簡單以zscore為例子

def standardize(column):
  """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
  # Finish the function so that it returns the z-scores
  z_score = (column - column.mean()) / column.std()
  return z_score

# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df['y1_gpa'])
df['y2_z'] = standardize(df['y2_gpa'])
df['y3_z'] = standardize(df['y3_gpa'])
df['y4_z'] = standardize(df['y4_gpa'])


def better_add_column(values, df=None):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  # Update the function to create a default DataFrame
  if df is None:
    df = pandas.DataFrame()
  df['col_{}'.format(len(df.columns))] = values
  return df


  #context managers
  with open('my_file.txt') as my_file: #with是告訴python你要開一個context，open function 就是context manager
# with <context-manager>(<arguements>) as <variable-name>:
    text = my_file.read()
    length = len(text)
print('the file is {} characters long'.format(length))

with open('alice.txt') as file:
  text = file.read() #讀檔 alice.txt
n = 0
for word in text.split(): #把alice.txt的文字都分開，然後裡面的東西
  if word.lower() in ['cat', 'cats']: #如果這些東西變成小寫，是['cat', 'cats']，就增加一個記數
    n += 1
print('Lewis Carroll uses the word "cat" {} times'.format(n)) #format裡的東西，就是{}裡的東西。


def my_context():
    print('hello')
    yield 42 #return的意思，但會執行完剩下其他的code 
    print('goodbye')

#connect to the database
#定義
def database(url):
    db = postgres.connect(url)
    yield db

    db.disconnect()

#執行
url = 'http://datacamp.com/data'
with database(url) as my_db:
    course_list = my_db.execute(
        'select * From courses'
    )


#example
# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.
  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))
with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)

@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.
  Args:
    filename (str): The location of the file to read
  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()
with open_read_only('my_file.txt') as my_file:
  print(my_file.read())


# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for value in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))

def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)
  # Add code that lets you handle errors
  try: #code that might raise an error
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  except: #do something about the error
    
  finally: #this code runs no matter what
    os.chdir(current_dir) #os.chdir 改變目前資料夾到指定的資料夾；getcwd 返回當前工作目錄；os.listdir()返回某目錄路徑


#可以將好多function集結成function集，然後套用到資料，就會同時執行所有function
# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input() #此處是隨機讓python生成1-4個function，但在現實中是用來讓使用者輸入指令

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)


#檢查function有無寫說明=docstring
ok = has_docstring(load_and_plot_data)
if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")



#實作
def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b #return 到 def add(a,b)
    return add #return 到 create_math_function(func_name)
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(a, b):
      return a - b #return 到 def subtract(a, b)
    return subtract #return 到 create_math_function(func_name)
  else:
    print("I don't know that one")
    
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))


#Scope
def read_files():
  file_contents = None

  def save_contents(filename):
    # Add a keyword that lets us modify file_contents
    nonlocal file_contents #nonlocal是指在nested function裡要對上層的東西更改的時候，就要用到
    if file_contents is None:
      file_contents = []
    with open(filename) as fin:
      file_contents.append(fin.read())
      
  for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
    save_contents(filename)
    
  return file_contents

print('\n'.join(read_files()))


def wait_until_done():
  def check_is_done():
    # Add a keyword so that wait_until_done() 
    # doesn't run forever
    global done #是指在function design外面的地方
    if random.random() < 0.1:
      done = True
      
  while not done:
    check_is_done()

done = False
wait_until_done()

print('Work done? {}'.format(done))


#找到nonlocal variable的值
def foo():
    a = 5
    def bar():
        print(a)
    return bar

func = foo() #這邊代表foo()被func所代表

func() #當我們這樣子，就代表print(a)這個動作，但a=5其實並不存在於def bar()裡，但python連這個都記住了，而且沒辦法改變

type(func.__closure__) 
len(func.__closure__)
func.__closure__[0].cell_contents #看過function裡有多少定義的東西後，因為只有1個，所以就找出這個的內容，得知原來python知道a=5

#一些資訊
def my_special_function():
  print('You are running my_special_function()') 
def get_new_func(func):
  def call_func():
    func()
  return call_func
new_func = get_new_func(my_special_function) #響呢到會將get_new_func同my_special_function assign 到new_func入面
# Redefine my_special_function() to just print "hello"
def my_special_function(): #呢到既my_special_function 系另一個新開始，吾會覆蓋上一個my_special_function
  print('hello')
new_func()

#next
def my_special_function():
  print('You are running my_special_function()')  
def get_new_func(func):
  def call_func():
    func()
  return call_func
new_func = get_new_func(my_special_function)
# Delete my_special_function()
del(my_special_function) #就算del左my_special_function，都吾會影響new_func入面個my_special_function
new_func()