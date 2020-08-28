import requests
import re
from bs4 import BeautifulSoup
from googletrans import Translator
import sys

#リンクをを取得	
r = requests.get("https://news.yahoo.co.jp/topics/top-picks")
	
#ニュースリストを取得

soup = BeautifulSoup(r.text, "html.parser")

search = soup.find_all("a")
news=soup.find("ul", "newsFeed_list")

translator = Translator()
for tag in news:
    trans = translator.translate(tag.get_text())
    print(trans.text)
input("Press Enter to finish the program")
