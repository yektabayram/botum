import discord
from discord.ext import commands
import os
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx,count_heh=5):
   await ctx.send("he"*count_heh) 

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)  

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def mem(ctx):
    resim = random.choice(os.listdir('images'))
    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
    with open(f'images/{resim}', 'rb') as f:
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

oneriler=["plastik atıklarınızla el işi yapın","tekrar poşetleri kullanabilirsiniz","pilleria atık kutusuna atabiliriz"]

@bot.command()
async def atik(ctx):
    sonuc=random.choice(oneriler)
    await ctx.send(sonuc)

@bot.command()
async def afis(ctx):
    afis = random.choice(os.listdir('afisler'))
    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
    with open(f'afisler/{afis}', 'rb') as f:
        afis_ = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=afis_)

bot.run("TOKEN")
