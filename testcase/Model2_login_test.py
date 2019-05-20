#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Duke
#  Create Date: 2018/3/16

import os, sys
from importlib import reload

#import unittest
from common.pub import pub
from common.extend_kw import ext
from common.common_func import common
from elements.elements import Homepage, signIn


src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

cfg = common.read_yaml_config()

class Test_Login(pub):

    @classmethod
    def setUpClass(cls):
        ext.open_page(cfg['env']['url'])
    	ext.bases.click(Homepage.signinbtn)

    def testCase01_login_account_isEmpty(self):
        ext.bases.click(Homepage.signinbtn)
        ext.login(cfg['signIn']['emptyaccount']['username'],cfg['signIn']['emptyaccount']['password'])
        autual_value = ext.bases.getElementText(Homepage.checktext)
        self.assertEqual(autual_value,cfg['signIn']['expectMsg']['emptyaccount'])

    def testCase02_login_password_isEmpty(self):
        ext.login(cfg['signIn']['account']['username'], cfg['signIn']['emptyaccount']['password'])
        autual_value = ext.bases.getElementText(Homepage.checktext)
        self.assertEqual(autual_value, cfg['signIn']['expectMsg']['emptypassword'])

    def testCase03_login_password_isWrong(self):
        ext.login(cfg['signIn']['account']['username'], cfg['signIn']['invalidaccount']['password'])
        autual_value = ext.bases.getElementText(Homepage.checktext)
        self.assertEqual(autual_value, cfg['signIn']['expectMsg']['invalidpassword'])

    def testCase04_login_account_isnot_existed(self):
        ext.login(cfg['signIn']['invalidaccount']['username'],cfg['signIn']['account']['password'])
        autual_value = ext.bases.getElementText(Homepage.checktext)
        self.assertEqual(autual_value,cfg['signIn']['expectMsg']['invalidaccount'])

    def testCase05_login_accountType_isNumber(self):
        ext.login(cfg['signIn']['numberaccount']['username'], cfg['signIn']['numberaccount']['password'])
        ext.sleep(5)
        value = ext.bases.getElements(signIn.signsuccess)
        self.assertIsNone(value)
        ext.logout()

    def testCase06_login_bound_cellphone(self):
        ext.bases.click(Homepage.signinbtn)
        ext.login(cfg['signIn']['bindaccount']['mobile'], cfg['signIn']['account']['password'])
        ext.sleep(5)
        value = ext.bases.getElements(signIn.signsuccess)
        self.assertIsNone(value)
        ext.logout()

    def testCase07_login_bound_email(self):
        ext.bases.click(Homepage.signinbtn)
        ext.login(cfg['signIn']['bindaccount']['email'], cfg['signIn']['account']['password'])
        ext.sleep(5)
        value = ext.bases.getElements(signIn.signsuccess)
        self.assertIsNone(value)
        ext.logout()

    def testCase08_login_with_keepworkaccount(self):
        ext.bases.click(Homepage.signinbtn)
        ext.login(cfg['signIn']['account']['username'], cfg['signIn']['account']['password'])
        ext.sleep(5)
        value = ext.bases.getElements(signIn.signsuccess)
        self.assertIsNone(value)
        ext.logout()

    # @classmethod
    # def tearDownClass(cls):
    # 	cls.driver.quit()