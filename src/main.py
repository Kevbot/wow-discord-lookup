#!/usr/bin/env python

"""
main.py: 
    - Initializes the Discord bot and awaits user input.
    - Makes API requests to Blizzard's API by using credentials retrieved through settings.py
    - Instantiates a Character object for the searched character
    - Calls input_handler.py to parse user input and character_utils.py to print output.
"""

import asyncio
import json
import requests

import discord
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound
from discord.ext import commands

from settings import TOKEN, PREFIX 
from settings import SEARCH_COMM_STR, HELP_COMM_STR, STOP_COMM_STR
from request_handler import get_api_data
from io_handler import format_expansion_info
from io_handler import format_character_info


Client = discord.Client()  # Initialise Client
client = commands.Bot(command_prefix=PREFIX, case_insensitive=True,
                      help_command=None)  # Initialise client bot

# pylint: disable=E1101

@client.event
async def on_ready():
    print("Bot is online and connected to Discord.")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


#@client.command(aliases=expansion_pack_names)
@client.command(name=SEARCH_COMM_STR)
async def event_loop(ctx):
    if ctx.author == client.user:
        return

    char_response, exp_response = get_api_data(ctx.message)
    await print_result_to_discord(ctx, char_response, exp_response)


@client.command(name=STOP_COMM_STR)
async def logout(ctx):
    await ctx.send(f"{STOP_COMM_STR.upper()} command issued - logging off.")
    await client.logout()


@client.command(name=HELP_COMM_STR)
async def print_help_msg(ctx):
    help_text = "How to use this bot:\n"
    help_text += f"\nExample: `{PREFIX}{SEARCH_COMM_STR} bfa asmongold us kel'thuzad`"
    help_text += f"\nExample: `{PREFIX}{SEARCH_COMM_STR} wotlk armory eu ragnaros`\n"
    help_text += f"\nAvailable server regions: US, EU, KR, TW, CN\n"
    await ctx.send(help_text)


async def print_char_not_found(ctx):
    error_msg = f"<@%s> Character not found. Please double check the character name, region, and realm." % (
        ctx.author.id)
    error_msg += f" Use `{PREFIX}{HELP_COMM_STR}` for more information."
    await ctx.send(error_msg)

async def print_result_to_discord(ctx, char_response, exp_response):
    if char_response.status_code != requests.codes.ok or exp_response[0].status_code != requests.codes.ok:
        print("DEBUG: Error retrieving character or expansion data")
        await print_char_not_found(ctx)
    else:
        output_to_discord = "<@%s>\n" % (ctx.author.id)
        output_to_discord += format_character_info(char_response)
        output_to_discord += format_expansion_info(exp_response[0], exp_response[1])
        await ctx.send(output_to_discord)

client.run(TOKEN)
