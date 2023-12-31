import discord
from discord.ext import commands

# Create a bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, world!')

# Run the bot
bot.run('YOUR_BOT_TOKEN')
