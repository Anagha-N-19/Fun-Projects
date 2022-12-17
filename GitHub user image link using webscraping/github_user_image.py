import requests
from bs4 import BeautifulSoup

user_name = input("Enter Username: ")
URL = f"https://github.com/{user_name}"
response = requests.get(URL)
web_pg = response.content
soup = BeautifulSoup(web_pg, 'html.parser')
profile_image = soup.find('img',{'alt':'Avatar'})['src']
print("Link for image:",profile_image)
