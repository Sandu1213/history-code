#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Duke
# Create Date: 2018/3/15

import unittest,os,sys
from importlib import reload
from common.common_func import common
from HtmlTestRunner import HTMLTestRunner

src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

def load_all_testSuite():
    TestSuite = unittest.TestSuite()
    testcase_file_path = os.path.abspath('testcase')
    #print(testcase_file_path);
    discover = unittest.defaultTestLoader.discover(testcase_file_path, pattern="*_test.py", top_level_dir=None)
    for test_suite in discover: 
        TestSuite.addTests(test_suite)              
    print(TestSuite)                
    return TestSuite


def runSuite(suite):
    report_path = os.path.join(os.getcwd(),u'report\%s'%(common.get_current_date()))
    #print(report_path);
    print("----------------------------------");
    common.create_dir(report_path)      
    runner = HTMLTestRunner(output = report_path)    
    runner.run(suite)   
    









