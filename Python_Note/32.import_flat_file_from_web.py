#URL = Universal Resourse Locators

# Import package
from urllib.request import urlretrieve
# Import pandas
import pandas as pd
# Assign url of file: url
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Save file locally
urlretrieve(url, 'winequality-red.csv') #我們向http發出請求，並存檔在我們電腦裡
# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())


# Import packages
import matplotlib.pyplot as plt
import pandas as pd
# Assign url of file: url
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')
# Print the head of the DataFrame
print(df.head())
# Plot first column of df
df.iloc[:, 0].hist()
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

# Import package
import pandas as pd
# Assign url of file: url
usl = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# Read in all sheets of Excel file: xls
xls = pd.read_excel(usl, sheet_name = None)
# Print the sheetnames to the shell
print(xls.keys())
# Print the head of the first sheet (using its name, NOT its index)
print(pd.read_excel(usl, sheet_name = '1700').head())

#HTML = hyperText Markup Language
#************爬蟲!!!!!************ very important!!! web crawler
from urllib.request import uslopen, Request
usl = 'https://www.wikipedia.org/'
request = Request(usl)
response = urlopen(request)
html = response.read()
response.close()

#簡單版
import requests
usl = 'https://www.wikipedia.org/'
r = requests.get(usl)
text = r.text

#example/ assignment
# Import package
from urllib.request import urlopen, Request
# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"
# This packages the request: request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(request)
# Print the datatype of response
print(type(response))
# Be polite and close the response!
response.close()


#用Soup來美化在網路上拿到的東西
# Import packages
import requests
from bs4 import BeautifulSoup
# Specify url: url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()
# Print the response
print(pretty_soup)


#要在網頁裡找到title 用.title function
# Import packages
import requests
from bs4 import BeautifulSoup
# Specify url: url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extract the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Get the title of Guido's webpage: guido_title
guido_title = soup.title #提取標題
# Print the title of Guido's webpage to the shell
print(guido_title)
# Get Guido's text: guido_text
guido_text = soup.get_text() #提取文本
# Print Guido's text to the shell
print(guido_text)



#用for loop來找網頁中所有的超連結
# Import packages
import requests
from bs4 import BeautifulSoup
# Specify url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Print the title of Guido's webpage
print(soup.title)
# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a') #'a'是超連結
# Print the URLs to the shell
for link in a_tags:
    print(link.get('href')) #href是超連結的意思

#example JSON，JSON是一種傳送api的訊息到server的檔案類型，跟HTML 
# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

#以HTML方式抓檔案下來
# Import requests package
import requests
# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Print the text of the response
print(r.text)

#以json方式抓，json的檔案會更加的容易讀，很整齊，以dictionary 方式呈現
# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Decode the JSON data into a dictionary: json_data
json_data = r.json()
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

# Import package
import requests
# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Decode the JSON data into a dictionary: json_data
json_data = r.json()
# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)


#實際使用twitter api來取得資料試試
# Store credentials in relevant variables #這四個東西都是在申請twitter 帳號的時候可以拿到的，如果真的要用的話就要開啟相關功能
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
# Create your Stream object with credentials
stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret) #輸入這些以登入
# Filter your Stream variable
stream.filter(['clinton','trump','sanders','cruz']) #篩選這些單詞



# Import package
import json
# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'
# Initialize empty list to store tweets: tweets_data
tweets_data = []
# Open connection to file
tweets_file = open(tweets_data_path, "r")
# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line) #把tweets_data_path內的每一個tweets用json來讀取
    tweet = tweets_data.append(tweet) #然後加在tweets_data裡
# Close connection to file
tweets_file.close()
# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Import package
import pandas as pd
# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])
# Print head of DataFrame
print(df.head())


import re
def word_in_text(word, text):
    word = word.lower()
    text = text.lower() #lower大寫變小寫
    match = re.search(word, text) #會幫忙找出text裡有沒有word這個東西，一般會輸入資料格式
    if match:
        return True
    return False
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0] #設定基本值
# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows(): #df.iterrows() 用在dictionary的loop
    clinton += word_in_text('clinton', row['text']) #如果df入面有clinton就會+1，如果df裡有的話，word_in_text就會回傳True，使clinton += 成立，然後加一
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns
# Set seaborn style
sns.set(color_codes=True)
# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']
# Plot the bar chart
ax = sns.barplot(cd, [clinton, trump, sanders, cruz]) #x = cd, y = [clinton, trump, sanders, cruz]的資料
ax.set(ylabel="count")
plt.show()
