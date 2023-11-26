import requests
from send_email import send_email
# Eg: basically we do serach thing in web app like google chorme using url
# In python we need to read thorough requests module.

api = '86021958d416448fb37a9e8f6a2464a9'

#this api id is created but newapi.org throught web using mail

#This url also created by newaapi.org after creating account
#this is created using my api account automatically.
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2023-10-26&sortBy=publishedAt&"
       "apiKey=86021958d416448fb37a9e8f6a2464a9&language=en")

request = requests.get(url) # get funtion will extract the url into requests
#content = request.text #it should be in text formate
# you will entire web while printing content

content = request.json() # we need out data in json because we need to extract particulaer data

boby = ""
for article in content['articles']: # key = content['articles']
#     print(article['title']) # inside content['articles'] we to extract only title
#     print(article['description'])# inside content['articles'] we to extract only description
# print(content)
    if article['title'] is not None:
        boby = "subject: Todays News"+(boby + article['title'] + '\n'
                + article['description'] + '\n'
                + article['url']+ 2*'\n')

boby = boby.encode('utf-8')
send_email(message=boby)