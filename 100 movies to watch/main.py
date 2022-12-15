import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_pg = response.text
soup = BeautifulSoup(web_pg, 'html.parser')

divname = soup.select(selector='div h3')  # put name of the required class
# print(divname)
divname.reverse()
with open('movie_names.txt', 'a', encoding="utf-8") as file_ob:
    file_ob.write("GREATEST MOVIES TO WATCH\n")
    for tag in divname:
        movie = tag.getText()
        file_ob.write(f"{str(movie)}\n")
