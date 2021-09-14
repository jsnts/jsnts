# How2ITC_bot.py

# libreria para conectar el programa con discord
import discord

# para poder usar los comandos
from discord.ext import commands

# el token de nuestro bot. DIFERENTE PARA CADA PERSONA
TOKEN = 'ODg2Mzg2MDQ3OTcyNDI5ODU1.YT01Vg.shB0MRKrb-d7SqB-_qRZnSoGRK8'
GUILD = 'chivas-zambettifanclub'

# aqui es como queremos usar nuestros comandos
bot = commands.Bot(command_prefix='!')

class MyMusicBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
    
    async def on_ready(self):
        print("Bot is ready")

    async def on_message(self, message):
        





#aqui comprobamos si ya se conecto o no
@bot.event
async def on_ready():
    guild = guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
        )

# funcion para contestar mensajes
@bot.event
async def on_message(message):

    # checa si el mensaje es de otro ususario, no de el mismo
    if message.author == bot.user:
        return

    # depende de que le mandemos es la respuesta que nos da
    if message.content == 'Hola':
        response = 'Hola buenos dias.'
        await message.channel.send(response)

    elif message.content == 'Que tranza carnal':
        response = 'Como andamios'
        await message.channel.send(response)

    elif message.content == 'Qui hubo mirrey':
            response = 'Que pasa paps'
            await message.channel.send(response)

    await bot.process_commands(message)

@bot.command()
async def play(ctx, url : str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="el_criko_lobby")
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await voiceChannel.connect()

@bot.colmmand()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
    
@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")
    

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()



@bot.command(name="canal")
async def canal(ctx, nombre):

    await ctx.guild.create_text_channel(nombre)

 

bot.run(TOKEN) 