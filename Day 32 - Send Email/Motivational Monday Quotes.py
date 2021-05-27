import smtplib
import datetime as dt
import random
#
my_email = "INSERT@gmail.com"
password = "INSERT "
#



now = dt.datetime.now() #this gets you the current date and time
with open('quotes.txt', 'r') as q:
    quotes = q.readlines()

if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="INSERT",
                        msg=f"Subject: Today's Motivation\n\n  {random.choice(quotes)}")
else:
    pass
