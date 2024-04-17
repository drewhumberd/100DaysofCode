from bs4 import BeautifulSoup
import requests
import html

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
rawmovies = response.text

soup = BeautifulSoup(rawmovies, "html.parser")

titles = soup.find_all("h3", class_="title")

plaintitles = [title.get_text() for title in titles]
ordered_list = plaintitles[::-1]

with open("movies.txt", "a") as file:
    for movie in ordered_list:
        file.write(f"{movie}\n")