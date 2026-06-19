import smtplib
import datetime as dt
import random
now = dt.datetime.now()
year = now.year
my_email = "cadec292@gmail.com"
my_password = "kxot mhts pvna oqka"

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, 
                        to_addrs="fallynmcconnell3@gmail.com", 
                        msg=f"Subject:Hello\n\n{quote}"
    )
        
def send_quote():
    # if now.weekday() == 0:
         with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)
            print(quote)            
            send_email(quote)


send_quote()