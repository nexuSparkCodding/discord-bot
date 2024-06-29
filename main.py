import discord
from discord.ext import commands
from bot_mantik import gen_pass
import random, os

# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
bot= commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı')

@bot.command()
async def merhaba(ctx):
    await ctx.send("Merhaba seni burada görmek çok güzel!")
    
@bot.command()
async def gorusuruz(ctx):
    await ctx.send("Görüşürüz, seni burada tekrar görmek dileğiyle!")

@bot.command()
async def sifre(ctx):
    await ctx.send("Şifreniz: " + gen_pass(10))

@bot.command()
async def kurallar(ctx):
    with open("metinler/metin.txt", 'r', encoding='utf-8') as dosya:
        a = dosya.read()
    await ctx.send(a)
    
@bot.command()
async def mem(ctx):
    '''
    Dosya Açmak İçin Gerekli Olan Komut => open()
    open() İçerisine birden fazla argman kabül eder.
    1. Argüman => Hangi dosyayı açmak istiyorsanız o dosyanın yolu. Bunu yazarken string veri türünü kullan. 
    2. Argüman => Bu metin/metin olmayan dosyayı açmak istiyorsanız tanımlanan dosya açma kiplerini/modlarını kullanın.
                  --------------------- Dosya Açma Modları--------------------  
                  1 => Okuma Modu (Metin olmayan dosyaları) => Read (Okumak) --> 'rb'
                  2 => Yazma Modu (Metin olmayan dosyalar) => Write (Yazmak) --> 'wb'
    '''
    liste =  os.listdir('resimler')
    resim_adi = random.choice(liste)
    
    with open(f"resimler/{resim_adi}", 'rb') as resim:
        gorsel = discord.File(resim)
    await ctx.send(file=gorsel)
        

bot.run("TOKEN")