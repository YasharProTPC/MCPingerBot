import discord
from discord.ext import commands, tasks
from os import system, remove
from mcsrvstat import Stats, ServerPlatform
import qrcode
from random import randrange
PREFIX = "8"
TOKEN = ""

def main():
    client = commands.Bot(command_prefix=PREFIX, case_insensitive=True)


    @client.event
    async def on_ready():
        system("cls")
        print("Connected Successfull " + client.user.name+"#"+client.user.discriminator)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="& Prefix"))

    @client.command()
    async def status(ctx, *, argv=None):
        if argv == None:
            await ctx.channel.send("<:no_entry_sign:945297274844626994> Please Enter IP On Next Arg")
        else:
            server = Stats(platform=ServerPlatform.java, ip_address=argv)
            name = argv.replace('play.', '').replace('mc.', '').replace('oyna.', '').replace('hub.', '').replace('.ir', '').replace('.com', '').replace('.io', '').replace('es.', '').replace('.es', '').replace('.net', '').replace('.game', '').replace('.tr', '').replace('join.', '').replace('.network.', '').replace('.', '')
            if await server.check_if_online():
                print(f"Server : {argv}")
                players = await server.get_player_count()
                online = f"{players.online}/{players.max}"
                embedvar = discord.Embed(title="", description="", color=0x00ff00)
                embedvar.set_image(url=f"http://status.mclive.eu/{name.title()}/{argv.title()}/25565/banner.png")
                embedvar.set_thumbnail(url=f"https://eu.mc-api.net/v3/server/favicon/{argv}")
                embedvar.set_author(name="TrackerBot", icon_url="https://cdn.discordapp.com/attachments/943906561699504179/945314960370728970/logo.png")
                embedvar.add_field(name="**<:map:944637428658995221> Address **»", value=f"{argv.title()} - 25565", inline=False)
                embedvar.add_field(name="**<:people_hugging:944637570833326110> Players **»", value=online, inline=True)
    
                await ctx.channel.send(ctx.message.author.mention, embed=embedvar)
            else:
                offlineEmbed = discord.Embed(title="", description="", color=0xfc0303)
                offlineEmbed.set_image(url=f"http://status.mclive.eu/{name.title()}/{argv.title()}/25565/banner.png")
                offlineEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/943906561699504179/945314952120500274/offline.png")
                offlineEmbed.set_author(name="TrackerBot", icon_url="https://cdn.discordapp.com/attachments/943906561699504179/945314960370728970/logo.png")
                offlineEmbed.add_field(name="**<:map:944637428658995221> Address **»", value=f"{argv.title()} - 25565", inline=False)
                offlineEmbed.add_field(name="**<:people_hugging:944637570833326110> Players **»", value="<:no_entry_sign:945297274844626994> Offline", inline=True)
                offlineEmbed.add_field(name="**<:people_hugging:944637570833326110> Software **»", value="<:no_entry_sign:945297274844626994> Offline", inline=True)
                await ctx.channel.send(ctx.message.author.mention, embed=offlineEmbed)
    @client.command()
    async def qrcode(ctx, *, argv=None):
        if argv==None:
            await ctx.channel.send("")
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
if __name__ == "__main__":
    main()
