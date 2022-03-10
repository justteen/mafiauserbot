
# Thanks to @D3_krish
# Porting in MafiaBot by @H1M4N5HU0P

import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/5599bdacfbd38a8790a99.png"
pm_caption = "  __**▁ ▂ ▄ ▅ ▆ ▇ █BUZZ MAFIA IS ALIVE█ ▇ ▆ ▅ ▄ ▂ ▁**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 👑𝐌𝐀𝐒𝐓𝐄𝐑👑\n  **『😈[{DEFAULTUSER}](tg://user?id={mafia})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `Telethon:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `Version:` `{mafiaversion}`\n"
pm_caption += f"┣•➳➠ `Sudo:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `Channel:` [ᴊᴏɪɴ](https://t.me/Kisahkitaakukaudanmereka)\n"
pm_caption += f"┣•➳➠ `Creator:` [RIDWAN](https://t.me/psycho_syridwan)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥MOD 1🔥](https://t.me/CitraAyuWinieF) 🔹 [📜MOD 2📜](https://t.me/xnafrlzy)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAFIA_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
