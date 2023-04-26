##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
# name,email,year,month,day
# YourName,your_own@email.com,today_year,today_month,today_day

import datetime as dt
import pandas
import smtplib
import random

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)  # tuple


MY_EMAIL = "@gmail.com"
MY_PASSWORD = ""


data = pandas.read_csv("Code_100/Day_32/birthday_wisher/birthdays.csv")
birthday_dict = {(data_row.month, data_row.day)                 : data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    rand = random.randint(1, 3)
    file_path = f"Code_100/Day_32/birthday_wisher/letter_templates/letter_{rand}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        updated_letter = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{updated_letter}")
