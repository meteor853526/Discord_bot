import discord
from discord.ext import commands

# 同樣繼承bot的屬性
class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

