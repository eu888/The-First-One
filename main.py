import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

GUILD_ID = 881250112549027880  

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    guild = discord.Object(id=GUILD_ID)
    await tree.sync(guild=guild)
    print(f"Synced slash commands to guild {GUILD_ID}")

    activity = discord.Game(name="Made by Me88_88")
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@tree.command(name="ping",
              description="Replies with pong.",
             )
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


@tree.command(name="roll",
              description="Roll a die",
              )
async def roll(interaction: discord.Interaction, sides: int):
    import random
    result = random.randint(1, sides)
    await interaction.response.send_message(
        f"You rolled a {result} on a {sides}-sided die.")


@tree.command(name="uptime",
              description="Shows when bot joined this server",
              )
async def uptime(interaction: discord.Interaction):
    joined = interaction.guild.me.joined_at
    await interaction.response.send_message(
        f"I've been up since {joined.strftime('%Y-%m-%d %H:%M:%S')}")


@tree.command(name="test",description="Test command with arguments")
async def test(interaction: discord.Interaction, arg1: str, arg2: str = None):
    if arg2:
        await interaction.response.send_message(
            f"Received arguments: {arg1}, {arg2}")
    else:
        await interaction.response.send_message(f"Received argument: {arg1}")

@tree.command(name="help", description="Show available commands and what they do.")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🤖 A Normal Bot — Help",
        description="Here are the available commands:",
        color=discord.Color.blue()
    )
    embed.add_field(name="/ping", value="Check the bot's latency.", inline=False)
    embed.add_field(name="/roll [sides]", value="Roll a die with `[sides]` sides.", inline=False)
    embed.add_field(name="/uptime", value="Shows how long the bot has been running.", inline=False)
    embed.add_field(name="/test [arg1] [arg2]", value="Returns your input to test argument parsing.", inline=False)
    embed.add_field(name="/help", value="Display this help message.", inline=False)
    await interaction.response.send_message(embed=embed)

keep_alive()

bot.run(os.environ.get("DISCORD_BOT_SECRET"))
