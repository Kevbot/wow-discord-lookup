#!/usr/bin/env python

"""
settings.py: 
    - Initializes environment variables from .env file and sets the Discord bot command variables
"""

import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

# environment vars
TOKEN = os.getenv("OAUTH2")
ID = os.getenv("WOW_CLIENT_ID2")
SECRET = os.getenv("WOW_CLIENT_SECRET2")

# Discord bot parameters
PREFIX = "!"
SEARCH_COMM_STR = "char"
HELP_COMM_STR = "help"
STOP_COMM_STR = "stop"