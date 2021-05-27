import smtplib
#
# my_email = "INSERT@gmail.com"
# password = "INSERT "
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="INSERTHERE",
#                         msg="Subject: Testing my Python\n\n  This is the body of my test message!")

import datetime as dt

now = dt.datetime.now() #this gets you the current date and time
year = now.year #you can get any part of the datetime string like this. Day, month, hour, etc..

date_of_birth = dt.datetime(year= 1993, month=12, day=15, hour=4) #Sept 15th 1993 at 4am


