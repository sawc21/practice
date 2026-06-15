import smtplib

my_email = "cadec292@gmail.com"
my_password = "kxot mhts pvna oqka"


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="cadecade614@yahoo.com", 
                        msg="Subject:Hello\n\nThis is the body of the email."
    )