from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_site = response.text

soup = BeautifulSoup(empire_site, "html.parser")


#
titles = soup.find_all(name="h3", class_="title")
print(titles)
#
# print(titles)
# # title_texts = []
# # for title in titles:
# #     text = title.getText()
# #     title_texts.append(text)
#
# # print(title_texts)
#
# # jsx-4245974604