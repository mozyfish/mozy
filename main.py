import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random


import random
with open('database.txt', encoding='utf-8') as file:
    lines = file.readlines()
    random_line = random.choice(lines)

with open('random_line.txt', 'w') as file:
    file.write(random_line)



@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    num = 0
    while (num<10):
        try:
            msg.edit(random_line)
            return random_line
        except FloodWait as e:

            sleep(e.x)



app.run()
