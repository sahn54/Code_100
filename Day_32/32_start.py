import smtplib

# my_email = "@gmail.com"
# password = ""
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="@gmail.com", msg="Subject:Hello\n\n This is the body of my email.")

import datetime as dt

# current data and time
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

day_of_birth = dt.datetime(year=1995, month=3, day=22, hour=12)
print(day_of_birth)
