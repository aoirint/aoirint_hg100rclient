from getpass import getpass
import json
import os
from pathlib import Path
from pydantic import BaseModel, parse_obj_as

CONFIG_PATH = Path(os.path.expanduser('~/.hg100rclientrc'))

class Config(BaseModel):
  router_url: str
  password: str

def load_config() -> Config:
  if not CONFIG_PATH.exists():
    raise Exception('Config not exist. Call interactive_config()')

  with open(CONFIG_PATH, 'r', encoding='utf-8') as fp:
    return parse_obj_as(Config, json.load(fp))

def save_config(config: Config):
  with open(CONFIG_PATH, 'w', encoding='utf-8') as fp:
    fp.write(config.json())

def interactive_config():
  if CONFIG_PATH.exists():
    # TODO: validate auth
    return

  router_url = input('Router URL: ')
  password = getpass(prompt='Password: ')

  save_config(Config(
    router_url=router_url,
    password=password,
  ))
