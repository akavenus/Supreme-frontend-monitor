#To do
#Add proxy support
#Add more loops to monitor multiple products
#Make the discord alert message contain more details about the product. Such as the product image

import discord
import requests
from bs4 import BeautifulSoup
client = discord.Client()
url = 'https://www.supremenewyork.com/shop/accessories/t1e9xord8/bxd1pzhyu'
x = True
while x:
    try:
        if soup.find('input',{'class':'button'}):
            response = requests.get(url).text
            soup = BeautifulSoup(response, 'lxml') 
            price = soup.find()
            print("in stock")
            price_x = soup.find('p', class_='price').text
            name_x = soup.find('h2', class_='protect').text
            x = False
            xa = "Send"
            @client.event
            async def on_ready():
                if xa == "Send":
                    text_channel = client.get_channel(770388223448449035)
                    myEmbed = discord.Embed(title="Supreme Restock ",  color=0x0000FF)
                    myEmbed.add_field(name="Name", value=name_x,  inline=False)
                    myEmbed.add_field(name="Price", value=price_x,  inline=False)
                    myEmbed.add_field(name="Link", value=url,  inline=False)
                    await text_channel.send(embed=myEmbed)
                    
    except:
        print("error")
        x = False
       

    
client.run('enter your token here')
