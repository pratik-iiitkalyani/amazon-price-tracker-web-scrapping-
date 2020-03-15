import requests
from bs4 import BeautifulSoup
import smtplib
import time

# url of product
URL = "https://www.amazon.in/Mi-20000mAH-Li-Polymer-Sandstone-Charging/dp/B07VXJS7DH/ref=sr_1_5?crid=10E2BF63U8P7R&keywords=power+bank+20000+mah&qid=1575865163&sprefix=power+bank+20000mah%2Caps%2C278&sr=8-5"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:7].replace(',', ""))
    if converted_price < 2000:
        send_email()
    print(title.strip())

def send_email():
    print("asdh")
    smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()

    smtpserver.login('pratik@iiitkalyani.ac.in', wkfroqgwgovfngdg)

    subject = 'Price fell down!'
    body = f'Check the amazon link {URL}'

    msg = f"Subject: {subject}\n\n{body}"

    smtpserver.sendmail(
        'pratik@iiitkalyani.ac.in',
        'pkraja121dss@gmail.com',
        msg
    )

    print("Hey Email has been sent!")
    smtpserver.quit()

while(True):
    check_price()
    time.sleep(60*60)