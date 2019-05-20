#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Duke
# CreateDate:2018/3/20

from elements.elements import Homepage, personalpage, realNamepage, templatepage, mysite, setupCenter, purchaseVip, \
    signIn, signUp
import time
from selenium.webdriver.common.by import By
from common import bases
from common.pub import pub

kw = bases.bases(pub.driver)
class ext():
    bases = kw
    #打开测试页面
    def open_page(url):
        pub.driver.maximize_window()
        pub.driver.get(url)
    #登陆
    def login(username,password):
        els_array = [Homepage.username,Homepage.password,Homepage.login]
        els = [signIn.username,signIn.password,signIn.login]
        data = [username,password]
        current_url = kw.getCurrentUrl()
        if(current_url.find('home') != (-1)):
            kw.submitData(els_array,data)
        else:
            kw.submitData(els,data)

    #退出
    def logout():
        kw.click(Homepage.avator)
        kw.click(Homepage.exit)

    #注册
    def signUp(username,password,cellphone):
        els_array = [signUp.username,signUp.password,signUp.cellphone,signUp.signupbtn]
        data = [username,password,cellphone]
        kw.submitData(els_array,data)

    #获取手机的验证码(注册页面)
    def getSMScode(username,password,cellphone):
        els_array = [signUp.username, signUp.password, signUp.cellphone, signUp.sendSMScode]
        data = [username,password,cellphone]
        kw.submitData(els_array,data)

    #输入验证码(注册页面)
    def inputSMScode(smscode):
        els_array = [signUp.smsCode,signUp.signupbtn]
        kw.submitData(els_array,smscode)

    #显示等待
    def sleep(sleep_time):
        time.sleep(sleep_time)

    #切换菜单栏
    def switchMenu(menu_name):
        kw.click(Homepage.avator)
        if menu_name == 'mainpage':
            kw.click(Homepage.mainpage)
        elif menu_name == 'siteManagement':
            kw.click(Homepage.siteManagement)
        elif menu_name == 'pageEditor':
            kw.click(Homepage.pageEditor)
        elif menu_name == 'skyDriver':
            kw.click(Homepage.skyDriver)
        elif menu_name == 'setupCenter':
            kw.click(Homepage.setupCenter)
        elif menu_name == 'VIP':
            kw.click(Homepage.vipenter)

    #手机绑定页面
    def bindpage(smscode):
        els_array = [setupCenter.security_bindTab_mobile_piccodetext,setupCenter.security_bindTab_mobile_sendSMSbtn]
        kw.click(setupCenter.security_bindTab_mobile_picrefresh)    #防止图片验证码没有刷新出来的情况
        imgcode = kw.getAttributeValues(setupCenter.security_bindTab_mobile_imageCode,'src')
        kw.submitData(els_array,str(imgcode).split('?')[-1])
        locs = [setupCenter.security_bindTab_mobile_smscode,setupCenter.security_bindTab_mobile_Confirmbtn]
        kw.submitData(locs,smscode)

    #对模板进行预览
    def tmppreview(type,template,preview_btn):
        kw.click(type)
        kw.click(template)
        kw.click(preview_btn)
    #根据选择的模板创建网站
    def createsite_By_temp(type,tmp,sitename):
        kw.click(type)
        kw.click(tmp)
        kw.click(templatepage.domain_next)
        kw.inputData(templatepage.domain_sitename,sitename)
        kw.click(templatepage.domain_next)
        time.sleep(2)
        kw.click(templatepage.domain_next)

    #获取当前网站总数
    def getSitesNum():
        siteNum = kw.getElementText(mysite.siteNum)
        return siteNum

    #获取网站的所有信息(默认取前5条)
    def getWebsitesInfo(num=5):
        info = []
        for i in range(num):
            sitename = kw.getElementText((By.CSS_SELECTOR, "div.flex-table > div:nth-child(" + (i + 3) + ") > div:nth-child(1)"))
            address = kw.getElementText((By.CSS_SELECTOR, "div.flex-table > div:nth-child(" + (i + 3) + ") > div:nth-child(2)"))
            dates = kw.getElementText((By.CSS_SELECTOR, "div.flex-table > div:nth-child(" + (i + 3) + ") > div:nth-child(3)"))
            subinfo = {"sitename":sitename,"address":address,"dates":dates}
            info.append(subinfo)
        return info

    #获取私有网站的数量和信息
    def getPrivatesite(num):
        private_sign = 0
        private_info = []
        for i in range(num):
            loc = "div.flex-table > div:nth-child(" + (i + 3) + ") > div:nth-child(1) > span[class=\\'iconfont icon-lock\\']"
            script = "var els=document.querySelectorAll('" + loc + "');" \
                    + "return els;"
            res = kw.execScript(script)
            sitename = kw.getElementText(
                (By.CSS_SELECTOR, "div.flex-table > div:nth-child(" + (i + 3) + ") > div:nth-child(1)"))
            if(res.length > 0):
                private_sign = private_sign + 1
                private_info.append(sitename)

        All_info = {"num":private_sign ,"details":private_info}
        return All_info

    #删除网站
    def delwebsite(locator,options="confirm"):
        kw.click(locator)
        kw.getElementText(mysite.operation_remove_delWindowTitle)
        kw.click(mysite.operation_remove_clearDataSource)
        if(options == "confirm"):
            kw.click(mysite.operation_remove_confirm_btn)
        else:
            kw.click(mysite.operation_remove_cancel_btn)