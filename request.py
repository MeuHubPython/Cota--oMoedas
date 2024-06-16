import requests
from bs4 import BeautifulSoup

link_dolar = "https://www.bing.com/search?q=cotacao+dolar"
link_euro = "https://www.bing.com/search?q=cotacao+euro"
link_libra = "https://www.bing.com/search?q=cotacao+libra"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

requisicao_dolar = requests.get(link_dolar, headers=headers)
requisicao_euro = requests.get(link_euro, headers=headers)
requisicao_libra = requests.get(link_libra, headers=headers)

site_dolar = BeautifulSoup(requisicao_dolar.text, "html.parser")
site_euro = BeautifulSoup(requisicao_euro.text, "html.parser")
site_libra = BeautifulSoup(requisicao_libra.text, "html.parser")

dolar = site_dolar.find("input", id="cc_tv")
euro = site_euro.find("input", id="cc_tv")
libra = site_libra.find("input", id="cc_tv")

