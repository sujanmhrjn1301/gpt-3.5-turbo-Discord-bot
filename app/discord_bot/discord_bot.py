import discord
from openai import OpenAI
import os
from dotenv import load_dotenv
from discord.ext import tasks
from app.openai_api.openai_api import Bll

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):
    async def on_ready(self):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= "with you"))
        print(f"{bot.user} is now ready to respond! ")

    async def on_guild_join(self,guild):
        channel= guild.system_channel
        if channel:
            await channel.send(f"https://tenor.com/view/entrance-confident-im-here-woody-toy-story-gif-11881136")
    
    async def on_message(self,message):
        if message.author== bot.user:
            return
        
        content= message.content.lower()
        words=["/helpme","/ask","/describe"]
        img_cmds=["/make","/create","/generate"]  

        try:
            if (bot.user.mentioned_in(message) and content) or any(word in content for word in words):
                print(f"{message.author.name} searched for: {content}")
                await message.channel.send("Thinking...")
                AI_Response =  Bll.openAI_response(content)
                await message.channel.send(AI_Response)
            else:
                pass
        except Exception as  e:
            print(e)
            await message.channel.send(f"An Error has Occurred: {e}")
        
        if message.content in content:
            try:
                if any(word in content for word in img_cmds):
                    await message.channel.send("Processing. Please wait few seconds...")
                    print(f"{message.author.name} searched for: {content}")
                    AI_Img_Response  = Bll.openAI_image(content)
                    print(AI_Img_Response)
                    await message.channel.send(AI_Img_Response)
        
            except Exception as e:
                await message.channel.send(f"An Error has Occurred: {e}")
                print(e)
       
bot= MyClient(intents=intents)