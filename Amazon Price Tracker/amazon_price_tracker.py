import requests
from bs4 import BeautifulSoup
import string
import smtplib

my_email = "abcd@gmail.com"
my_pass = "aaaaaaaaa"

URL = "https://www.amazon.in/boAt-Wave-Call-Dedicated-Multi-Sport/dp/B0B5B6PQCT?ref_=Oct_DLandingS_D_c92d352c_60&th=1"
response = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"})
web_pg = response.text
soup = BeautifulSoup(web_pg, 'html.parser')
# print(response)

name_of_product = soup.find(id="productTitle").getText().strip()
# print(name_of_product)
price_tag = soup.find(class_='a-price-whole').getText()
price_tag = int(price_tag.translate(str.maketrans('', '', string.punctuation)))

if price_tag > 1250:
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(my_email, my_pass)
    connection.sendmail(from_addr=my_email, to_addrs=my_email,
                        msg=f"Subject:Low price for {name_of_product}\n\n\n Get your product at amazon for Rs {price_tag}.\nLink{URL}")
