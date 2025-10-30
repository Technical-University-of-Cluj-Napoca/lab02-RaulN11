import requests
from bs4 import BeautifulSoup
import sys
url="https://dexonline.ro/definitie/"
if len(sys.argv)!=2:
    exit()
else:
    word = sys.argv[1]
url=url+word
x=requests.get(url)
if(x.status_code!=200):
    print("Error")
soup = BeautifulSoup(x.text, 'html.parser')
result=soup.find("span", class_="def").get_text()
print(result)
