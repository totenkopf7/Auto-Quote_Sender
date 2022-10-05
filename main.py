import smtplib
import random
import datetime as dt


my_email = "Your Email"
my_password = "Your Email Password"
Email _To = "Destination Email Address"


now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

if day_of_week == 4:
    with open("quotes.txt", "r") as file:
        #     quotes_list = []
        #     for quote in file:
        #         quotes = quote.strip()
        #         quotes_list.append(quotes)
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=Email_To,
                            msg=f"subject: Your Today's Quote\n\nHello\n\nI hope this email finds you well,\n\n"
                                f"as this is the first day of the week, I just wanted to motivate you with this nice "
                                f"quote: "
                                f"\n\n{random_quote}")
