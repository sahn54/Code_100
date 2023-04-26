import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day = now.weekday()


MY_EMAIL = "sungpower177@gmail.com"
MY_PASSWORD = "yvnmixdwegciqwus"


num = 0
if day == 1:
    with open("Code_100/Day_32/quotes.txt") as file:
        all_quotes = file.readlines()
        today_quote = random.choice(all_quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject:Motivation\n\n{today_quote}")  # type: ignore
