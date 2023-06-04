#迴圈會先跑子內容，再跑general的內容
def shout():#general
    shout_word = 'congratulations' + '!!!' #子
    print(shout_word) #子
shout()# general

# shout的內容可以自己設定
def shout(word):
    shout_word = word + '!!!'
    print(shout_word)
shout('hi')

#說明一下return在定義時的功用
def shout(word):
    shout_word = word + '!!!'
    return(shout_word) #系統會把shout_word存起來，等你用print就印出來
yell = shout('congratulations')
print(yell)

def shout(word1, word2):
    shout1 = word1 +'!!!'
    shout2 = word2 +'!!!'
    new_shout = shout1 + shout2
    return new_shout
yell = shout('hey', 'you')
print(yell)

num1, num2, num3 = nums #可以反過來定義
even_nums = [2,4,6]

#一個小作業
import pandas as pd
df = pd.read_csv('xxx.csv')
langs_count = {} #建立一個空的空間
col = df['lang'] #col定義為df裡的lang column
for entry in col: #for 一個變數，在lang column裡，一個一個跑col裡的東西
    if entry in langs_count.keys(): #如果跑col的過程中，有一個key則數字加1
        langs_count[entry] +=1
    else:
        langs_count[entry] = 1 #沒有則維持1
print(langs_count)

#用定義方式跑
def count_entries(df, col_name):
    langs_count = {}
    col = df[col_name]
    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1
    return langs_count
result = count_entries(tweets_df, 'lang')
print(result)

#nest def
def three_shouts(word1, word2, word3):
    def inner(word):
        return word +'!!!'
    return(inner(word1), inner(word2), inner(word3))
print(three_shouts('a','b','c'))

#定義可以先定默認的東西
def shout_echo(word1, echo = 1): #echo被默認為1

#定義可以定義成括號裡所有東西都跑迴圈
def add_all(*args):
    sum_all = 0
    for num in args:
        sum_all += num
    return sum_all
add_all(1,2,3,4,5,6) #最後就會把括號中的所有東西加總

#定義dictionary
def print_all(**kwargs):
    for key, value in kwargs.items():
        print(key + ':' + value)
print_all(name='dumbledore', job='headmaster')

#簡易定義lambda
echo_word = (lambda word1, echo: word1 * echo) #基本上就是lambda 變項: 公式, list
result = echo_word('hey', 5)
print(result)

#lambda進階
spells = ["protego", "accio", "expecto patronum", "legilimens"]
shout_spells = map(lambda item: item + '!!!', spells) #spells是一個list, item從這個list裡拿的
shout_spells_list = list(shout_spells)
print(shout_spells_list)

#Error定義1
def shout_echo(word1, echo=1):
    echo_word = ''
    shout_words = ''
    try:#類似if 與 else
        echo_word = word1*echo
        shout_words = echo_word + '!!!'
    except:
        print("word1 must be a string and echo must be an integer.")
    return shout_words
shout_echo("particle", echo="accelerator")

#Error定義2
def shout_echo(word1, echo=1):
    if echo < 0: #raise就是自訂這個錯誤是甚麼類型
        raise ValueError('echo must be greater than or equal to 0')
        echo_word = word1 * echo
        shout_word = echo_word + '!!!'
        return shout_word
    shout_echo("particle", echo=5)