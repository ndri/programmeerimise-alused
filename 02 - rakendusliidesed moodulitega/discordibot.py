import discord
from discord.ext import commands
import requests
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, "et_EE.UTF-8")

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command()
async def tere(ctx):
    await ctx.send("Sa oled tore inimene.")

    
@bot.command()
async def liida(ctx, vasak: int, parem: int):
    summa = vasak + parem
    await ctx.send(f"Summa on {summa}.")


@bot.command()
async def chucknorris(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random").json()
    await ctx.send(response["value"])

    
@bot.command()
async def nimepäev(ctx, nimi:str = ""):
    if not nimi:
        response = requests.get("https://api.abalin.net/today?country=ee").json()
        await ctx.send("Tänased nimepäevalised: " + response["data"]["namedays"]["ee"])
        return
    parameters = {
        "name": nimi,
        "country": "ee"
    }
    response = requests.get("https://api.abalin.net/getdate", params=parameters).json()
    dates = []
    for result in response["results"]:
        dates.append(date(month=result["month"], day=result["day"], year=date.today().year).strftime("%d. %B"))
    if not dates:
        await ctx.send("Ei ole nimepäeva :/")
    else:
        await ctx.send(", ".join(dates))


bot.run("sinutoken")
