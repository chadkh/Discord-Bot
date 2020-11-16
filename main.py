#main.py

from bannerClass.BaseBanner import BaseBanner

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("SECRET_TOKEN")

rollyBot = commands.Bot(command_prefix='!')

@rollyBot.event
async def on_ready():
    print(f'{rollyBot.user.name} has connected to Discord!')


@rollyBot.command(name='single')
async def single_response(ctx,banner_type:str):
    pass

@rollyBot.command(name='multi')
async def multi_response(ctx,banner_type:str):
    pass

@rollyBot.command(name='roll')
async def on_message(ctx, banner_type: str):
    # sim = roll.Simulator()
    # sim.single_summoning(banner_type)
    test = BaseBanner()
    newList = test.genProbabilityRange(5,3,1)
    # print(len(newList))
    print(test.genRandomNumber(newList))
    await ctx.send(newList)
    

rollyBot.run(TOKEN)
