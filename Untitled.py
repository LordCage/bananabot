#---
#
#
#
#
#---

# I m p o r t
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    #
    print('Logging Infomation')
    print('---------------')
    print('Bot:') 
    print(bot.user.name)
    #
    print('Bot ID:')
    print(bot.user.id)
    #
    print('Author:' + ' CookieKenneth') # Later on i'll remember the auth shit
    print('Author Discrim: 5996')         # Later on i'll remember the auth shit
    print('(c) 2018 CookieKenneth, LLC.')
    print('---------------')
    #
    #
        # This shit is clearly outdated. I believe you can't run this during a on_ready without a parm in ()
    #await change_presence(game=None, status=None)
    #await client.change_presence(game=discord.Game(name='bananahouse.org | .help'))
    #
    #

@bot.command()
async def info(info1):
    embed = discord.Embed(title="test", description="test", color=0xe9d770)
    
    # Author
    embed.add_field(name="Author", value="CookieKenneth#5996")
    
    # Server Count
    embed.add_field(name="Server count", value={len(bot.guilds)})

    # invite
    embed.add_field(name='Invite', value="https://discordapp.com/oauth2/authorize?client_id=482265626069434380&scope=bot")

    await info1.send(embed=embed)

@bot.command()
async def announcement(context):
    announcement_embed=discord.Embed(title="An Explaination ", url="https://www.reddit.com/r/BananaHouse/comments/9agpwi/an_explanation/", color=0xffff80)
    announcement_embed.set_author(name="CookieKenneth", icon_url="https://images-ext-1.discordapp.net/external/dbCNP6tfCdLMTBiEru1BTwuq3uaBXmSTotqEOHRCbcI/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/258049689608257538/e58084527f01814ccebecb8d0212e20c.png")
    announcement_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/453331979828592642/483471543167352843/rq36kl1xjxr01.png")
    announcement_embed.add_field(name='Infomation', value='Hello everyone, I made a reddit post describing the past events of our network and things that we failed to do with BananaHouse V1. Along with the real reason behind our closing. If you were a former staff or member we recommend you read this.', inline=False)
    announcement_embed.set_footer(text="©2018 BananaHouse, LLC. All rights reserved.")
    await context.send(embed=announcement_embed)
        #announcement_embed = discord.Embed(title=':page_facing_up: **An explanation.**', description='Announcement #2', thumbnail="https://cdn.discordapp.com/attachments/453331979828592642/483471543167352843/rq36kl1xjxr01.png", color=0xe9d770)
        #await ctx.send(embed=announcement_embed)   

@bot.command()
async def banana(banana_message):
        banana_embed=discord.Embed(title="Welcome to the BananaHouse Discord!", description="Welcome to our discord server. Please make yourself at home!", color=0xffff80)
        banana_embed.set_author(name="CookieKenneth", icon_url="https://images-ext-1.discordapp.net/external/dbCNP6tfCdLMTBiEru1BTwuq3uaBXmSTotqEOHRCbcI/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/258049689608257538/e58084527f01814ccebecb8d0212e20c.png")
        banana_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/453331979828592642/483044917241839616/Untitled.png")
        banana_embed.add_field(name='BananaHouse', value='BananaHouse is a discord server dedicated to our minecraft server, bananahouse.org and could be joined to play minigames and gamemodes like factions and skyblock with new and custom features that you have never seen before! If you dont play minecraft or do not play on our server you are still welcomed to enjoy our discord server and community! We welcome you and if you need anything we are happy to help you out.', inline=True)
        banana_embed.add_field(name='Invites', value='We offer discord invite rewards and will be offering different custom rewards from time to time. To learn more use the command .invites to learn how to start.', inline=True)
        banana_embed.add_field(name='Bots', value='BananaHouse has a lot of different bots to use to have fun, play music and do a lot of other cool tasks! Our custom bot BananaBot™ was created and improved by the original coder LordCage. These bots can be used in the commands channel and you can even sync your minecraft account and stats with the BananaBot™ sync feature in the sync channel. (Soon™) If you need help or would like to learn some of our bot commands use the command .help', inline=True)
        banana_embed.add_field(name='Staff', value='Were always looking for staff to join our team! If you have an interest in our server please use the command .apply to learn about what our server has to offer and if you fill out our application we will contact you with in a week. Asking staff to look at your application will result in an instant application denied state.', inline=True)
        banana_embed.add_field(name='Server IP', value='bananahouse.org', inline=True)
        banana_embed.set_footer(text="©2018 BananaHouse, LLC. All rights reserved.")
        await banana_message.send(embed=banana_embed)

#@bot.command()
#async def online(online_check):
#    await online_check.send(':white_check_mark: **BananaBot** is now Online and ready!')

#@bot.command()
#@checks.is_owner()
#async def shutdown(self):
#    pass
#    await bot.logout()
    #instance stays awake for 5mins?
    












bot.run('')
