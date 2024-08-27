import os
from discord.ext import commands
import music
from hoster import works

my_secret = os.environ['TOKEN']

cogs = [music]

client = commands.Bot(command_prefix = '$')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.lower() == '$credits':
    await message.channel.send('The genius that created me is called MrJackRegen. Kneel before thy god!')
  else:
    await client.process_commands(message)

  if message.content.lower() == '$gay':
    await message.channel.send('Hah! GAAAAAAYYYYY!')
  else:
    await client.process_commands(message)

for i in range(len(cogs)):
  cogs[i].setup(client)

works()
client.run(os.getenv('TOKEN'))