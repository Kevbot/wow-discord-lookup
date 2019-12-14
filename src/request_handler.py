#!/usr/bin/env python

"""
request_handler.py: 
    - Sends requests to the Blizzard API and returns the responses
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from settings import ID, SECRET
from io_handler import parse_user_input, get_region_info, get_expansion_info

def get_api_data(message):
    
    exp_pack, char_name, region, realm = parse_user_input(message.content.split(" "))
    expansion_index = get_expansion_info(exp_pack)
    api_namespace, api_locale, api_region_short = get_region_info(region)

    path = '/oauth/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(ID, SECRET)
    base_url = 'https://{0}.battle.net{1}'.format(api_region_short, path)

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    response = session.get(base_url)
    json = response.json() # access token info
    token = json['access_token']

    access_url = f'https://{api_region_short}.api.blizzard.com/profile/wow/character/{realm}/{char_name}?namespace={api_namespace}&locale={api_locale}&access_token={token}'
    char_response = session.get(access_url)
    
    access_url = f'https://{api_region_short}.api.blizzard.com/profile/wow/character/{realm}/{char_name}/encounters/raids?namespace={api_namespace}&locale={api_locale}&access_token={token}'
    exp_response = session.get(access_url)
    exp_response = [exp_response, expansion_index]

    return char_response, exp_response