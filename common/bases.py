#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Duke
# Create Date: 2018/3/15


import time,traceback
import os,sys
from importlib import reload
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException


src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

class bases(object):    
    def __init__(self,driver):
        self.driver=driver

    #获取元素
    def getElements(self,locators):
        driver=self.driver               
        try:
            elements=[]            
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locators))         
            elements.append(element)            
            return elements            
        except (NoSuchElementException,TimeoutException):
            traceback.print_exc()
    
    #根据locator类型进行元素获取
    def getElementAndInfos(self,locators):        
        try:
            if isinstance(locators, tuple):
              elements=self.getElements(locators)
              return elements
            
            elif isinstance(locators, list):
              elements=[]
              for locate in locators:
                elements.extend(self.getElements(locate))
              return elements
                            
        except TypeError:            
            traceback.print_exc()

    #提交数据
    def submitData(self,locators,datas,sleep_time=2):
        self.inputData(locators[:-1], datas)
        time.sleep(sleep_time)        
        self.click(locators[-1])

    #执行输入操作(可一次输入多个)
    def inputData(self,locators,datas):
        try:
            elements=self.getElementAndInfos(locators)
            flag=isinstance(datas, str)
            flag1=isinstance(datas, list) 

            for index,element in enumerate(elements):
                if flag:
                    element.clear()
                    element.send_keys(datas)                    
                elif flag1:
                    element.clear()
                    element.send_keys(datas[index])
        except IndexError:
            traceback.print_exc()

    #执行点击操作
    def click(self,locators,sleep_time=1):
        elements=self.getElementAndInfos(locators)
        try:
            for element in elements:
                element.click()
                time.sleep(sleep_time)
        except Exception:
            traceback.print_exc()

    #获取当前页面URL地址
    def getCurrentUrl(self):
        try:
           page_url = self.driver.current_url
           return page_url
        except Exception:
            traceback.print_exc()


    #获取元素值
    def getElementText(self,locators):
        try:
            elements = self.getElementAndInfos(locators)
            for element in elements:
                text = element.get_attribute("innerText")
                return text
        except TypeError:
            traceback.print_exc()

    #获取元素属性值
    def getAttributeValues(self,locators,att):
        try:
            elements = self.getElementAndInfos(locators)
            if (len(elements) > 0):
                value = ''
                for element in elements:
                    value = element.get_attribute(att)
                return value
        except Exception :
            traceback.print_exc()

    #执行特定脚本(同步模式)
    def execScript(self,script):
        try:
            result = self.driver.execute_script(script)
            return result
        except Exception :
           traceback.print_exc()

    #根据locator获取元素值
    def getElstextByLocator(self,locators):
        try:
            script = "var els=document.querySelectorAll('" + locators + "');" \
                + "var elsTxt=[];" \
                + "for(let i=0;i<els.length;i++){" \
                + "var txt=els[i].innerText;" \
                + "elsTxt.push(txt);" \
                + "}" \
                + "return elsTxt;"
            print(script)
            res = self.execScript(script)
            return res
        except Exception :
            traceback.print_exc()

    #保持当前页面截图
    def saveScreenshot(self,filename):
        try:
            self.driver.save_screenshot(filename)
        except Exception :
            traceback.print_exc()

    #切换到新窗口页面
    def switchToNewWindow(self,switchwindow):
        try:
            all_windows = self.driver.window_handles
            for window in all_windows:
                if(window != switchwindow):
                    self.driver.switch_to_window(window)
        except Exception:
            traceback.print_exc()

    #关闭当前窗口
    def closepage(self):
        self.driver.close()

    #返回默认窗口
    def backtoDefaultWindow(self,window):
        self.driver.switch_to_window(window)

    #切换到iFrame上去
    def switchToiFrame(self,iframe):
        self.driver.switch_to_frame(iframe)

    #返回主页面(从iFrame页面返回)
    def backtoDefaultPage(self):
        self.driver.switch_to_default_content()

    #页面返回操作
    def back(self):
        self.driver.back()

    def checkResult(self,type,autual_value,expect_value):
        try:
            if(type == 'equals'):
                print('autual_value' +str(autual_value) +'|||expect_value:' +expect_value)
                return self.equals(autual_value,expect_value)
            elif(type == 'not_equals'):
                return self.not_equals(autual_value,expect_value)
            elif(type == 'contains'):
                return self.contains(autual_value,expect_value)

        except Exception :
            traceback.print_exc()

    
     


