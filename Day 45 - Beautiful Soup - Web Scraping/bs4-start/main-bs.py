from bs4 import BeautifulSoup
import requests


response = requests.get("http://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

## TO Get all the Story Titles:
# stories = soup.select(selector=".storylink")
# for story in stories:
#     print(story.getText())
#
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().strip(' points')) for score in soup.find_all('span', class_='score')]

## Find article w/ most upvotes and it's index.
max_upvotes = max(article_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)
# print(max_upvotes)
# print(max_upvotes_index)

print(article_texts[max_upvotes_index])
print(article_links[max_upvotes_index])





# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.prettify())
# #
# # all_anchor_tags = soup.find_all(name="a") #Isolates all <a> tags in the page.
# # for tag in all_anchor_tags:
# #     # print(tag.getText()) #This gets just the name of the links.
# #     # print(tag.get("href")) #This gets just the URLs of the links.
#
# # head = soup.find(name="h1", id="name") #Isolates the first h1 heading that also has he id name.
# #### THis uses soup.find and not find_all because there is only one.
# # print(head)
#
# # section_heading = soup.find(name="h3", class_="heading") #This lso isolates by class,
# # HOWEVER Python doesnt allow the use of class in this way (it can only refer to an object class), so it becomes class_)
# # print(section_heading )
#
#
# ####You can use CSS selectors as well:
# company_url = soup.select_one(selector="p a") #looking for an a tag inside a p tag.
# print(company_url)
#
# name = soup.select_one(selector="#name") #Finding element w id of "name".
# print(name)
#
# headings = soup.select(".heading") #FInding elements with a "heading" class.
# print(headings)