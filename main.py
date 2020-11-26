#main.py

from bannerClass import wanderLustInvocationBanner as wlib

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("SECRET_TOKEN")

#currently used to maintain userData
userList = {}



rollyBot = commands.Bot(command_prefix='!')

@rollyBot.event
async def on_ready():
    print(f'{rollyBot.user.name} did the moon kick.')

# @rollyBot.event
# async def on_message(msg):



#check decorator confirming if user is registered
async def isRegisteredUser(ctx):
    if(ctx.message.author.id not in userList):
        await ctx.send("You must register before rolling!\n" +
                        "Use the command: !register" )
    return ctx.message.author.id in userList

#check banner type and send error string if invalid
async def checkBannerType(ctx,banner_type:str):
        if banner_type is None:
            await ctx.send("Please enter a banner name")
            return False

        elif banner_type != 'valid':#compares banner_type string to list of valid banner strings
            await ctx.send("Banner name invalid")
            return False

        else:
            return True

####
####
#### COMMANDS
####
####



@rollyBot.command(name='register')
async def registerUser(ctx):
    #initializes user data with banner objects
    await ctx.send(f"Registering User {ctx.message.author.name}..")

    #TODO
    userList[ctx.message.author.id] = wlib.wanderLustInvocationBanner()#class that encapsulates all banners
    # await ctx.send(f"List of Current Users: {userList}")

    await ctx.send(f"{ctx.message.author.name} can now go broke!")
    # await ctx.send(f"User ID: {ctx.message.author.id}")
    

@rollyBot.command(name='single')
async def single_response(ctx,banner_type:str=None):
    if  await isRegisteredUser(ctx):
        if await checkBannerType(ctx,banner_type):
            await ctx.send(userList[ctx.message.author.id].roll(1))





    

@rollyBot.command(name='multi')
async def multi_response(ctx,banner_type:str=None):
    if await isRegisteredUser(ctx):
        if await checkBannerType(ctx,banner_type):
            await ctx.send(userList[ctx.message.author.id].roll(10))



rollyBot.run(TOKEN)
