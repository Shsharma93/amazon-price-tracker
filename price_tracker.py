from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import requests
import smtplib
import time

load_dotenv()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('play.skmr@gmail.com', os.getenv("PASSWORD"))

    msg = create_email()
    server.sendmail('play.skmr@gmail.com', 'shsharma1122@hotmail.com', msg)
    print('Email sent')
    server.quit()


def create_email():
    subject = "Price fell down!!!"
    body = f'check the amazon link {os.getenv("URL")}'
    return f'Subject: {subject} \n\n {body}'


def check_price():
    URL = os.getenv("URL")

    page = requests.get(URL, os.getenv("HEADERS"))
    soup = BeautifulSoup(page.content, 'html.parser')
    #title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().replace(',', '')
    price = float(price[1:6])

    if price > 1500:
        send_email()


while(True):
    check_price()
    time.sleep(60 * 60 * 24)
