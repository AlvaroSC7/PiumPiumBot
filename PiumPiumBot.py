import discord
from discord.ext import commands
from os.path import dirname, abspath

def get_bot_token():
    """
    Get Discord bot token to be used in any request. It must be stored in PiumPiumToken.txt

    Parameters:
        void

    Returns:
        Response: Bot token.
    """
    ws_path = dirname(abspath(__file__))
    path = ws_path + "/PiumPiumToken.txt"
    tokenFile = open(path,"r")
    token = tokenFile.read()
    return token

intents = discord.Intents.all()
#bot = EasyBot(intents= intents)
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.command(name='suma')
async def sumar(ctx, num1, num2):
    response = int(num1) + int(num2)
    await ctx.send(response)

def main():
    token = get_bot_token()
    bot.run(token)

if __name__ == "__main__":
    main()