#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MemberCounterMeta Telegram bot by TeLe TiPs] (https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/MemberCounterMeta

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio
from texts.texts_teletips import *

MemberCounterMeta = Client(
    name = "membercountermeta",
    api_id = int(os.environ["14055090"]),
    api_hash = os.environ["a46f7b439d0afa45b7a69fc450f754e9"],
    session_string = os.environ["1BVtsOIkBuy3uFjMYzr5t6QzTJ_Jx3wdEloCwDopspcyk-VT2muCoDs0sUCRN6BS-5OfIVFMlgUZ_5O4xETTgy4MJs2L9LokmXZ2lWxvgr0kfdSxFvX5P6vW_X6d9tgy1X9eGnKNZDJLLOb35dLkI8opl1KBXKtAVhBx8Tblqq27HQZ96Et4TlamQcdIHHLadtl49dVsdUiScFQAUWpXujMoblMUwdiPq1IcHCU6Az-gc0usAWh_SniNHZF0w1P2hH3UGiKoEsyEqOnCnN6hLY2tKPOKYNLT2KeOsN4bOZkvMJ_w4awhPVLI9Utmz0IgCXbqbF6AIoo2F4ZPKvPnJB4zS4PHdLvI="]
)
CHANNEL_OR_GROUP_LIST = [i.strip() for i in os.environ.get("-1001742371821").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["-1001742371821"])
MESSAGE_ID = int(os.environ["-1001742371821"])

print(text_1)
async def main_MemberCounterMeta():
    async with MemberCounterMeta:
        try:
            while True:
                print(text_2)
                edit_message_text_teletips = "**📈 | Emo Member Counter** ☘ The Simple And Fast Member Counter On Telegram"
                for CHANNEL_OR_GROUP in CHANNEL_OR_GROUP_LIST:
                    try:
                        get_chat_teletips = await MemberCounterMeta.get_chat(int(CHANNEL_OR_GROUP))   
                        if get_chat_teletips.type == "channel":
                            edit_message_text_teletips += f"\n\n📣  **{get_chat_teletips.title}**\n👤 ├ <i>{get_chat_teletips.members_count} Subscribers</i>\n🔗 └ <i>[Link]({get_chat_teletips.invite_link})</i> \n\n ⚡ Powerd By @emMemberCounter_Bot"
                        else:
                            edit_message_text_teletips += f"\n\n💬  **{get_chat_teletips.title}**\n👤 ├ <i>{get_chat_teletips.members_count} Members</i>\n🔗 └ <i>[Link]({get_chat_teletips.invite_link})</i> \n\n ⚡ Powerd By @emMemberCounter_Bot" 
                        await asyncio.sleep(2)
                    except ValueError:
                        print(f'🤷‍♂️ ID not found: {CHANNEL_OR_GROUP }. Skipping...')                       
                edit_message_text_teletips += f"\n\n<i>♻ Automatically refreshes every 15 minutes</i>"
                try:
                    await MemberCounterMeta.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, edit_message_text_teletips, disable_web_page_preview=True)
                except Exception:
                    pass    
                print(text_3)              
                await asyncio.sleep(900) # 15 minutes = 900 seconds
        except FloodWait as e:
            await asyncio.sleep(e.x)

@MemberCounterMeta.on_message(filters.command("status", "!") & filters.me)
async def alive(_, message: Message):
    await message.edit(" Member Counter is alive!")
    await asyncio.sleep(10)
    await message.delete()                   
                        
MemberCounterMeta.run(main_MemberCounterMeta())

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
