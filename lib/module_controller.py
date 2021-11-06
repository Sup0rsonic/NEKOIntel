import sqlite3
import os
import sys
import json
from lib.outputlib import *

with open(f'{os.path.dirname(os.path.abspath(__file__))}/../config.json') as fp:
    try:
        JSON_CONFIG = json.load(fp)
        debug('NEKOINTEL_LOAD_JSON')
    except json.JSONDecodeError as e:
        fatal(f'(ⓛωⓛ *) Fatal: The cat couldn\'t load the config json file. \nError: {e}', 1)

class ModuleController:
    def __init__(self):
        if not JSON_CONFIG:
            warning('(=🝦 ༝ 🝦=) Failed to load the config json file. Some functions might not be available')
        self.module_db = sqlite3.connect(JSON_CONFIG['sqlite_db_name'])
        return