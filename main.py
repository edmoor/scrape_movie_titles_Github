import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
news = soup.find_all(class_="article-title-description")

movies = []

for item in news:
    title_element = item.find(class_="title")
    if title_element:
        movies.append(title_element.get_text())

with open("lista.txt", "w") as file:
    file.write("\n".join(reversed(movies)))
