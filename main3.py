from discord.ext import commands
import discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents= intents)
@bot.event
async def on_ready():
    print (f'Tu bot {bot.user} esta en linea')
@bot.command()
async def manualidad(ctx, material: str = ""):
    material = material.lower().strip()
    
    # Diccionario con enlaces funcionales a tutoriales en YouTube
    ideas = {
        "rollo": (
            "**ManualitOzo: Cohete Espacial**\n"
            "Pinta el rollo, coloca un cono de papel arriba y papel de colores abajo.\n\n"
            "**Ver Tutorial en Video:** https://youtu.be/fgw22hRwqB4?si=FgEBPfCN60ipG_Sh"
        ),
        "botella": (
            "**ManualitOzo: Cerdito Alcancia**\n"
            "Haz una ranura arriba, forrala de color y coloca 4 tapas como patas.\n\n"
            "**Ver Tutorial en Video:** https://youtu.be/HF6MNAQXets?si=Ig1uGEIaXEsOJMtv"
        ),
        "carton": (
            "**ManualitOzo: Teatrito de Sombras**\n"
            "Recorta el centro de la caja, pega papel blanco y proyecta luz desde atras.\n\n"
            "**Ver Tutorial en Video:** https://youtu.be/eIIKqTGAJtY?si=KEYf-578E2ZMHMAF"
        )
    }
    
    if material in ideas:
        await ctx.send(ideas[material])
    else:
        await ctx.send("Hola creador. Elige un material para ver su manualidad y enlace:\nUsa: `-manualidad rollo`, `-manualidad botella` o `-manualidad carton`")
token = ""
bot.run(token)