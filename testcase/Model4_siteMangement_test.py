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
from elements.elements import Homepage, personalpage,mysite, purchaseVip,signIn,templatepage
from page import loginPage

src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

cfg = common.read_yaml_config()
global siteNum
class siteMangement(pub):
    @classmethod
    def setUpClass(cls):
        ext.bases.click(Homepage.signinbtn)
        ext.login(cfg['signIn']['account']['username'], cfg['signIn']['account']['password'])
        ext.sleep(3)

    def testCase01_siteMangement_siteNum_validate(self):
        siteNum = ext.getSitesNum()
        if(siteNum>0):
            siteInfo = ext.getWebsitesInfo(siteNum)
            print("序号     站点名称   站点地址   创建时间")
            for index, infos in enumerate(siteInfo):
                print("NO."+str(index+1) +":"+ infos["sitename"] + " " + infos["address"] + " " +infos["dates"])
        else:
            print("you need to create a site first!")

    def testCase02_siteMangement_private_site(self):
        # siteNum = ext.getSitesNum()
        if(siteNum>0):
            info = ext.getPrivatesite(siteNum)
            print("private sites Num is " +  info["num"] )
            for subinfo in info["details"]:
                print("The sites info is " + subinfo)
        else:
            print("you need to create a site first!")

    def testCase03_siteMangement_create_newsite(self):
        site = ext.getWebsitesInfo(1)
        for info in site:
            if(info["address"].find('11') != (-1)):
                ext.delwebsite(mysite.operation_remove_key)
                siteNum = siteNum - 1

        ext.bases.click(mysite.create)
        ext.createsite_By_temp(templatepage.personal_key, templatepage.personal_blank_select, cfg['sites']['sitename'])
        ext.bases.click(templatepage.domain_nextstep)
        ext.sleep(10)
        checksuccess = ext.bases.getElementText(templatepage.domain_checksuccess)
        self.assertEqual(checksuccess.strip(), cfg['tmppage']['createResult'])


    def testCase04_siteMangement_siteNum_validateAgain(self):
        pass

    def testCase05_siteMangement_siteNum_validate(self):
        pass

    def testCase06_siteMangement_siteNum_validate(self):
        pass


