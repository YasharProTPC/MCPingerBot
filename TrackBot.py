import discord
from discord.ext import commands, tasks
from os import system, remove, name
import qrcode
from random import randrange
import json, requests 


if __name__ == "__main__":
    try:
        TOKEN = ""
        PREFIX = ",,"

        client = commands.Bot(command_prefix=PREFIX, case_insensitive=True)
        client.remove_command('help')

        @client.event
        async def on_ready():
            system("cls" if name == "nt" else "clear")
            print("Connected Successfull " + client.user.name+"#"+client.user.discriminator)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{PREFIX} Prefix"))

        @client.command()
        async def status(ctx, argv=None, port=25565):
            if argv == None:
                await ctx.channel.send("<:no_entry_sign:945297274844626994> Please Enter IP On Next Arg")
            else:
                url = requests.get(f"https://mcapi.us/server/status?ip={argv}&port={port}")
                text = url.text
                data = json.loads(text)
                if data['online'] == True:
                    print(f"{data['players']['now']}/{data['players']['max']}")
                    ar = argv.lower()
                    name = ar.replace('play.', '').replace('mc.', '').replace('oyna.', '').replace('hub.', '').replace('.ir', '').replace('.com', '').replace('.io', '').replace('es.', '').replace('.es', '').replace('.net', '').replace('.game', '').replace('.tr', '').replace('join.', '').replace('.network.', '').replace('.', '')
                    
                    print(f"Server : {argv}")
                    embedvar = discord.Embed(title="", description="", color=randrange(0xffffff))
                    embedvar.set_image(url=f"http://status.mclive.eu/{name.title()}/{argv.title()}/25565/banner.png")
                    embedvar.set_thumbnail(url=f"https://eu.mc-api.net/v3/server/favicon/{argv}")
                    embedvar.set_author(name="TrackerBot", icon_url="https://cdn.discordapp.com/attachments/943906561699504179/945314960370728970/logo.png")
                    embedvar.add_field(name="**<:map:944637428658995221> Address **»", value=f"{argv.title()} - {port}", inline=False)
                    embedvar.add_field(name="**<:people_hugging:944637570833326110> Players **»", value=f"{data['players']['now']}/{data['players']['max']}", inline=False)

                    await ctx.channel.send(ctx.message.author.mention, embed=embedvar)
                else:
                    offlineEmbed = discord.Embed(title="", description="", color=(0xffffff))
                    offlineEmbed.set_image(url=f"http://status.mclive.eu/{name.title()}/{argv.title()}/25565/banner.png")
                    offlineEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/943906561699504179/945314952120500274/offline.png")
                    offlineEmbed.set_author(name="TrackerBot", icon_url="https://cdn.discordapp.com/attachments/943906561699504179/945314960370728970/logo.png")
                    offlineEmbed.add_field(name="**<:map:944637428658995221> Address **»", value=f"{argv.title()} - {port}", inline=False)
                    offlineEmbed.add_field(name="**<:people_hugging:944637570833326110> Players **»", value="<:no_entry_sign:945297274844626994> Offline", inline=True)
                    offlineEmbed.add_field(name="**<:ringed_planet:945415491508379699> Ping **»", value="<:no_entry_sign:945297274844626994> Offline", inline=False)
                    await ctx.channel.send(ctx.message.author.mention, embed=offlineEmbed)
        @client.command()
        async def qrcode(ctx, *, argv=None):
            if argv==None:
                await ctx.channel.send("<:no_entry_sign:945297274844626994> Please Enter Web Address On Next Arg")
            else:
                if "https://" in argv:
                    filename = randrange(100000, 9999999)
                    print(filename)
                    system(f'qr "{argv}" > {filename}.png')
                    file = discord.File(f"{filename}.png", filename=f"{filename}.png")

                    qrembed = discord.Embed(title="", description=f"Your QR Code For **{argv}**", color=0xfc0303)
                    qrembed.set_image(url=f"attachment://{filename}.png")
                    await ctx.channel.send(ctx.message.author.mention, file = file, embed=qrembed)
                    remove(f"{filename}.png")
                else:
                    ctx.channel.send("<:no_entry_sign:945297274844626994> Please Write ( Link ) Of Your Website! https://")
        client.run(TOKEN)
    except Exception as e:
        print(e)

        
