import imp
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.jumia.com.gh/phones-tablets/"
url = requests.get(url,headers=headers)
url = url.content


result = BeautifulSoup(url,"lxml")

print(result.prettify())
