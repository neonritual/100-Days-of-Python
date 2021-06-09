
from twilio.rest import Client
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
