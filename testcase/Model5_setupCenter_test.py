#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Duke
#  Create Date: 2018/3/28

import os, sys
from importlib import reload

#import unittest
from common.pub import pub
from common.extend_kw import ext
from common.common_func import common
from elements.elements import Homepage, signIn,setupCenter


src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

cfg = common.read_yaml_config()

class Login(pub):
    @classmethod
    def setUpClass(cls):
        ext.open_page(cfg['env']['url'])
        ext.bases.click(Homepage.signinbtn)

    def testCase01_login_account_isEmpty(self):
        pass

    # @classmethod
    # def tearDownClass(cls):
    # 	cls.driver.quit()