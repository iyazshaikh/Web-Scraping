import requests
import json
from bs4 import BeautifulSoup

url = "https://www.amazon.in/gp/product/B089F5JGM1/ref=s9_acss_bw_cg_Lap_1a1_w"

headers = {'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}


r = requests.get(url, headers= headers)

soup = BeautifulSoup(r.content, features="lxml")

image= []
for img in img:
    image.append(img['src'])


title = soup.select("#title")[0].get_text().strip()
price = soup.select("#priceblock_ourprice")[0].text.replace('\u20b9\u00a0','').strip()
img = soup.select('img[src^="https://images-na.ssl-images-amazon.com/images/I"]')[:6]
categorie = soup.select('#variation_pattern_name')[0].text.replace('\n',' ')
review_count = int(soup.select("#acrCustomerReviewText")[0].get_text().split()[0])
feature =  soup.findAll(id="featurebullets_feature_div")[0].get_text()
des =  soup.select("#productDescription")[0].text.replace('\n',' ')
short = feature[4:120] 




jsonObject = {'title':title,'price':price,'review_count':review_count,'short':short,'categorie':categorie,'des':des,'image':image}
print(json.dumps(jsonObject, indent=2))


    