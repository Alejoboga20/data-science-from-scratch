from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.p
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()
print(first_paragraph_words)