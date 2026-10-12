from discord.ext import commands
import discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents= intents)
@bot.event
async def on_ready():
    print (f'Tu bot {bot.user} esta en linea')
@bot.command()
async def reciclar(ctx, residuo: str = ""):
    residuo = residuo.lower().strip()
    if residuo == "papel":
        await ctx.send("El papel se recicla en el contenedor azul.")
    elif residuo == "plastico":
        await ctx.send("El plástico se recicla en el contenedor amarillo.")
    elif residuo == "vidrio":
        await ctx.send("El vidrio se recicla en el contenedor verde.")
    elif residuo == "organico":
        await ctx.send("Los residuos orgánicos se reciclan en el contenedor marrón.")
    elif residuo == "metal":
        await ctx.send("El metal se recicla en el contenedor gris.")
    else:
        await ctx.send("No reconozco ese tipo de residuo. Por favor, ingresa uno de los siguientes: papel, plastico, vidrio, organico, metal.")

token = ""
bot.run(token)