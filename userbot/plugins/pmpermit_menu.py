# if you change credits, you get anal cancer and get murdered by russians in 3 days.
"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
"""
import asyncio

from telethon import functions

from userbot.plugins.sql_helper import pmpermit_sql as pmpermit_sql
from userbot.Config import Config
from . import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Mafia User"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.sender_id
    event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:

            PM = (
"`Halo. Anda sedang mengakses menu yang tersedia di fitur private saya,`"
                f"{DEFAULTUSER}.\n"
                "Mari kita buat ini lancar dan beri tahu saya mengapa Anda ada di sini.\n"
                "Pilih salah satu alasan berikut mengapa Anda ada di sini:\n\n"
                "1. Untuk mengobrol dengan tuanku\n"
                "2. Untuk memberikan nomor pacarmu.\n"
                "3. Untuk menanyakan sesuatu\n"
                "4. Untuk meminta sesuatu\n"
            )
            ONE = (
                "_Oke. Permintaan Anda telah didaftarkan. Jangan mengirim spam ke kotak masuk tuan saya. Anda dapat mengharapkan balasan dalam waktu 24 tahun cahaya. Dia orang yang sibuk, tidak seperti Anda mungkin._\n\n"
                "⚠️ **Anda akan diblokir dan dilaporkan jika Anda melakukan spam** ️\n\n"
                "_Gunakan `/start` untuk kembali ke menu utama._"
            )
            TWO = "**Sangat tidak keren, ini bukan rumahmu. Pergi mengganggu orang lain. Anda telah diblokir dan dilaporkan hingga pemberitahuan lebih lanjut**"
            FOUR = "_Baik. Tuanku belum melihat pesanmu. Dia biasanya menanggapi orang, meskipun aku tidak tahu tentang yang terbelakang._\n _Dia akan menjawab ketika dia kembali, jika dia mau. Sudah ada banyak pesan yang tertunda😶_\n **Tolong jangan melakukan spam kecuali jika Anda ingin diblokir dan dilaporkan.**"
            FIVE = "`Baik. tolong miliki dasar tata krama, agar tidak terlalu mengganggu tuanku. Jika dia ingin membantu Anda, dia akan segera membalas Anda.`\n**Jangan bertanya berulang-ulang karena Anda akan diblokir dan dilaporkan.**"
            LWARN = "**Ini peringatan terakhirmu. JANGAN kirim pesan lain, Anda akan diblokir dan dilaporkan. Tetap sabar. Tuanku akan menjawab Permintaan Anda.**\n_Gunakan_ `/start` _untuk kembali ke menu utama._"

        async with borg.conversation(chat) as conv:
            await borg.send_message(chat, PM)
            chat_id = event.sender_id
            response = await conv.get_response(chat)
            y = response.text
            if y == "1":
                await borg.send_message(chat, ONE)
                response = await conv.get_response(chat)
                await event.delete()
                if not response.text == "/start":
                    await response.delete()
                    await borg.send_message(chat, LWARN)
                    response = await conv.get_response(chat)
                    await event.delete()
                    await response.delete()
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            elif y == "2":
                await borg.send_message(chat, LWARN)
                response = await conv.get_response(chat)
                if not response.text == "/start":
                    await borg.send_message(chat, TWO)
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat_id))

            elif y == "3":
                await borg.send_message(chat, FOUR)
                response = await conv.get_response(chat)
                await event.delete()
                await response.delete()
                if not response.text == "/start":
                    await borg.send_message(chat, LWARN)
                    await event.delete()
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            elif y == "4":
                await borg.send_message(chat, FIVE)
                response = await conv.get_response(chat)
                if not response.text == "/start":
                    await borg.send_message(chat, LWARN)
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            else:
                await borg.send_message(
                    chat,
                    "`Anda telah memasukkan perintah yang tidak valid. Silakan kirim /start lagi atau jangan kirim pesan lain jika Anda tidak ingin diblokir dan dilaporkan.`",
                )
                response = await conv.get_response(chat)
                z = response.text
                if not z == "/start":
                    await borg.send_message(chat, LWARN)
                    await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
