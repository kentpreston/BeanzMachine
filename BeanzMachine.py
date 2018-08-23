# Beanz Machine
# A fun discord bot

import discord
import random

client = discord.Client()

with open('Insults', 'r') as insultsFile:
    insults = insultsFile.read().split("\n")

with open('greetings', 'r') as greetingsFile:
    greetings = greetingsFile.read().split("\n")

with open('songs', 'r') as songsFile:
    songs = songsFile.read().split("@")

with open('jokes', 'r') as jokesFile:
    jokes = jokesFile.read().split("@")

with open('youreWelcome', 'r') as welcomeFile:
    welcomes = welcomeFile.read().split("\n")

with open('goodnight', 'r') as goodnightFile:
    goodnights = goodnightFile.read().split("\n")

with open('validations', 'r') as validationFile:
    validations = validationFile.read().split("\n")

@client.event

async def on_message(input):
    # we do not want the bot to reply to itself
    if input.author == client.user:
        return

    # Only speak when spoken to
    if not ('beanzmachine' in input.content.lower() or "bmash" in input.content.lower()):
        return

    # Print input
    print("\n" + input.author.name + "\t\t:\t\"" + input.content + "\"")

    # Clean up input message
    message = input.content.lower().replace("beanzmachine", '').replace("bmash", '').replace("?", '')
    response = ''

    # Response to "help"
    if "!help" in message:
        with open('HelpMessage', 'r') as helpFile:
            helpText = helpFile.read()
        response += helpText

    # Response to "!advanced"
    if "!advanced" in message:
        with open('advancedHelp', 'r') as advancedFile:
            advancedText = advancedFile.read()
        response += advancedText

    if "!addinsult" in message:
        with open('Insults', 'a+') as insultsFile:
            insultsFile.write("\n" + message.replace(" !addinsult ", ''))
        response += ("Added \"" + message.replace(" !addinsult ", '') + "\" as an insult.\n").format(input)

    # Response to greetings
    if ("hello" in message) or ("hey" in message) or ("hi" in message):
        response += (greetings[random.randint(0,len(greetings) - 1)] + " {0.author.mention}\n").format(input)
        message = input.content.lower().replace("beanzmachine", '').replace("?", '').replace("hello", '').replace("hey", '').replace("hi", '')

    # Decision making: options must be separated by "or"
    if " or " in message:
        options = message.replace(" or ", ",").split(",")
        response += options[random.randint(0, len(options) - 1)].format(input) + "\n"

    # Song recommendation:
    if " song" in message:
        response += (songs[random.randint(0,len(songs) - 1)]).format(input) + "\n"

    if " joke" in message:
        response += (jokes[random.randint(0,len(jokes) - 1)]).format(input) + "\n"

    # Add song recommendation:
    if "!addsong" in message:
        with open('songs', 'a+') as songsFile:
            songsFile.write("\n@\n" + message.replace(" !addsong ", ''))
            songsFile.write("\nSubmitted by " + input.author.name)
        response += "Added song to list.\n"

    # Good bmash
    if message == "good ":
        response += "*Woof!*\n"

    # Bad bmash
    if message == "bad ":
        response += ":(\n"

    # Fuck you
    if "fuck you" in message:
        response += (insults[random.randint(0,len(insults) - 1)] + " {0.author.mention}").format(input) + "\n"

    # I love you
    if "i love you" in message:
        response += "I love you too,  {0.author.mention}\n".format(input)

    # Validation
    if "validate" in message:
        response += (validations[random.randint(0,len(validations) - 1)]).format(input) + "\n"

    # Thank you
    if ("thank you" in message) or ("thanks" in message):
        response += (welcomes[random.randint(0,len(welcomes) - 1)] + ", {0.author.mention}\n").format(input)

    if ("goodnight" in message) or ("gn" in message) or ("good night" in message):
        response += (goodnights[random.randint(0,len(goodnights) - 1)] + "!\n").format(input)

    # Send response if not empty
    if response != '':
        await client.send_message(input.channel, response)
        print("BeanzMachine\t:\t\"" + response + "\"\n")

@client.event

# Startup message
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDgxOTUyOTI2MzYxNzE0Njg4.Dl96gw.7xOWvrW3mZ5qFDBmVO6VYtT4_zE')
