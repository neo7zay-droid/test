import requests
from bs4 import BeautifulSoup
url="https://quotes.toscrape.com"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")
first_quote=soup.find("span",class_="text").text
print("___DATA EXTRACTION___")
print(first_quote)
print("____________________________")