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



rollyBot = commands.Bot(command_prefix='!',help_command=None)

@rollyBot.event
async def on_ready():
    print(f'{rollyBot.user.name} did the moon kick.')

# @rollyBot.event
# async def on_message(msg):



#check decorator confirming if user is registered
def isRegisteredUser():
    async def predicate(ctx):
        if(ctx.message.author.id not in userList):
            await ctx.send("You must register before rolling!\n" +
                            "Use the command: !register" )
        return ctx.message.author.id in userList
        # return ctx.message.author.id in userList
    # await ctx.send("greetings")
    return commands.check(predicate)


####
####
#### COMMANDS
####
####


# @rollyBot.command(name='help')
# async def helpList(ctx):
#     await ctx.send("Currently Supported Commands: !register,\n!single\n,!multi\n More Coming Soon...")

@rollyBot.command(name='help')
async def helpCommand(ctx):
    await ctx.send("There are currently no commands!")

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
@isRegisteredUser()
async def single_response(ctx,banner_type:str):

    await ctx.send(userList[ctx.message.author.id].roll(1))

@rollyBot.command(name='multi')
@isRegisteredUser()
async def multi_response(ctx,banner_type:str):
    
    await ctx.send(userList[ctx.message.author.id].roll(10))


rollyBot.run(TOKEN)
