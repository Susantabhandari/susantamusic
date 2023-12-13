import random
import re
import string

import lyricsgenius as lg
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS, lyrical
from VenomX import app
from VenomX.utils.decorators.language import language

api_key = "P2xjUTYciOtLP6ojcobvMpX419x4aVUzA12x6pl-a4ZybUxWybN3Z-P8tcD2B0M-csh2rkqCIO2aElZBeiWzug"
genius_api = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
genius_api.verbose = False

@app.on_message(
    filters.command(["lyrics"]) 
    & ~BANNED_USERS
)
@language
async def search_lyrics(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text(_["lyrics_1"])

    title = message.text.split(None, 1)[1]
    reply_message = await message.reply_text(_["lyrics_2"])

    song_result = genius_api.search_song(title, get_full_info=False)

    if song_result is None:
        return await reply_message.edit(_["lyrics_3"].format(title))

    random_hash = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    lyrics = song_result.lyrics

    if "Embed" in lyrics:
        lyrics = re.sub(r"\d*Embed", "", lyrics)

    lyrical[random_hash] = lyrics

    keyboard_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["L_B_1"],
                    url=f"https://t.me/{app.username}?start=lyrics_{random_hash}",
                ),
            ]
        ]
    )

    await reply_message.edit(_["lyrics_4"], reply_markup=keyboard_markup)
