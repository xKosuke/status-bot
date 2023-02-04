import discord
import socket
import asyncio
import pytz
import ping3
from datetime import datetime

client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents(messages=True, guilds=True)

@client.event
async def on_ready():
    tchannel = client.get_channel(ID DU SALON) # <- MET L'ID DU SALON ICI A LA PLACE DE "ID DU SALON"
    await tchannel.send("Copie l'ID de ce message et met ligne 15 !")  # NE MODIF PAS
    tmessage = await tchannel.fetch_message(ID DU MESSAGE) # <- MET L'ID DU MESSAGE ICI
    hosts = [("www.google.com", 443, "Google"), ("reddit.com", 443, "Reddit"), ("188.114.97.2", 80, "Cloudflare")]
    await asyncio.ensure_future(editembed(tmessage, hosts))

async def editembed(tmessage, hosts):
    requetes = 0
    while True:
        embed = discord.Embed(title="Kosuke - Status", color=discord.Color.green(), timestamp=datetime.utcnow())
        embed.set_image(url="https://cdn.discordapp.com/attachments/1008470729861365780/1071430782549229578/IMG20221209161133.png")
        for host, port, nom in hosts:
            try:
                host_name = host
                host = socket.gethostbyname(host)
                tempsreponse = ping3.ping(host)
                tempsreponse = round(tempsreponse, 3)
                tempsreponse = "{:.3f} ms".format(tempsreponse)
                s = socket.create_connection((host, port), 2)
                s.close()
                embed.add_field(name=nom, value="<a:on:1071438974150770728> ({})".format(tempsreponse), inline=True)
            except:
                embed.add_field(name=nom, value="<a:off:1071438984678486088> **OFF**", inline=True)
        fr_timezone = pytz.timezone("Europe/Paris")
        fr_datetime = datetime.now(fr_timezone)
        requetes += 1
        embed.set_footer(text=f"Mis à jour à {fr_datetime.strftime('%H:%M:%S')} | Nombre de requêtes : {requetes}")
        await tmessage.edit(content=None, embed=embed)
        await asyncio.sleep(10)

client.run('TOKEN ICI')
