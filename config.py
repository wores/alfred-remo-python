# encoding: utf-8
import os
import json
import sys
from workflow import Workflow, notify


__CONFIG_FILE_NAME = 'config.json'
__BUNDLE_ID = 'com.wrs.nature-remo'


class Config:

    def __init__(self, config_dict={}):
        self._access_token = config_dict.get('access_token', '')
        self._aircon_id = config_dict.get('aircon_id', '')

    @property
    def access_token(self):
        return self._access_token

    @property
    def aircon_id(self):
        return self._aircon_id


def __getDefaultConfigPath():
    home_dir = os.path.expanduser('~')
    return os.path.join(home_dir, "Library/Application Support/Alfred 2/Workflow Data/", __BUNDLE_ID)


def __readFile():
    config_path = __getDefaultConfigPath()
    file_path = os.path.join(config_path, __CONFIG_FILE_NAME)
    dic = {}
    if not os.path.exists(file_path):
        return dic

    with open(file_path, 'r') as f:
        dic = json.load(f)

    return dic


def update_access_token(access_token):
    dic = { 'access_token': access_token }
    update_config(dic)


def update_aircon_id(aircon_id):
    dic = { 'aircon_id': aircon_id }
    update_config(dic)


def update_config(data_dic):
    config_path = __getDefaultConfigPath()
    if not os.path.exists(config_path):
        os.makedirs(config_path)
        os.chmod(config_path, 0777)

    current = __readFile()
    current.update(data_dic)
    file_path = os.path.join(config_path, __CONFIG_FILE_NAME)
    with open(file_path, 'w') as f:
        json.dump(current, f, indent=4)


def create_config():
    return Config(__readFile())
