import requests
from bs4 import BeautifulSoup as be
html="https://www.islamicfinder.org/world/united-kingdom/2644210/liverpool-prayer-times/?language=id"
# print(html)
#untuk menampilkan url
jadwalsolat=requests.get(html).text
# print(jadwalsolat)
#untuk menampilkan situs dalam bentuk teks (bisa juga dalam bentuk json dan content)
parser=be(jadwalsolat,"html.parser")
# print(parser)
#untuk menmapilkan website menjadi format html
namaelemen=parser.find("div",attrs={'class':"pt-card-tiles"})
print(namaelemen.text.replace("\n",""))
#untuk menampilkan nama elemen berbentuk teks dalam json