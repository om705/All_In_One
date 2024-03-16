#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6507614205:AAEKQjmh8RiZBWBuxYtUELo1bhOt_JVrYZU")
    API_ID = int(os.environ.get("API_ID", "22114233"))
    API_HASH = os.environ.get("API_HASH", "d7abcec5c967414fadb1d438fa05ebea")
    AUTH_USERS = "1403488629"

