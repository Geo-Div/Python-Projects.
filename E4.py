Exercise 4: Change the urllinks.py program to extract and count paragraph (p)
tags from the retrieved HTML document and display the count of the paragraphs
as the output of your program. Do not display the paragraph text, only count
them. Test your program on several small web pages as well as some larger web
pages.

Answer:
import urllib.request
from bs4 import BeautifulSoup

url = input("Enter URL: ")
try:
    html = urlib.request.urlopen(url).read()
except:
    print("Improperly formatted or non-existent URL")
    quit()

soup = eautifulSoup(html, "html.parser")

tags = soup("p")
print("Number of paragraphs:", len(tags))