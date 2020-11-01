import discord
import requests
from bs4 import BeautifulSoup
client = discord.Client()

url = 'https://www.supremenewyork.com/shop/accessories/t1e9xord8/bxd1pzhyu'
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
x = True
while x:
    try:
        if soup.find('input',{'class':'button'}):
            price = soup.find()
            print("in stock")
            x = False
            xa = "Send"
            @client.event
            async def on_ready():
                if xa == "Send":
                    text_channel = client.get_channel(770388223448449035)
                    myEmbed = discord.Embed(title="Supreme Restock ",  color=0x0000FF)
                    myEmbed.add_field(name=url, value="supreme",  inline=False)
                    myEmbed.set_footer(text="")
                    myEmbed.set_author(name="@Saturnkicks on ig")
                    await text_channel.send(embed=myEmbed)
                    
    except:
        pass
       



        
    
client.run('NzY3NTEwOTQ2MjU1NDcwNjQ0.X4y-RQ.qVwcQ-GLIHqQSCcgInpxpnT_0qg')