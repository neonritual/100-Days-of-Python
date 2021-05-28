
import pandas as pd
import datetime as dt
import random


date = dt.datetime.today()
today_month = date.month
today_day = date.day
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


def write_letter():
    letter_num = random.randint(1, 3)
    get_letter = open(f"./letter_templates/letter_{letter_num}.txt", "rt")
    new_letter = open("./letter_templates/new_letter.txt", "wt")
    for line in get_letter:
        new_letter.write(line.replace('[NAME]', birthdays_dict[today]["name"]))

    get_letter.close()
    new_letter.close()




def send_email():
    import smtplib
    #
    my_email = "###Insert Email Login Here"
    password = "###Insert Email Password Here"
    new_letter = open("./letter_templates/new_letter.txt", "r")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="### Insert the FROM Email here.",
                        msg=f"Subject: Happy Birthday!\n\n  {new_letter.read()}")
    new_letter.close()


if today in birthdays_dict:
    write_letter()
    send_email()