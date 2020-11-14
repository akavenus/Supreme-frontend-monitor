import requests
from bs4 import BeautifulSoup
from dhooks import Webhook, Embed
import time
import lxml
from fake_headers import Headers
s = requests.Session()
headers = Headers(os="mac", headers=True).generate()
url = 'https://www.supremenewyork.com/shop/accessories/vqfyz36pa/swqgeku2i'
Delay = 5 #Delay between each requests that you send to monitor the site
response = s.get(url, headers=headers).text
soup = BeautifulSoup(response, 'lxml') 
x = True
while x:
    try:
        if soup.find('input',{'class':'button'}):
            print("in stock")
            price_x = soup.find('p', class_='price').text
            name_x = soup.find('h2', class_='protect').text
            picture = soup.find(id='img-main')

            film_id = 'img-main'
            raw_picture = soup.find(itemprop="image")
            picture_x = 'https:' + (raw_picture["src"])
            print(picture_x)
            x = False
            embed = Embed(title='Supreme Restock', description='', color=0x5CDBF0, timestamp='now')
            hook = Webhook("https://discord.com/api/webhooks/775197355234426900/nbFhxu4gWP8dPrenMIf_xzSBxiHHkaMKGn6Tx3KTTHiLmQH-XWkBGtG2hugrxxScLKjs")
            embed.set_author(name='Supreme monitor')
            embed.set_image(picture_x)
            embed.add_field(name="Product", value=name_x)
            embed.add_field(name="Price", value=price_x)
            embed.add_field(name="Link", value=url)
            embed.set_footer(text='This bot was coded by Venus#9210')
            hook.send(embed=embed)
            time.sleep(Delay)

    except:
        print("error finding product or out of stock")
        time.sleep(Delay)
        x = False
