
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('라프라프')
    await client.change_presence(status=discord.Status.online, activity=game)

#!dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('!dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id ==720927829193392189):
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="라프라프")
                        embed.add_field(name="Laf", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/9hBP7fP")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzM2NDEzMzYyOTI5NTMyOTMw.XxucYw.687eaW6-s8iO5wwTXwNFdV2aJvw')
