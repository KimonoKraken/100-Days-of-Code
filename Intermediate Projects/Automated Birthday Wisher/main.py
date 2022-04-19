import smtplib
import datetime as dt
import random
import pandas

my_email = "dimitriyk25@gmail.com"
password = "CLEARED"

now = dt.datetime.now()
today_tuple = (now.month, now.day)
year = now.year
month = now.month
day = now.day
weekday = now.weekday() # 0 = monday, 1 = tuesday, etc


# Checks if today is the birthday of anyone in the birthdays.csv file, if so, sends birthday email
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents_updated = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:HAPPY BIRTHDAY!!!!!\n\n{contents_updated}"
                            )

