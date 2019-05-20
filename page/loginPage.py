#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Duke
#  Create Date: 2018/3/16

import os,sys
from importlib import reload
from common import bases
from elements.elements import Homepage
from common.common_func import common
src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)
cfg = common.read_yaml_config()

class loginPage(bases.bases):
	def signIn_with_empty_account(self):		
		els_array = [Homepage.username,Homepage.password,Homepage.login]
		data = [cfg['login']['invaildusername'],cfg['login']['invaildpassword']]
		print(data)
		self.submitData(els_array,data)

		#self.equals()

	def signIn_with_right_account(self):
		els_array = [Homepage.username,Homepage.password,Homepage.login]
		data = [cfg['login']['username'],cfg['login']['password']]
		print(data)
		self.submitData(els_array,data)

	def logout(self):
		self.click(Homepage.avator)		
		self.click(Homepage.exit)