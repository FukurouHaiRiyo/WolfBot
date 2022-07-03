import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

#GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	#CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED 
      # WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send('My name is Blade Wolf, or simply Wolf, officially designated IF Prototype LQ-84i. You\'ll be checked in shortly.')
	
	return await bot.process_commands(message)

bot = commands.Bot(command_prefix='!')

@bot.command()
@bot.command()
async def check_age(ctx, user:discord.User):
	#get the current time
	now = datetime.now()

	#get the user's account creation date
	user_created = user.created_at

	#get the difference between the two dates
	difference = now - user_created

	#get the difference in years if days > 365
	if difference.days > 365:
		years = int(difference.days / 365)
		await ctx.send(f'{user.name}s account is {years} year(s) old.')
	#get the difference in months if days > 30
	elif difference.days > 30:
		months = int(difference.days / 30)
		await ctx.send(f'{user.name}s account is {months} month(s) old.')
	#get the difference in days if days > 0
	elif difference.days > 0:
		days = int(difference.days)
		await ctx.send(f'{user.name}s account is {days} day(s) old.')
	#get the difference in hours if days < 1
	elif difference.seconds / 3600 > 0:
		hours = int(difference.seconds / 3600)
		await ctx.send(f'{user.name}s account is {hours} hour(s) old.')
	#get the difference in minutes if days < 1
	elif difference.seconds / 60 > 0:
		minutes = int(difference.seconds / 60)
		await ctx.send(f'{user.name}s account is {minutes} minute(s) old.')
	#get the difference in seconds if days < 1
	else:
		seconds = int(difference.seconds)
		await ctx.send(f'{user.name}s account is {seconds} second(s) old.')

		
@bot.command()
async def day_of_creation(ctx, user: discord.User):
	#check the date and the hour of creation of the user
	user_created = user.created_at
	return await ctx.send(f'{user.name} created their account on {user_created.day}/{user_created.month}/{user_created.year} at {user_created.hour}:{user_created.minute}:{user_created.second}.')


@bot.command()
async def whoareyou(ctx):
	return await ctx.send("My name is Blade Wolf, or simply Wolf, officially designated IF Prototype LQ-84i. I was designated to check the creation date of a discord account. To get started type ```!com``` to see my commands")

@bot.command()
async def com(ctx):
	return await ctx.send("I'm a bot that can check your discord account age. Type ```!check_age <user_id>``` or ```!check_age <@username#1234>``` to check the age of the user's discord account.")

#checks if a link it's safe or not by using ipqualityscore api's (found here https://ipqualityscore.com) 
@bot.event
async def on_message(message):
	url = message.content
	api_url = 'https://ipqualityscore.com/api/json/url/your_token/'

	encoded_url = urllib.parse.quote(url, safe='')
	data = requests.get(api_url + encoded_url)

	with open('file.json', 'w') as f:
		f.write(json.dumps(data.json(), indent=4))

	with open('file.json', 'r') as f:
		Dict = json.load(f)
		msg = '** **'

		#print(Dict['message'])
		
		if Dict['message'] == 'Success.':
			if Dict['suspicious'] == True:
				channel = bot.get_channel('channel_id')
				msg = 'Suspicious link'
				return await channel.send(msg)
			elif Dict['suspicious'] == False:
				channel = bot.get_channel('channel_id')
				msg = 'Safe link'
				return await channel.send(msg)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("BOT_TOKEN")
