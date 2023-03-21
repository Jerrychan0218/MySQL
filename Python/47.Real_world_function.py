#time###############################################################
import time
def timer(func): #可以測你的function跑了多久，args就是function名稱
    def wrapper(*args, **kwargs): #args 及keyword args，*args是輸入任意數量的參數，**kwargs是dict格式，指輸入任意key，比如wrapper(22,33, k1=44, k2=55)
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
        return result 
    return wrapper

@timer #代表會執行上面定義好的計算秒數function
def sleep_n_seconds(n):
    time.sleep(n) #延遲執行的秒數
sleep_n_seconds(5)    
#出來的結果是sleep_n_seconds took 5.010701656341553s，因為延遲了5秒，所以實際執行了5.010701656341553-5 的時間

#也就是說他執行了
def timer(sleep_n_second): #可以測你的function跑了多久，args就是function名稱
    def wrapper(5): #args 及keyword args，*args是輸入任意數量的參數，**kwargs是dict格式，指輸入任意key，比如wrapper(22,33, k1=44, k2=55)
        t_start = time.time() #執行的開始時間
        result = sleep_n_second(5) #def wrapper時的5用在這裡
        t_total = time.time() - t_start #執行完再測一次時間，減掉一開始執行的開始時間
        print('{} took {}s'.format(func.__name__, t_total)) #print出sleep_n_second took t_total s
        return result 
    return wrapper

#memoize##############################################################
def memoize(func): #會儲存第一次執行function後的結果，以便之後使用
    cache = {} #建立一個dict來儲存東西
    def wrapper(*args, **kwargs):
        if(args, kwargs) not in cache: #如果現在輸入的東西沒有在cachs裡
            cache[(args, kwargs)] = func(*args, **kwargs)
        return cache[(args, kwargs)]
    return wrapper

@memoize
def slow_function(a,b):
    print('sleeping...')
    time.sleep(5)
    return a + b

slow_function(3,4) #當我們輸入後，會跑5秒才挑出7

def memoize(slow_function):
    cache = {}
    def wrapper(3, 4):
        if(3, 4) not in cache:
            cache[(3, 4)] = slow_function(3, 4)
        return cache[(3, 4)]
    return wrapper

slow_function(3,4) #當我們輸入第2次，就會立即跳出7，因為memoize已經記住了

#print_type###########################################################
def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

#function_count#########################################
def counter(func): #計算用了幾次同一個function
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func(*args, **kwargs)
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))

#當我們定義了function，或想知道別人的function在做什麼，便可以用
def sleep_n_seconds(n=10)
print(sleep_n_seconds.__doc__) #可以了解function的說明，docstring，__doc__等等這種叫作matadata
print(sleep_n_seconds.__defaults__) #可以知道function的預設值



