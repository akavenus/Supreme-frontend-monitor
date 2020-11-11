#To do
#Add proxy support
#Add more loops to monitor multiple products
#Make the discord alert message contain more details about the product. Such as the product image

import requests
from bs4 import BeautifulSoup
from dhooks import Webhook, Embed
url = 'https://www.supremenewyork.com/shop/accessories/g7u54g3ja/bxd1pzhyu'
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml') 
x = True
while x:
    try:
        if soup.find('input',{'class':'button'}):
            price = soup.find()
            print("in stock")
            price_x = soup.find('p', class_='price').text
            name_x = soup.find('h2', class_='protect').text
            x = False
            embed = Embed(
            description='',color=0x5CDBF0,
            timestamp='now'  # sets the timestamp to current time
            )
            hook = Webhook("enter your webhook here")
            embed.set_author(name='Twitter Monitor')
            embed.add_field(name="Name", value=name_x)
            embed.add_field(name="Price", value=price_x)
            embed.add_field(name="Link", value=url)
            embed.set_footer(text='This bot was coded by Venus#9210')
            hook.send(embed=embed)
    except:
        print("error finding product")
        x = False
       
