import requests
import csv
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")
first_quote=soup.find("a", class_="title")
print("___DATA EXTRACTION___")
print(first_quote)
print("____________________________")
all_quotes=soup.find_all("a",class_="title")
with open("laptops.csv","w",newline="",encoding="utf-8")as f:
    writer=csv.writer(f)
    writer.writerow("Product Name")
    for q in all_quotes:
        print("Found product: " + q.text)
        writer.writerow([q.text])