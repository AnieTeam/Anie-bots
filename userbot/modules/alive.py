from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from userbot.uniborgConfig import Config
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DevilUserBot User"

PM_IMG = Config.ALIVE_PIC

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

pm_caption = "__**π₯π₯Anie ΟΡΡΡΠ²ΟΡ ΞΉΡ ΟΞ· ΖΞΉΡΡπ₯π₯**__\n\n"

pm_caption += (
    f"               __βΌπΌπ°πππ΄πβ__\n**γ[{DEFAULTUSER}](tg://user?id={kraken})γ**\n\n"
)

pm_caption += "β ΓͺlΓͺβ hΓ°Γ± VΓͺrΒ§Γ―Γ°Γ±: `1.15.0` \n"

pm_caption += "κ£κ¦κκ»κ²κ κ¦κκͺκκκ²κ:      `3.7.4` \n"

pm_caption += f"Anie VΙβ±€β΄ΕΓβ¦:  __**D.0**__\n"

pm_caption += f"sα΄α΄α΄            : `{sudou}`\n"

pm_caption += "κκ€κ£κ£κ²κͺκ κκͺκ²κ€κ£  : [α΄α΄ΙͺΙ΄](https://t.me/Aniebotsupports)\n"

pm_caption += "π²ππππππ    : [Click Here](https://t.me/d3nvil)\n\n"

pm_caption += "    [β¨REPOβ¨](https://github.com/Anieteam/Anie-userbot) πΉ [πLicenseπ](https://github.com/lucifeermorningstar/deviluserbot/blob/master/LICENSE)"



@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'denvil', None, 'Check weather yhe bit is alive or not. In your custom Alive Pic and Alive Msg if in Heroku Vars'
).add()
