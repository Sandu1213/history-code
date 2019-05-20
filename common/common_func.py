#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Duke
# Create Date: 2018/3/15
import os
import random
import string
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from config import config
import yaml

class common():
    def getDriver():
        driver = webdriver.Remote(
            command_executor= 'http://127.0.0.1:4444/wd/hub',
            desired_capabilities= DesiredCapabilities.CHROME
        )
        return driver

    def gen_random_string(type,str_len=6):
        if(type == 'str'):
            randomstr = ''.join(random.choice(string.ascii_letters) for _ in range(str_len)).lower()
            return randomstr
        elif(type == 'int'):
            randomstr = ''.join(random.choice(string.digits) for _ in range(str_len))
            return randomstr
        else:
            randomstr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len)).lower()
            return randomstr

    # get current date, default format is %Y-%m-%d
    def get_current_date(fmt="%Y-%m-%d"):
        return datetime.datetime.now().strftime(fmt)

    def create_dir(dirname):
        if os.path.exists(dirname) is not True:
            os.mkdir(dirname)
    
    def read_yaml_config():
        yaml_config = 'config/config.yml'
        with open(yaml_config, 'r',encoding='utf-8') as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg
    
    def write_account_config(data):
        account_file = 'account.txt'
        fo = open(account_file,'a+')
        fo.write(data)
        fo.close()