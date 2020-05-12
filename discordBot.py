import discord
from discord.ext.commands import Bot
from discord.ext import commands
###
#internetten veri çekmek için
import requests
from bs4 import BeautifulSoup
###

client=discord.Client()
bot_prefix="/";
bot = commands.Bot(command_prefix=bot_prefix);

@bot.event
async def on_ready():
	print(" ")
	print("Bot çevrimiçi !")
	print("İsim : {}".format(bot.user.name))
	print(str(len(set(bot.get_all_members()))) + " tane kullanıcıya erişiyor !")

#mesaj silinince
@bot.event
async def on_message_delete(message):
    kim = message.author
    mesajicerik = message.content
    kanal = message.channel
    print("Silinen mesaj => "," Kanal : ",kanal,"// Kişi : ", kim,"// Mesaj : ",mesajicerik)
    await bot.process_commands(message)
    silinenMesaj = mesajicerik.lower()
    if silinenMesaj == "mal bot":
    	await message.channel.send("Hah şöyle, aferin")
@bot.event
async def on_message(message):
	if message.author != client.user:
		mesaj = message.content.lower()
		if mesaj == "sa":
			await message.channel.send("as")
		elif mesaj == "cs":
			await message.channel.send("@everyone Hadi seri cs !!!")
		elif mesaj == "!risk":
			await message.channel.send("@everyone Hadi seri risk")
		elif mesaj == "beyler":
			await message.channel.send("Buyur koçum")
		elif mesaj == "valorant":
			await message.channel.send("@everyone Hadi seri valorant !!!")
		elif mesaj == "anan" :
			await message.channel.send("Ayıp lan !");
		elif mesaj == "@everyone":
			await message.channel.send("Boş yere everyone atmayın lütfen")
		elif mesaj == "merhaba":
			await message.channel.send("Size de merhaba")
		elif mesaj == "mal bot":
			await message.channel.send("Ne dedin sen sil o mesajı hemen !")
		elif mesaj == "!say":
			for x in range(1,11):
				await message.channel.send(x)
		#internetten veri alanlar
		elif mesaj == "!korona" or mesaj == "!covid19":
			#korona
			saglik = requests.get('https://covid19.saglik.gov.tr/')
			soupC = BeautifulSoup(saglik.content,"html.parser")
			test= soupC.find("span",{"class":"buyuk-bilgi-l-sayi"})
			veriler= soupC.find_all("span",{"class":""})
			await message.channel.send("Bugünkü Test Sayısı: "+test.text)
			await message.channel.send("Bugünkü Vaka Sayısı: "+veriler[13].text)
			await message.channel.send("Bugünkü Vefat Sayısı: "+veriler[15].text)
			await message.channel.send("Bugünkü İyileşen Sayısı: "+veriler[17].text)
		elif mesaj == "!dolar":
			#dolar
			dolarKuru= requests.get('http://bigpara.hurriyet.com.tr/doviz/dolar/')
			soup = BeautifulSoup(dolarKuru.content,"html.parser")
			dolarFiyat = soup.find("span", {"class":"value up"})
			await message.channel.send("1 Dolar "+ dolarFiyat.text+" Tl")

bot.run('')   #Tırnak içine kendi tokenınızı yazınız. :)
