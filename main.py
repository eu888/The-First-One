import os
import discord
from discord.ext import commands
from keep_alive import keep_alive  # Make sure keep_alive.py exists

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    activity = discord.Game(name="Made by Me88_88", type=1)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("pong")

@bot.command(name='roll')
async def roll(ctx, num: int):
    await ctx.send(f"Rolls a {num}-sided die {num} times")

@bot.command(name='uptime')
async def uptime(ctx):
    await ctx.send(f"I've been up since {ctx.guild.me.joined_at.strftime('%Y-%m-%d')}")

@bot.command(name='test')
async def test(ctx, *args):
    await ctx.send(f'{len(args)} arguments: {", ".join(args)}')

extensions = [
    'cogs.cog_example'
]

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

    keep_alive()  # Starts the Flask web server
    bot.run(os.environ.get("DISCORD_BOT_SECRET"))
