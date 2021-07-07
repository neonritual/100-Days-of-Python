from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_site = response.text

soup = BeautifulSoup(empire_site, "html.parser")


#
titles = soup.find_all(name="h3", class_="title")
print(titles)
#\