#main.py

from bannerClass import wanderLustInvocationBanner as wlib

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
    test = wlib.wanderLustInvocationBanner()

    await ctx.send(test.roll(1))

@rollyBot.command(name='multi')
async def multi_response(ctx,banner_type:str):
    test = wlib.wanderLustInvocationBanner()
    await ctx.send(test.roll(10))

@rollyBot.command(name='roll')
async def on_message(ctx, banner_type: str):
    pass
    # # sim = roll.Simulator()
    # # sim.single_summoning(banner_type)
    # test = BaseBanner()
    # newList = test.genProbabilityRange(5,3,1)
    # # print(len(newList))
    # print(test.genRandomNumber(newList))
    # await ctx.send(newList)
    

rollyBot.run(TOKEN)
