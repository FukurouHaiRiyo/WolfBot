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
async def check_age(ctx, user:discord.User):
	#get the current time
	now = datetime.now()

	#get the user's account creation date
	user_created = user.created_at

	#get the difference between the two dates
	difference = now - user_created

	#get the difference in days
	days = difference.days

	#send the message
	return await ctx.send(f"@{user} is {days} days old.")

@bot.command()
async def whoareyou(ctx):
	return await ctx.send("My name is Blade Wolf, or simply Wolf, officially designated IF Prototype LQ-84i. I was designated to check the creation date of a discord account. To get started type ```!com``` to see my commands")

@bot.command()
async def com(ctx):
	return await ctx.send("I'm a bot that can check your discord account age. Type ```!check_age <user_id>``` or ```!check_age <@username#1234>``` to check the age of the user's discord account.")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("BOT_TOKEN")