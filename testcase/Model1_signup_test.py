# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# #  Author: Duke
# #  Create Date: 2018/3/16
#
# import os, sys
# from importlib import reload
#
# #import unittest
# from common.pub import pub
# from common.extend_kw import ext
# from common.common_func import common
# from elements.elements import Homepage, signIn, signUp,setupCenter
# from page import loginPage
#
# src_path = os.path.abspath('..')
# sys.path.append(src_path)
# reload(sys)
#
# cfg = common.read_yaml_config()
#
#
# class Signup(pub):
#     @classmethod
#     def setUpClass(cls):
#         ext.open_page(cfg['env']['url'])
#         ext.sleep(2)
#
#     def testCase01_signup_allinfo_isEmpty(self):
#         ext.bases.click(Homepage.signupbtn)
#         ext.sleep(1)
#         ext.signUp(cfg['signup']['emptyaccount']['username'], cfg['signup']['emptyaccount']['password'],
#                    cfg['signup']['emptyaccount']['cellphone'])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value, cfg['signup']['expectMsg']['emptyAllinfo'][index])
#
#     def testCase02_signup_username_isEmpty(self):
#         ext.signUp(cfg['signup']['emptyaccount']['username'], cfg['signup']['account']['password'],
#                    cfg['signup']['account']['cellphone'][2])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 print(index, value)
#                 self.assertEqual(value, cfg['signup']['expectMsg']['emptyAccountinfo'][index])
#
#     def testCase03_signup_username_rules(self):
#         ext.signUp(cfg['signup']['accountrules']['username'], cfg['signup']['account']['password'],
#                    cfg['signup']['account']['cellphone'][2])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value, cfg['signup']['expectMsg']['rulesinfo'][index])
#
#     def testCase04_signup_username_isNumber(self):
#         ext.signUp(cfg['signup']['numberaccount']['username'], cfg['signup']['account']['password'],
#                    cfg['signup']['account']['cellphone'][2])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value, cfg['signup']['expectMsg']['numAccountinfo'][index])
#
#     def testCase05_signup_username_contain_sensitiveword(self):
#         ext.signUp(cfg['signup']['invaildaccount']['username'], cfg['signup']['account']['password'],
#                    cfg['signup']['account']['cellphone'][2])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value, cfg['signup']['expectMsg']['filteraccountinfo'][index])
#
#     def testCase06_signup_username_length_overlimit(self):
#         username = common.gen_random_string('All',31)
#         ext.signUp(username, cfg['signup']['account']['password'], cfg['signup']['account']['cellphone'][2])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value,cfg['signup']['expectMsg']['overaccount'][index])
#
#     def testCase07_signup_password_isEmpty(self):
#         ext.signUp(cfg['signup']['account']['username'], cfg['signup']['emptyaccount']['password'],
#                    cfg['signup']['account']['cellphone'][2])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value, cfg['signup']['expectMsg']['invaildpwd'][index])
#
#     def testCase08_signup_password_length(self):
#         ext.signUp(cfg['signup']['account']['username'], cfg['signup']['invaildaccount']['password'], cfg['signup']['account']['cellphone'][2])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value,cfg['signup']['expectMsg']['invaildpwd'][index])
#
#     def testCase09_signup_invaild_cellphone(self):
#         ext.getSMScode(cfg['signup']['account']['username'], cfg['signup']['account']['password'],
#                    cfg['signup']['invaildaccount']['cellphone'])
#         check_value = ext.bases.getElstextByLocator(signUp.checktext)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value, cfg['signup']['expectMsg']['vaildcellphone'][index])
#
#     def testCase10_signup_bound_cellphone(self):
#         ext.getSMScode(cfg['signup']['account']['username'], cfg['signup']['account']['password'],
#                        cfg['signup']['account']['cellphone'][0])
#         ext.inputSMScode(cfg['signup']['account']['smscode'])
#         ext.sleep(1)
#         check_value = ext.bases.getElstextByLocator(signUp.checkrepeatinfo)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value,cfg['signup']['expectMsg']['repeatphone'])
#
#     def testCase11_signup_invaild_smscode(self):
#         ext.bases.click(Homepage.signupbtn)
#         ext.getSMScode(cfg['signup']['account']['username'], cfg['signup']['account']['password'],
#                        cfg['signup']['account']['cellphone'][2])
#         ext.inputSMScode(cfg['signup']['invaildaccount']['smscode'])
#         ext.sleep(1)
#         check_value = ext.bases.getElstextByLocator(signUp.checkrepeatinfo)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value, cfg['signup']['expectMsg']['errorSMScode'])
#
#     def testCase12_signup_backtoHome(self):
#         username = 'test'+ common.gen_random_string('int')
#         password = common.gen_random_string('int')
#         data = username + '/' + password +'\n'
#         common.write_account_config(data)    #账号信息写入accout.txt文件里
#         ext.bases.click(Homepage.signupbtn)
#         ext.getSMScode(username, password, cfg['signup']['account']['cellphone'][2])
#         ext.inputSMScode(cfg['signup']['account']['smscode'])
#         ext.sleep(10)
#         ext.bases.click(signUp.backbtn)   #点击返回按钮
#         ext.sleep(2)
#         ### 进行手机解绑操作，以便下次注册使用
#         ext.switchMenu('setupCenter')
#         ext.bases.click(setupCenter.security_key)
#         ext.bases.click(setupCenter.security_bindTab_key)
#         ext.bases.click(setupCenter.security_bindTab_mobile_unbindbtn)
#         ext.bindpage(cfg['signup']['account']['smscode'])
#         ext.logout()
#
#     def testCase13_signup_backtoPersoanlpage(self):
#         username = 'test' + common.gen_random_string('int')
#         password = common.gen_random_string('int')
#         data = username + '/' + password + '\n'
#         common.write_account_config(data)  # 账号信息写入accout.txt文件里
#         ext.bases.click(Homepage.signupbtn)
#         ext.getSMScode(username, password, cfg['signup']['account']['cellphone'][2])
#         ext.inputSMScode(cfg['signup']['account']['smscode'])
#         ext.sleep(10)
#         ext.bases.click(signUp.gotohome)  # 点击返回按钮
#         ext.sleep(2)
#         ### 进行手机解绑操作，以便下次注册使用
#         ext.switchMenu('setupCenter')
#         ext.bases.click(setupCenter.security_key)
#         ext.bases.click(setupCenter.security_bindTab_key)
#         ext.bases.click(setupCenter.security_bindTab_mobile_unbindbtn)
#         ext.bindpage(cfg['signup']['account']['smscode'])
#         ext.logout()
#
#     def testCase14_signup_duplicate_Account(self):
#         ext.bases.click(Homepage.signupbtn)
#         ext.getSMScode(cfg['signup']['repeataccount']['username'], cfg['signup']['account']['password'], cfg['signup']['account']['cellphone'][2])
#         ext.inputSMScode(cfg['signup']['account']['smscode'])
#         ext.sleep(2)
#         check_value = ext.bases.getElstextByLocator(signUp.checkrepeatinfo)
#         if isinstance(check_value, list):
#             for index, value in enumerate(check_value):
#                 self.assertEqual(value,cfg['signup']['expectMsg']['repeataccount'])
#
#
#     # @classmethod
#     # def tearDownClass(cls):
#     # 	cls.driver.quit()
#
#
#
#
#
#
