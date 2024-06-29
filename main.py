import discord
from discord.ext import commands
from bot_mantik import gen_pass

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

bot.run("TOKEN")