import pandas
import datetime
import random
import smtplib

my_email = "sample@gmail.com"
password = "password"

today = datetime.datetime
today = today.now()
today_month = today.month
today_date = today.day

all_birthdays = pandas.read_csv("birthdays.csv")
all_birthdays_dict = all_birthdays.to_dict(orient="records")

for i in range(len(all_birthdays_dict)):
    if today_month == all_birthdays_dict[i]["month"] and today_date == all_birthdays_dict[i]["day"]:
        all_letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
        letter = random.choice(all_letters)

        with open(file=letter, mode="r") as letters:
            letter = letters.read()
            letter = letter.replace("[NAME]", all_birthdays_dict[i]["name"])



        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=all_birthdays_dict[i]["email"],
                msg=f"Subject:Happy Birthday\n\n{letter}"
            )

