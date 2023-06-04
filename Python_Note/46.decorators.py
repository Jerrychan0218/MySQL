#decorator 裝飾器 用來改變執行function時的input、output，又或者是function本身，可以簡化function的code



@double_args #會在前面加上@，double_args會將function入面要輸入的args都乘以2，再執行function
def multuply(a,b):
    return a*b
multiply(1,5) #因為有@double_args，所以args = a同b就會自動乘2，變成2,10

#另外一種
def my_function(a, b, c):
  print(a + b + c)
# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function) #print_args系一種decorator
my_function(1, 2, 3)

#也可以這樣，結果跟上面一樣
@print_args
def my_function(a, b, c):
  print(a + b + c)
my_function(1,2,3)

#要如何自訂意一個decorate呢?

def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args) #multply(5,10)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

############################################
@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)