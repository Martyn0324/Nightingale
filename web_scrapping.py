from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
Search for databases with relation Disease ---> Symptom Incidence (must be or converted to %)

https://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html

'''

with urlopen("https://www.msdmanuals.com/professional") as url:
    test = url.read()


soup = BeautifulSoup(text, "html_parser")
paragraphs = soup.find_all("p")

for p in paragraphs:
    text = p.get_text()
    print(text)
    
