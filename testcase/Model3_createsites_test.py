# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# #  Author: Duke
# #  Create Date: 2018/3/26
#
# import os, sys
# from importlib import reload
#
# #import unittest
# from common.pub import pub
# from common.extend_kw import ext
# from common.common_func import common
# from elements.elements import Homepage, personalpage, templatepage, mysite
#
#
#
# src_path = os.path.abspath('..')
# sys.path.append(src_path)
# reload(sys)
#
# cfg = common.read_yaml_config()
#
# class CreateSites(pub):
#
#     @classmethod
#     def setUpClass(cls):
#         ext.open_page(cfg['env']['url'])
#         ext.bases.click(Homepage.signinbtn)
#         ext.login(cfg['signIn']['account']['username'], cfg['signIn']['account']['password'])
#         ext.sleep(3)
#
#     def testCase01_CreateSites_preview_blankTmp(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.tmppreview(templatepage.personal_key,templatepage.personal_blank_select,templatepage.personal_blank_preview)
#         ext.sleep(5)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         preview_result = ext.bases.getElementText(templatepage.personal_blank_previewcheck)
#         ext.bases.closepage()
#         ext.bases.backtoDefaultWindow(current_window)
#         self.assertEqual(preview_result, cfg['tmppage']['personal']['blankpage'])
#
#     def testCase02_CreateSites_blanksite(self):
#         sitename = 'blank' + common.gen_random_string('All',3)
#         ext.createsite_By_temp(templatepage.personal_key,templatepage.personal_blank_select,sitename)
#         ext.bases.click(templatepage.domain_nextstep)
#         ext.sleep(10)
#         checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
#         self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])
#
#     def testCase03_CreateSites_preview_basicTmp(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.tmppreview(templatepage.personal_key, templatepage.personal_basic_select,
#                        templatepage.personal_basic_preview)
#         ext.sleep(5)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         preview_result = ext.bases.getElementText(templatepage.personal_basic_previewcheck)
#         ext.bases.closepage()
#         ext.bases.backtoDefaultWindow(current_window)
#         self.assertEqual(preview_result, cfg['tmppage']['personal']['basicpage'])
#
#     def testCase04_CreateSites_basicsite(self):
#         sitename = 'basic' + common.gen_random_string('All', 3)
#         ext.createsite_By_temp(templatepage.personal_key, templatepage.personal_basic_select, sitename)
#         ext.sleep(10)
#         checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
#         self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])
#
#     def testCase05_CreateSites_preview_resumeTmp(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.tmppreview(templatepage.personal_key, templatepage.personal_resume_select,
#                        templatepage.personal_resume_preview)
#         ext.sleep(5)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         preview_result = ext.bases.getElementText(templatepage.personal_resume_previewcheck)
#         ext.bases.closepage()
#         ext.bases.backtoDefaultWindow(current_window)
#         self.assertEqual(preview_result, cfg['tmppage']['personal']['resumepage'])
#
#     def testCase06_CreateSites_resumesite(self):
#         sitename = 'resume' + common.gen_random_string('All', 3)
#         ext.createsite_By_temp(templatepage.personal_key, templatepage.personal_resume_select, sitename)
#         ext.sleep(10)
#         checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
#         self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])
#
#     def testCase07_CreateSites_preview_vipTmp(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.tmppreview(templatepage.personal_key, templatepage.personal_vip_select,
#                        templatepage.personal_vip_preview)
#         ext.sleep(5)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         preview_result = ext.bases.getElementText(templatepage.personal_vip_previewcheck)
#         ext.bases.closepage()
#         ext.bases.backtoDefaultWindow(current_window)
#         self.assertEqual(preview_result, cfg['tmppage']['personal']['vippage'])
#
#     def testCase08_CreateSites_vipsite(self):
#         sitename = 'vip' + common.gen_random_string('All', 3)
#         ext.createsite_By_temp(templatepage.personal_key, templatepage.personal_vip_select, sitename)
#         ext.sleep(10)
#         checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
#         self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])
#
#     def testCase09_CreateSites_preview_company1Tmp(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.tmppreview(templatepage.company_key, templatepage.company_1_select,
#                        templatepage.company_1_preview)
#         ext.sleep(5)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         preview_result = ext.bases.getElementText(templatepage.company_1_previewcheck)
#         ext.bases.closepage()
#         ext.bases.backtoDefaultWindow(current_window)
#         self.assertEqual(preview_result, cfg['tmppage']['company']['company1'])
#
#     def testCase10_CreateSites_company1site(self):
#         sitename = 'company1' + common.gen_random_string('All', 3)
#         ext.createsite_By_temp(templatepage.company_key, templatepage.company_1_select, sitename)
#         ext.sleep(10)
#         checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
#         self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])
#
#     def testCase11_CreateSites_preview_company2Tmp(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.tmppreview(templatepage.company_key, templatepage.company_2_select,
#                        templatepage.company_2_preview)
#         ext.sleep(5)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         preview_result = ext.bases.getElementText(templatepage.company_2_previewcheck)
#         ext.bases.closepage()
#         ext.bases.backtoDefaultWindow(current_window)
#         self.assertEqual(preview_result, cfg['tmppage']['company']['company2'])
#
#     def testCase12_CreateSites_company2site(self):
#         sitename = 'company2' + common.gen_random_string('All', 3)
#         ext.createsite_By_temp(templatepage.company_key, templatepage.company_2_select, sitename)
#         ext.sleep(10)
#         checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
#         self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])
#
#     def testCase13_CreateSites_preview_groupTmp(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.tmppreview(templatepage.group_key, templatepage.group_select,
#                        templatepage.group_preview)
#         ext.sleep(5)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         preview_result = ext.bases.getElementText(templatepage.group_previewcheck)
#         ext.bases.closepage()
#         ext.bases.backtoDefaultWindow(current_window)
#         self.assertEqual(preview_result, cfg['tmppage']['group']['prepage'])
#
#     def testCase14_CreateSites_groupsite(self):
#         sitename = 'group' + common.gen_random_string('All', 3)
#         ext.createsite_By_temp(templatepage.group_key, templatepage.group_select, sitename)
#         ext.sleep(10)
#         checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
#         self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])
#
#     def testCase15_CreateSites_preview_gameTmp(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.tmppreview(templatepage.game_key, templatepage.game_select,
#                        templatepage.game_preview)
#         ext.sleep(5)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         preview_result = ext.bases.getElementText(templatepage.game_previewcheck)
#         ext.bases.closepage()
#         ext.bases.backtoDefaultWindow(current_window)
#         self.assertEqual(preview_result, cfg['tmppage']['game']['prepage'])
#
#     def testCase16_CreateSites_gamesite(self):
#         sitename = 'game' + common.gen_random_string('All', 3)
#         ext.createsite_By_temp(templatepage.game_key, templatepage.game_select, sitename)
#         ext.sleep(10)
#         checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
#         self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])
#
#     def testCase17_CreateSites_coursesite(self):
#         ext.switchMenu('siteManagement')
#         ext.bases.click(mysite.create)
#         ext.sleep(3)
#         ext.bases.click(templatepage.course_key)
#         ext.bases.click(templatepage.course_select)
#         ext.bases.click(templatepage.domain_next)
#         ext.sleep(5)
#         iframe_name = ext.bases.getElements(templatepage.course_daofeng_iframe)
#         ext.bases.switchToiFrame(iframe_name[0])
#         ext.sleep(2)
#         ext.bases.click(templatepage.course_daofeng_login)
#         ext.sleep(3)
#         current_window = self.driver.current_window_handle
#         ext.bases.switchToNewWindow(current_window)
#         ext.login('test001','123456')
#         ext.sleep(5)
#         ext.bases.click(templatepage.course_daofeng_agree_btn)
#         ext.bases.backtoDefaultWindow(current_window)
#         ext.sleep(2)
#         df_iframe_name = ext.bases.getElements(templatepage.course_daofeng_iframe)
#         ext.bases.switchToiFrame(df_iframe_name)
#         ext.bases.click(templatepage.course_daofeng_close_btn)
#         ext.sleep(2)
#
#
#     @classmethod
#     def tearDownClass(cls):
#         ext.bases.backtoDefaultPage()
#         ext.bases.back()
#         ext.bases.back()
#         ext.bases.back()
#         ext.logout()