# bot.py
import os
import random
import discord
import time
import math
import asyncio
import praw
from dotenv import load_dotenv


# Main Setups
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Praw Setups
reddit = praw.Reddit(
    client_id="XUcJ3ZXe2GothVnmrWBmdw",
    client_secret="ZOLEtzMlgulhWIb7aTcFqzxW4J4qVQ",
    user_agent="discord.com:AndrewMamBot:v0.0.1 (by u/wistful02)",
    username="wistful02",
    password="sun02252004",
    check_for_async=False
)
print("Reddit read only: " + str(bool(reddit.read_only)))
print("Reddit account connected: " + str(reddit.user.me()))

# Other Setups
PATH = r"C:\Users\Zavier\Documents\codes\python\discordBot\storage.txt"

# Bot Setup
intents = discord.Intents.default()
intents.members = True
help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = commands.Bot(command_prefix='!a ', intents=intents, help_command = help_command)


# Commands
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user.name} has connected to Discord!')
    async for member in guild.fetch_members(limit=40):
        print(member.name,end=',')
    print()
    await bot.change_presence(activity=discord.Game(name=" with local boys 24/7! Use !a to join <3."),status = discord.Status.online)

@bot.event
async def on_message(message):
    if(message.author==bot.user):
        return
    if len(message.clean_content) > 100:
        channel = message.channel
        await channel.send('Blog it')
    else:
        await bot.process_commands(message)

@bot.event
async def on_message(message):
    if(message.author==bot.user):
        return
    if(random.randint(1,10)==1):
        await message.channel.send("Damn daddy ur words just made me horny \n*moans*")
        await bot.process_commands(message)
    else:
        await bot.process_commands(message)

@bot.command(name='sex',help='Simulates sex with Andrew mama')
async def sexCom(ctx):
    if str(ctx.channel) == "nsfw":
        responce = "Penetrate me daddy <3"
        await ctx.send(responce)
        await asyncio.sleep(5)
        await ctx.send("*Andrew mama cums*")
    else:
        guild = discord.utils.get(bot.guilds, name=GUILD)
        channel = discord.utils.get(guild.channels, name="nsfw") 
        await ctx.send("We can't do it here daddy <@"+str(ctx.message.author.id)+">, take me to somewhere private <3.")
        await ctx.send(f"Like <#{channel.id}>",delete_after=3.0)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    await ctx.send("Andrew Mama rolls a dice....")
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='fuck',help='says fuck you to someone,toUse:[!a fuck @user]')
async def fuckSomeone(ctx,fuckedUser):
    await ctx.send('fuck you '+fuckedUser)

@bot.command(name='fuckAndrewMama',help='fucks Andrew mama,toUse:[!a fuckAndrewMama]')
async def fuckAndrewMama(ctx):
    with open(PATH,'r') as file:
        data=file.readlines()

    amft=int(data[1])
    amft+=1
    await ctx.send('<@'+ str(ctx.message.author.id) + "> has fucked Andrew Mama! "+ "\nShe has been fucked a total of " + str(amft) + " times!")
    data[1]=str(amft)

    with open(PATH, 'w') as file:
        file.writelines(data)

@bot.command(name='donBai',help='deep roasts whatever user u choose,toUse[!a donBai @User]')
async def donBaiRap(ctx,target):
    if not "cringe" in [y.name.lower() for y in ctx.author.roles]:
        await ctx.send("你看你前面那秃噜操你妈的老铁们我们一起举报他。噔噔噔噔，"\
            +target+"傻逼操你妈，你妈大逼人人插。左插插他么右插插，插的你妈逼开花。你妈大逼血又血，"\
            "操你妈了个逼拉耶。你妈大逼串肉串，操你妈了个逼来贩。整形师我来操你妈，你妈大逼人人插，" \
            "叉的你妈直开花我操你妈来我操你妈。啊对面下播了，狗鸡巴不是你跟我俩装逼操")
        await ctx.message.delete()
    else:
        toDelete = await ctx.send("Sorry but u are cringe so u cannot use this command.",delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()

@bot.command(name='threeYearStory',help='tells a great tale of CCP')
async def threeYearStory(ctx):
    with open(r"C:\Users\Zavier\Documents\codes\python\discordBot\threeYearBigEat.txt",encoding="utf-8")as file:
        data=file.read()
    await ctx.send(data)

@bot.command(name='guessGame',help="Plays a guess game with Andrew Mama.")
async def guessGame(ctx):
    await ctx.send("Guess how many times Andrew mama got fucked last night? (guess 1~100)")
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel  
    
    msg = await bot.wait_for("message", check=check)
    if int(msg.content)<=100 and int(msg.content) >0:
        ans = random.randint(1, 100)
        if ans == int(msg.content):
            await ctx.send('Amazing guess!That is correct!!! <3')
        else:
            await ctx.send('Oopsie! Wrong guess. I actually had sex ' + str(ans) + ' times last night!')
    else:
        await ctx.send("invalid input!")

@bot.command(name="getReddit",help='Randomly gets one of the top 20 hottest posts in the subreddit specified.toUse[!a getReddit {subreddit}]')
async def getReddit(ctx,whatSub):
    try:
        submissions = reddit.subreddit(str(whatSub)).hot()
        post=random.randint(1,20)
        for i in range(0,post):
            getSub=next(x for x in submissions if not x.stickied)

        await ctx.send(getSub.url)
    except Exception as e:
        if str(e) == "Redirect to /subreddits/search":
            await ctx.send("That is not an existing subreddit")
        else:
            print(e)

@bot.command(name="getMaoQuote",help="Gives u a random quote from out great leader Mao")
async def getMaoQuote(ctx):
    with open(r"C:\Users\Zavier\Documents\codes\python\discordBot\ZedongQuotes.txt",'r',encoding="utf-8") as file:
        data=file.readlines()
    data = [ele for ele in data if ele.strip()]
    await ctx.send("Some wise words from our leader in heart: \n" + str(random.choice(data)))

@bot.command(name="nsfw",pass_context=True,help="Gives or removes NSFW role. toUse[!a nsfw (on/off)]")
async def addrole(ctx,turnOn):
    if not "cringe" in [y.name.lower() for y in ctx.author.roles]:
        if turnOn == "on":
            user = ctx.message.author
            memberRole = discord.utils.get(ctx.guild.roles, name='NSFW')
            await user.add_roles(memberRole)
            await ctx.send("NSFW role has been added to "+"<@"+str(ctx.message.author.id)+">")
        elif turnOn == "off":
            user = ctx.message.author
            memberRole = discord.utils.get(ctx.guild.roles, name='NSFW')
            await user.remove_roles(memberRole)
            await ctx.send("NSFW role has been removed from "+"<@"+str(ctx.message.author.id)+">")
    else:
        await ctx.send("U do not have the perms to access this command, daddy " + "<@" + str(ctx.message.author.id) + ">, possibly because ur cringe :(")

#errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command daddy <3.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('There is no such command baby <3, pls try again daddy :)')
    else:
        raise error


bot.run(TOKEN)