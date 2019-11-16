import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com.br/Notebook-Aspire-AN515-51-50U2-GeForce-Windows/dp/B07BN4B1BT/ref=mp_s_a_1_1?keywords=gamer&pf_rd_i=17351089011&pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_p=ef912351-90e1-48b5-b855-dd350e81cf01&pf_rd_r=5Y046K91BRMXC17YW923&pf_rd_s=mobile-hybrid-5&pf_rd_t=1201&qid=1573902447&s=computers&sr=1-1'

headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI PLAY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")

# print(soup.prettify())
print(title)
