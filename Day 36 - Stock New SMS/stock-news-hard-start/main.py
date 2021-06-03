import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = ""
STOCK_API = ""

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
TO_NUMBER = ...
FROM_NUMBER =  ...

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

YESTERDAY = str(datetime.date.today() + datetime.timedelta(days=-1))
DAY_BEFORE_YESTERDAY = str(datetime.date.today() + datetime.timedelta(days=-2))



##TODO: STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday.
#       Find the positive difference between the two prices. e.g. 40 - 20 = -20,
#       but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.


stock_response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&output=compact&symbol={STOCK}&apikey={STOCK_API}")
stock_data = stock_response.json()

yesterdays_close = float(stock_data["Time Series (Daily)"][YESTERDAY]["4. close"])
db4_yesterdays_close = float(stock_data["Time Series (Daily)"][DAY_BEFORE_YESTERDAY]["4. close"])


if yesterdays_close < db4_yesterdays_close:
    a = yesterdays_close
    b = db4_yesterdays_close
else:
    a = db4_yesterdays_close
    b = yesterdays_close

print(yesterdays_close, db4_yesterdays_close)
percentage_different = int(round(100 - (a / b * 100)))
print(percentage_different)


##TODO: STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

news_response = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}")
news_data = news_response.json()
# first_three_articles = news_data["articles"][:3] ##first articles
#title
#description

article= news_data["articles"]
article1= news_data["articles"][0]["title"]

##TODO: STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
#
if percentage_different >= 2:
    message1 = client.messages \
        .create(
             body=f"[TSLA] Title: {article1}",
             from_=FROM_NUMBER,
             to=TO_NUMBER
     )
    print(message1.sid)

    # message2 = client.messages \
    #     .create(
    #         body=f"<TSLA> \n Title: '{article}[1]['title']' \n Brief: {article}[1]['description']",
    #         from_=FROM_NUMBER,
    #         to=TO_NUMBER
    # )
    # print(message2.sid)

    print("done and done")




                                              


#TODO:#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

