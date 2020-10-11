import os
from dotenv import load_dotenv

from discord import Activity, ActivityType, Embed
from discord.ext import commands

import requests

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DEEP_DREAM_KEY = os.getenv("DEEP_DREAM_KEY")

#init bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	#sanity/success check
	print(f'{bot.user.name} has connected')
	
	#set status message
	await bot.change_presence(activity=Activity(name="Making dogs look more doglike", type=ActivityType.competing))



@bot.command(name="dream", description="Runs the previous message through DeepDream")
async def dream(ctx):
	
	#get past 2 messages
	messages = await ctx.history(limit=2).flatten()
	attachments = messages[1].attachments
	
	#if no attachments, assume message is embed link to image
	if not attachments:
		image_url = messages[1].content
	#else the message is a file upload; get file url
	else:
		image_url = attachments[0].url
	
	#send request to deep dream api
	deep_dream_output = requests.post(
		"https://api.deepai.org/api/deepdream",
		data={
			'image': image_url,
		},
		headers={'api-key': DEEP_DREAM_KEY}
	).json()["output_url"]
	
	await ctx.send(deep_dream_output)





bot.run(DISCORD_TOKEN)
