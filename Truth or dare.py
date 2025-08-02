import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# ------------------ Flask Web Server to Keep Alive ------------------
app = Flask('')

@app.route('/')
def home():
    return "Bot is online!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ------------------ Discord Bot Setup ------------------
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hi there! I’m alive.")

# ------------------ Start Web + Bot ------------------
keep_alive()
bot.run(os.getenv("TOKEN"))  # Set TOKEN as secret/env var
