#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from config import Config
from pyrogram import Client as ACE, idle
import asyncio
from logging.handlers import RotatingFileHandler
from plugins.regix import restart_forwards

RESATRT = True

# Auth Users
BOT_OWNER_ID = [Config.BOT_OWNER_ID]

# Prefixes 
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")

if __name__ == "__main__":
    AceBot = ACE(
        "AceBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=plugins
    )

    async def main():
        await AceBot.start()
        bot_info = await AceBot.get_me()
        # LOGGER.info(f"<--- @{bot_info.username} Started (c) ACE --->")
        if RESATRT:
            await restart_forwards(AceBot)
        await idle()

    asyncio.get_event_loop().run_until_complete(main())
    # LOGGER.info(f"<---Bot Stopped--->")
