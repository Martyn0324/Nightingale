from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen("https://www.msdmanuals.com/professional") as url:
    test = url.read()


soup = BeautifulSoup(text, "html_parser")
paragraphs = soup.find_all("p")

for p in paragraphs:
    text = p.get_text()
    print(text)
    
