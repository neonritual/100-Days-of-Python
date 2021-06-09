
from twilio.rest import Client
from secrets import *
from smtplib import *
from secrets import *

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_SMS(self, price, city, code, dateto, datefrom):
        client.api.account.messages.create(
            to=to_number,
            from_=from_number,
            body=f"Low Price Alert! Only {price} from London-LON to {city}-{code} from {dateto} to {datefrom}")


    def send_emails(self, receiver_email, price, city, code, dateto, datefrom):
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=email_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=receiver_email,
                                msg=f"Subject: Low Price Alert!\n\n  Only {price} from London-LON to {city}-{code} from {dateto} to {datefrom} \n\nURL: https://www.google.co.uk/flights?hl=en#flt=LON.{code}.{dateto}*{code}.LON.{datefrom} ")

        # sender = my_email
        # receivers = [receiver_email]
        #
        # message = f"""
        # Subject: Low Price!
        #
        # Only {price} from London-LON to {city}-{code} from {dateto} to {datefrom} \n\nURL: https://www.google.co.uk/flights?hl=en#flt=LON.{code}.{dateto}*{code}.LON.{datefrom} ")
        #
        # """
        #
        # try:
        #     smtpObj = SMTP("smtp.gmail.com", 587)
        #     smtpObj.sendmail(sender, receivers, message)
        #     print
        #     "Successfully sent email"
        # except SMTPException:
        #     print
        #     "Error: unable to send email"
        #
