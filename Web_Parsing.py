import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

file = open("news.csv", "w", encoding="utf-8_sig",newline="\n")
write_obj = csv.writer(file)
write_obj.writerow(["Title", "Date", "Link"])


index = 1
# while index <=6:
url = f"https://www.alia.ge/category/akhali-ambebi/page/{index}/"
res = requests.get(url)

html = res.text
print(html)
while index <=2:
    soup = BeautifulSoup(html, "html.parser")
    news_section = soup.find("div", class_="jeg_posts jeg_load_more_flag")
    all_news = news_section.find_all("article")

    for i in all_news:
        img_add = i.img.get('src')
        print(img_add)
        info = i.find("div", class_="jeg_postblock_content")
        title = info.h3.a.text.strip()
        print(title)
        date = i.find("div", class_="jeg_meta_date")
        time = date.a.text.strip()
        print(time)
        write_obj.writerow([title, time , img_add])

        index += 1
  # time.sleep(randint(15, 20))
