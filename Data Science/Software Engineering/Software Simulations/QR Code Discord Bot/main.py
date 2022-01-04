import discord 
from discord.ext import commands 
import pyqrcode 

client = commands.Bot(command_prefix='!')

@client.command(pass_context=True)
async def test(ctx, member):
    message = message.content 
    await ctx.send(file=discord.File('code.png'))

    link = pyqrcode.create(message)

    link.png('code.png', scale=10)

client.run('')
