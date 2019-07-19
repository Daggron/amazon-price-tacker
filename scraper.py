import requests
from bs4 import BeautifulSoup
import smtplib
import time

'''
Change the url below for the product you want
'''

URL = 'https://www.amazon.in/Redux-Analogue-Blue-Watch-RWS0216S/dp/B07KVZD6XM/ref=sr_1_2?keywords=watch&qid=1563564397&s=computers&sr=8-2'
headers = {
    "User-Agents": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def check_price(yourPrice):

    page = requests.get(URL, headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[2:])

    if converted_price < yourPrice:
        send_mail(converted_price)
    else:
        print("Price is high")

    print(converted_price)
    print(title)


def send_mail(converted_price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('maihoodon01@gmail.com', 'gssndzbxtphqixhu')

    subject = 'Price Fell Down to' + str(converted_price) + ' !!!!'
    body = str('Check the price for your product ' + URL)

    msg = 'Subject:' + str(subject+"\n\n"+body)

    server.sendmail(
        'maihoodon01@gmail.com',   #sender mail address
        'returnofking04@gmail.com', #change your email here in order to get notification to your mail "Reciever mail"
        msg                         #content of mail
    )

    print("Mail Sent!")

    server.quit()


if __name__ == '__main__':
    while True:
        yourprice = float(input('The highest price of the product you want\n'))
        check_price(yourprice)
        time.sleep(60*60)
        ''' 
        change the time here in case you want to check the price more rapidly
         
         for e.g. putting 20 here will check the price after 20  secs and mail you in every 20 secs

        '''