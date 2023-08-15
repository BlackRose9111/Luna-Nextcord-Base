import nextcord
from nextcord.ext import commands,tasks

from system.filemanager import filemanager

owner_ids = [240027656949596160, 1068287199688278166]
bot_name = "Luna"
bot = commands.AutoShardedBot(command_prefix="!",
                              strip_after_prefix=True,
                              case_insensitive=True,
                              intents=nextcord.Intents.all(),
                              owner_ids=owner_ids)


run_time = 0
TOKEN = ""

@bot.event
async def on_ready():
    print("Luna launched")


def database_connect():
    pass


def database_keepalive():
    pass


@tasks.loop(seconds=1)
def parallel_loop():
    global run_time
    run_time += 1
    database_keepalive()

def get_token():
    global TOKEN
    try:
        TOKEN = filemanager.get_value_from_json()
    except:
        TOKEN = None

    if TOKEN is None:
        while True:
            a = input("Bot Token was not found, please enter it by hand:")
            if a is not None and a != "":
                TOKEN = a
                break

def load_module(modulename):
    pass

