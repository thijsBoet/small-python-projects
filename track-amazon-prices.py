import requests
import smtplib
import time
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/PowerColor-Radeon-5700-8192MB-PCI/dp/B07WT15P2P/ref=sr_1_8?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=PowerColor+Radeon+RX+5700+Red+Dragon+8GB&qid=1582975984&sr=8-8#customerReviews'

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('creative.steve@gmail.com', 'paepcweydrflrcxo')

    subject = 'Price alert'
    body = 'Price Alert. Check the Amazon link: https://www.amazon.de/PowerColor-Radeon-5700-8192MB-PCI/dp/B07WT15P2P/ref=sr_1_8?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=PowerColor+Radeon+RX+5700+Red+Dragon+8GB&qid=1582975984&sr=8-8#customerReviews'

    msg = f'Subject: {subject} \n\n{body}'

    server.sendmail(
        'creative.steve@gmail.com',
        'creative.steve@gmail.com',
        msg
    )
    print('Email Alert has been send.')
    server.quit()

def check_price(url, prefered_price):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[0:3])
    if converted_price < prefered_price:
        send_mail()

while True:
    check_price(URL, 350)
    time.sleep(6)