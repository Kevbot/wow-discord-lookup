#!/usr/bin/env python

"""
io_handler.py: 
    - Filters Discord user input and returns sanitized input to main.py
"""

import json
import os

def parse_user_input(message):
    INPUT_EXP_PACK_INDEX = 1
    INPUT_CHAR_NAME_INDEX = 2
    INPUT_REGION_INDEX = 3
    INPUT_CHARACTER_REALM_INDEX = 4
    INPUT_MIN_WORD_COUNT = 5

    exp_pack = message[INPUT_EXP_PACK_INDEX].lower()
    region = message[INPUT_REGION_INDEX].lower()
    char_name = message[INPUT_CHAR_NAME_INDEX].lower()
    realm = ''

    if len(message) < INPUT_MIN_WORD_COUNT:
        return None, None, None, None

    # covers cases such as "Sisters of Elune"
    if len(message) > INPUT_MIN_WORD_COUNT:
        for word_index in range(INPUT_CHARACTER_REALM_INDEX, len(message)):
            realm += message[word_index]
            realm += "-" if (word_index != len(message)-1) else ''

    # covers cases such as Kel'Thuzad and Azjol-Nerub
    elif len(message) == INPUT_MIN_WORD_COUNT:
        realm = message[INPUT_CHARACTER_REALM_INDEX].replace(
            "-", "").replace("'", "")

    print(f"DEBUG: {exp_pack} {char_name} {region} {realm}")
    return exp_pack, char_name, region, realm


def get_region_info(region):
    if os.path.isfile('./json/regions.json'):
        regions_file_path = './json/regions.json'
    elif os.path.isfile('./src/json/regions.json'):
        regions_file_path = './src/json/regions.json'
    elif os.path.isfile('app/src/json/regions.json'):
        regions_file_path = 'app/src/json/regions.json'

    regions_file = open(regions_file_path)
    regions_data = json.load(regions_file)

    api_namespace = None
    api_locale = None
    api_region_short = None

    for data in regions_data["regions"]:
        if data["region"]["abbreviation"] == region:
            api_namespace = data["region"]["namespace"]
            api_locale = data["region"]["locale"]
            api_region_short = data["region"]["abbreviation"]
            break

    regions_file.close()
    return api_namespace, api_locale, api_region_short


def get_expansion_info(expansion):
    if os.path.isfile('./json/expansions.json'):
        expansions_file_path = './json/expansions.json'
    elif os.path.isfile('./src/json/expansions.json'):
        expansions_file_path = './src/json/expansions.json'
    elif os.path.isfile('app/src/json/expansions.json'):
        expansions_file_path = 'app/src/json/expansions.json'

    #expansions_file_path = "./src/expansions.json"
    expansions_file = open(expansions_file_path)
    expansions_data = json.load(expansions_file)
    expansions_index = None

    for data in expansions_data["expansions"]:
        for aliases in data["expansion"]["aliases"]:
            if aliases["alias"]["name"] == expansion:
                expansions_index = data["expansion"]["key"]
                break
                
    expansions_file.close()
    return expansions_index


def format_expansion_info(response, index):
    length = len(response.json()["expansions"])

    print(f"DEBUG: Expansion index is {index}, returned length of JSON query is {length}")

    if index > len(response.json()["expansions"]) - 1:
        output_data = "Character has no raid progress for the selected expansion pack."
    else:
        expansion_name = response.json()["expansions"][index]["expansion"]["name"]
        raids = response.json()["expansions"][index]["instances"]
        output_data = ("=" * 30 + "\n") + "Raid progress for " + expansion_name + ":\n" + ("=" * 30 + "\n")
        
        for i in range(0, len(raids)):
            output_data += (" " + raids[i]["instance"]["name"] + ":\n")
            for j in range(0, len(raids[i]["modes"])):
                completed_count = raids[i]["modes"][j]["progress"]["completed_count"]
                total_count = raids[i]["modes"][j]["progress"]["total_count"]
                difficulty = raids[i]["modes"][j]["difficulty"]["name"]
                output_data += (f"\t{completed_count}/{total_count} {difficulty}\n")
            output_data += "=" * 30 + "\n"
    return output_data

def format_character_info(response):
    name = response.json()["name"]

    # It is possible for the character to be guildless.
    try:
        guild = "<" + response.json()["guild"]["name"] + ">"
    except:
        guild = ""
    
    realm = response.json()["realm"]["name"]
    race = response.json()["race"]["name"]
    spec = response.json()["active_spec"]["name"]
    character_class = response.json()["character_class"]["name"]
    item_level = "Item level: " + str(response.json()["equipped_item_level"])

    output_data = f"{name}{guild} - {realm}\n{race} {spec} {character_class}\n{item_level}\n"

    return output_data