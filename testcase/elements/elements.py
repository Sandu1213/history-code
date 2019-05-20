#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Duke
# Create Date: 2018/3/15
from selenium.webdriver.common.by import By


class Homepage(object):
    username = (By.NAME, "username")
    password = (By.CSS_SELECTOR, "input[ng-model='password']")
    login = (By.CSS_SELECTOR, "a[ng-click*='login()']")
    signinbtn = (By.CSS_SELECTOR, "a[ng-click*='goLoginPage()']")
    signupbtn = (By.CSS_SELECTOR, "a[ng-click*='goRegisterPage()']")
    avator = (By.CSS_SELECTOR, "a.dropdown-toggle.profile")
    exit = (By.CSS_SELECTOR, "a[ng-click*='logout()']")
    mainpage = (By.CSS_SELECTOR, "a.ng-scope[translate='我的主页']")
    siteManagement = (By.CSS_SELECTOR, "a[ng-click*='websiteManager']")
    pageEditor = (By.CSS_SELECTOR, "a[ng-click*='goWikiEditorPage()']")
    setupCenter = (By.CSS_SELECTOR, "a[ng-click*='userProfile']")
    skyDriver = (By.CSS_SELECTOR, "a[ng-click*='qiniuPan']")
    vipenter = (By.CSS_SELECTOR, "a[ng-click*='myVIP']")
    checktext = (By.ID, "total-err")


class personalpage(object):
    newwebsite_enter = (By.CSS_SELECTOR, "a.item[href$='newWebsite']")
    siteManagement_enter = (By.CSS_SELECTOR, "a.item[href*='websiteManager']")
    editer_enter = (By.CSS_SELECTOR, "a.item[href*='wikieditor']")


class realNamepage(object):
    title = (By.CSS_SELECTOR, "h4[translate='实名手机认证']")
    cellphone = (By.CSS_SELECTOR, "input[ng-model='realNameInfo.cellphone']")
    smscode = (By.CSS_SELECTOR, "input[ng-model='realNameInfo.SMSCode']")
    sendcode = (By.CSS_SELECTOR, "div[ng-click='sendRealNameCellPhoneSMSCode()']")
    submit_btn = (By.CSS_SELECTOR, "button[ng-click*='submitRealnameInfo()']")
    cancel_btn = (By.CSS_SELECTOR, "button.btn.btn-md.ng-scope[ng-click='cancel()']")


class templatepage(object):
    # 个人
    personal_key = (By.CSS_SELECTOR,
                    "#userCenterSubPage > div > div.col-md-10.main-content > div.panel-body > div.step-content.clearfix > div:nth-child(1) > div > ul > li:nth-child(1) > a")
    # 空模板
    personal_blank_main = (By.CSS_SELECTOR, "img[ng-src$='wiki_blank_template.png']")
    personal_blank_preview = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[1]")
    personal_blank_select = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[2]")
    personal_blank_previewcheck = (By.CSS_SELECTOR, "div#_mdwiki_content_container_mdwiki_0")
    # 基础模板
    personal_basic_main = (By.CSS_SELECTOR, "img[ng-src$='wiki_basic_template.png']")
    personal_basic_preview = (By.XPATH, "//*[@id='personal-web']/div[2]/div/div[1]")
    personal_basic_select = (By.XPATH, "//*[@id='personal-web']/div[2]/div/div[2]")
    personal_basic_previewcheck = (By.CSS_SELECTOR, "div.wiki_page_inner_link.ng-scope > h2")
    # 简历模板
    personal_resume_main = (By.CSS_SELECTOR, "img[ng-src$='wiki_resume_site_template.png']")
    personal_resume_preview = (By.XPATH, "//*[@id='personal-web']/div[3]/div/div[1]")
    personal_resume_select = (By.XPATH, "//*[@id='personal-web']/div[3]/div/div[2]")
    personal_resume_previewcheck = (By.CSS_SELECTOR, "#wikiblock_mdwiki_0_0_1 > div > div:nth-child(1) > div:nth-child(1) > h3")
    # vip模板
    personal_vip_main = (By.CSS_SELECTOR, "img[ng-src*='wiki_basic_template.png']")
    personal_vip_preview = (By.XPATH, "//*[@id='personal-web']/div[4]/div/div[1]")
    personal_vip_select = (By.XPATH, "//*[@id='personal-web']/div[4]/div/div[2]")
    personal_vip_previewcheck = (By.CSS_SELECTOR, "div#_mdwiki_content_container_mdwiki_0")

    # 企业
    company_key = (By.CSS_SELECTOR,
                   "#userCenterSubPage > div > div.col-md-10.main-content > div.panel-body > div.step-content.clearfix > div:nth-child(1) > div > ul > li:nth-child(2) > a")
    # 企业模板1
    company_1_main = (By.CSS_SELECTOR, "img[ng-src$='wiki_company1_template.jpg']")
    company_1_preview = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[1]")
    company_1_select = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[2]")
    company_1_previewcheck = (By.CSS_SELECTOR, " div > div.sidebar.pull-left > p")
    # 企业模板2
    company_2_main = (By.CSS_SELECTOR, "img[ng-src$='wiki_company2_template.png']")
    company_2_preview = (By.XPATH, "//*[@id='personal-web']/div[2]/div/div[1]")
    company_2_select = (By.XPATH, "//*[@id='personal-web']/div[2]/div/div[2]")
    company_2_previewcheck = (By.CSS_SELECTOR, "#wikiblock_mdwiki_0_0_2 > div > div > div:nth-child(1) > h2 > span")

    # 组织
    group_key = (By.CSS_SELECTOR,
                 "#userCenterSubPage > div > div.col-md-10.main-content > div.panel-body > div.step-content.clearfix > div:nth-child(1) > div > ul > li:nth-child(3) > a")
    # 组织模板
    group_main = (By.CSS_SELECTOR, "img[ng-src$='wiki_organization_template.png']")
    group_preview = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[1]")
    group_select = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[2]")
    group_previewcheck = (By.CSS_SELECTOR, "div.user-msg > h1")

    # 比赛
    game_key = (By.CSS_SELECTOR,
                "#userCenterSubPage > div > div.col-md-10.main-content > div.panel-body > div.step-content.clearfix > div:nth-child(1) > div > ul > li:nth-child(4) > a")
    # 比赛模板
    game_main = (By.CSS_SELECTOR, "img[ng-src$='wiki_game_template.jpg']")
    game_preview = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[1]")
    game_select = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[2]")
    game_previewcheck = (By.CSS_SELECTOR, "#wikiblock_mdwiki_0_0_1 > div > div:nth-child(5) > div > div.banner-info > h1")
    # 课程
    course_key = (By.CSS_SELECTOR,
                  "#userCenterSubPage > div > div.col-md-10.main-content > div.panel-body > div.step-content.clearfix > div:nth-child(1) > div > ul > li:nth-child(5) > a")
    # 课程模板
    course_main = (By.CSS_SELECTOR, "img[ng-src$='img_1509532234890.png']")
    course_preview = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[1]")
    course_select = (By.XPATH, "//*[@id='personal-web']/div[1]/div/div[2]")
    course_daofeng_iframe = (By.CSS_SELECTOR, "iframe#addcourse")
    course_daofeng_login = (By.CSS_SELECTOR, "body > div > div.login-box > a")
    course_daofeng_agree_btn = (By.CSS_SELECTOR, "div[ng-click*='agree']")
    course_daofeng_close_btn = (By.CSS_SELECTOR, "span.rightform_head_close")

    course_daofeng_checksuccess = (By.CSS_SELECTOR, "a.logo[href*='lecture']")
    course_daofeng_checksuccess1 = (By.CSS_SELECTOR, "body > md-toolbar > div > a:nth-child(4) > span")
    # 新建网站
    domain_next = (By.CSS_SELECTOR, "div.panel-body > div.step-footer > button:nth-child(2)")
    domain_sitename = (By.CSS_SELECTOR, "input#websiteName")
    domain_prestep = (By.CSS_SELECTOR, "div.panel-body > div.step-footer > button:nth-child(1)")
    domain_nextstep = (By.XPATH, "//*[@id='userCenterSubPage']/div/div[1]/div[2]/div[2]/button[2]")
    domain_checksuccess = (By.CSS_SELECTOR, "#userCenterSubPage > div > div.col-md-10.main-content > div.panel-body > div.step-content.clearfix > div.congratulation > h4")
    domain_gotoEditor1 = (By.CSS_SELECTOR, "div.panel-body > div.step-footer > button[ng-click='goEditerPage()']")
    domain_gotoConfig1 = (By.CSS_SELECTOR, "div.panel-body > div.step-footer > button[ng-click='goEditWebsitePage()']")


class mysite(object):
    key = (By.CSS_SELECTOR, "li:nth-child(2) > div > div.panel-body > ul > a")
    # 网站创建按钮
    create = (By.CSS_SELECTOR, "a[ng-click$='goNewWebsitePage()']")
    # 网站总数
    siteNum = (By.CSS_SELECTOR, "div.panel-body.website-flex > h3 > span > span")
    # 网站类型图标
    sitetype = "span[class='iconfont icon-lock']"
    siteName = (By.CSS_SELECTOR, "div.flex-table > div:nth-child(3) > div:nth-child(1)")
    siteAddress = (By.CSS_SELECTOR, "div.flex-table > div:nth-child(3) > div:nth-child(2)")
    createDate = (By.CSS_SELECTOR, "div.flex-table > div:nth-child(3) > div:nth-child(3)")
    # 访问图标
    operation_see = (By.CSS_SELECTOR, "div.flex-table > div:nth-child(3) > div:nth-child(4) > a:nth-child(1)")
    # 编辑图标
    operation_edit = (By.CSS_SELECTOR, "div.flex-table > div:nth-child(3) > div:nth-child(4) > a:nth-child(2)")
    # 网站设置
    operation_setup_key = (By.CSS_SELECTOR, "div.flex-table > div:nth-child(3) > div:nth-child(4) > a:nth-child(3)")
    # 网站常规设置
    operation_setup_common_icon_input = (By.CSS_SELECTOR, "input.change-btn")
    operation_setup_common_icon_edit_btn = (By.CSS_SELECTOR, "a.change-btn.ng-scope")
    operation_setup_common_icon_save_btn = (By.CSS_SELECTOR, "a#finish")
    operation_setup_common_sitename = (By.CSS_SELECTOR, "input#webName")
    operation_setup_common_siteAddress = (By.CSS_SELECTOR, "#common > div > div:nth-child(4) > div.col-sm-5 > p")
    operation_setup_common_siteintro = (By.CSS_SELECTOR, "#intro")
    operation_setup_common_notice = (By.CSS_SELECTOR, "#common > div > div > div > p.text-danger")
    operation_setup_common_savebtn = (
    By.CSS_SELECTOR, "#common > div > div > div > button[ng-click='modifyWebsite()']")
    operation_setup_common_saveResult = (By.CSS_SELECTOR, "div#messageTipConentId")
    # 网站数据源页面
    datasource_key = (By.CSS_SELECTOR, "a[href*= '#datasource']")
    datasource_data = (By.CSS_SELECTOR, "select[ng-model^='dataSourceName']")
    # 域名管理页面

    domainManage_key = (By.CSS_SELECTOR, "a[href^='#domain']")
    domainManage_webAddress = (By.CSS_SELECTOR, "#domain > form > div:nth-child(2) > div > p")
    domainManage_webdomain = (By.CSS_SELECTOR, "#domain > form > div:nth-child(3) > div > p")
    # cname统计情况
    domainManage_cname_summary = ''
    # cname输入框
    domainManage_cname_input = ''
    domainManage_cname_addbtn = ''
    domainManage_cname_notesinfo = (By.CSS_SELECTOR, "div[ng-hide='user.vipInfo.isValid']")
    domainManage_cname_becomevip = (By.CSS_SELECTOR, "div[ng-hide='user.vipInfo.isValid'] > a")
    # 权限管理
    Permissions_key = (By.CSS_SELECTOR, "a[href^='#permission']")
    Permissions_desc_address = (By.CSS_SELECTOR, "#permission > div.inner-info > h4")
    Permissions_desc_content1 = (By.CSS_SELECTOR, "#permission > div.inner-info > p:nth-child(2)")
    Permissions_desc_content2 = (By.CSS_SELECTOR, "#permission > div.inner-info > p:nth-child(3)")
    Permissions_desc_content3 = (By.CSS_SELECTOR, "#permission > div.inner-info > p:nth-child(4)")

    Permissions_siteType_warnning = (By.CSS_SELECTOR, "#permission > div.change-type > div > p:nth-child(1)")
    Permissions_siteType_becomevip = (By.CSS_SELECTOR, "#permission > div.change-type > div > p > a[href='/wiki/vip']")
    # 公有项目
    Permissions_siteType_public_select = (By.CSS_SELECTOR, "input#publicItem")
    Permissions_siteType_public_name = (By.CSS_SELECTOR, "label[for^='publicItem']")
    Permissions_siteType_public_desc = (By.CSS_SELECTOR, "#permission > div.change-type > div > div:nth-child(2) > p")
    # 私有项目
    Permissions_siteType_private_select = (By.CSS_SELECTOR, "input#privateItem")
    Permissions_siteType_private_name = (By.CSS_SELECTOR, "label[for^='privateItem']")
    Permissions_siteType_private_desc = (By.CSS_SELECTOR, "#permission > div.change-type > div > div:nth-child(3) > p")

    # 授权管理
    Permissions_Rights_key = (By.CSS_SELECTOR, "a[href^='#authorize']")
    Permissions_Rights_selectGroup = (
    By.CSS_SELECTOR, "#authorize > form > div:nth-child(2) > div > select ")  # 排序第一的分组
    Permissions_Rights_selectRight = (By.CSS_SELECTOR, "#authorize > form > div:nth-child(3) > div > select ")  # 浏览的权限
    Permissions_Rights_addbtn = (By.CSS_SELECTOR, "#authorize > form > div.col-sm-12.save-setting > button")
    # 具体列表情况
    Permissions_Rights_list_gname = (
    By.CSS_SELECTOR, "#authorize > table > tbody > tr:nth-child(2) > td:nth-child(1)")
    Permissions_Rights_list_gpermission = (
    By.CSS_SELECTOR, "#authorize > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    Permissions_Rights_list_del = (By.CSS_SELECTOR, "#authorize > table > tbody > tr:nth-child(2) > td:nth-child(3)")
    # 分组管理
    Permissions_group_key = (By.CSS_SELECTOR, "a[href^='#grouping']")
    Permissions_group_name = (By.CSS_SELECTOR, "input#groupName")
    Permissions_group_createbtn = (By.CSS_SELECTOR, "div[ng-click='createGroup()']")
    Permissions_group_inputmember = (By.CSS_SELECTOR, "input#groupUserName")
    Permissions_group_addbtn = (By.CSS_SELECTOR, "div[ng-click='addUser()']")
    Permissions_group_memberlist = (
    By.CSS_SELECTOR, "#grouping > form > div:nth-child(3) > div > div.col-sm-12.labels-box >div")
    Permissions_group_backbtn = (By.CSS_SELECTOR, "div[ng-click*='editGroup']")
    # 具体列表情况
    Permissions_group_list_gname = (By.CSS_SELECTOR, "#grouping > table > tbody > tr:nth-child(1) > td:nth-child(1)")
    Permissions_group_list_gmember = (
    By.CSS_SELECTOR, "#grouping > table > tbody > tr:nth-child(1) > td:nth-child(2)")
    Permissions_group_list_edit = (
    By.CSS_SELECTOR, "#grouping > table > tbody > tr:nth-child(1) > td:nth-child(3)>a:nth-child(1)")  # 针对第一个分组
    Permissions_group_list_del = (
    By.CSS_SELECTOR, "#grouping > table > tbody > tr:nth-child(1) > td:nth-child(3)>a:nth-child(2)")

    # 网站删除操作
    operation_remove_key = (By.CSS_SELECTOR, "div.flex-table > div:nth-child(3) > div:nth-child(4) > a:nth-child(4)")
    operation_remove_delWindowTitle = (By.CSS_SELECTOR, "h4#deleteWebsiteConfirmModalLabel")
    operation_remove_clearDataSource = (By.CSS_SELECTOR, "input[ng-model^='delete']")
    operation_remove_confirm_btn = (By.CSS_SELECTOR, "button[ng-click^='confirm']")
    operation_remove_cancel_btn = (By.CSS_SELECTOR, "button.btn.btn-default.ng-binding[data-dismiss^='mod']")

    # 编辑器页面
    editor_editArea_loc = (By.CSS_SELECTOR, "div.CodeMirror-code > div:nth-child(1) > pre.CodeMirror-line")
    editor_editArea_splitTableft = (By.CSS_SELECTOR, "div.CodeMirror-code > div:nth-child(1) > pre > span")
    editor_editArea_saveBtn = (By.CSS_SELECTOR, "#codeToolbar > div:nth-child(2) > div:nth-child(1)")
    editor_editArea_saveSuccess = (By.CSS_SELECTOR, "div#messageTipId.alert > div#messageTipConentId")
    editor_editArea_backtoPersonalpage = (By.CSS_SELECTOR, "#codeToolbar > div.btn-group.brand-btn-group > a")

    # 校验
    site_checkpage_first = (By.CSS_SELECTOR, "div#_mdwiki_content_container_mdwiki_0")
    site_checkpage_second = (By.CSS_SELECTOR, "div#_mdwiki_content_container_mdwiki_0 > div > p")


class setupCenter(object):
    # 我的资料页面
    myprofile_key = (By.CSS_SELECTOR,
                     "#__UserSitePageContent__ > div > div > div.col-md-2.subnav.col-sm-3 > ul > li:nth-child(1) > div > div.panel-body > ul > a:nth-child(1)")
    myprofile_title = (By.CSS_SELECTOR, "#userCenterSubPage > div > div:nth-child(1) > div.panel-heading.ng-scope")
    myprofile_inputavatar = (By.CSS_SELECTOR,
                             "#userCenterSubPage > div > div:nth-child(1) > div.panel-body > div.col-md-3.preview-zone > p > input[type='file']")
    myprofile_saveavatarbtn = (By.CSS_SELECTOR, "a#finish")
    myprofile_nickname = (By.CSS_SELECTOR, "input#displayName")

    myprofile_sex_male = (By.CSS_SELECTOR, "input#inlineRadio1")
    myprofile_sex_female = (By.CSS_SELECTOR, "input#inlineRadio2")
    myprofile_sex_secrecy = (By.CSS_SELECTOR, "input#inlineRadio3")

    myprofile_position = (By.CSS_SELECTOR, "input#location")
    myprofile_intro = (By.CSS_SELECTOR, "#data-form > div:nth-child(5) > div > textarea")
    myprofile_Savebtn = (By.CSS_SELECTOR, " button[ng-click*='saveProfile']")
    myprofile_saveResult = (By.CSS_SELECTOR, "div#messageTipConentId")
    myprofile_notice = (By.CSS_SELECTOR, "#data-form > div:nth-child(6) > div > p:nth-child(1)")
    myprofile_overPos = (By.CSS_SELECTOR, "#data-form > div:nth-child(6) > div > p:nth-child(2)")
    myprofile_overIntro = (By.CSS_SELECTOR, "#data-form > div:nth-child(6) > div > p:nth-child(3)")
    # 账户安全页面

    security_key = (By.CSS_SELECTOR,
                    "#__UserSitePageContent__ > div > div > div.col-md-2.subnav.col-sm-3 > ul > li:nth-child(1) > div > div.panel-body > ul > a:nth-child(2)")
    # 修改密码页面
    security_pwdTab_key = (By.CSS_SELECTOR, "a[href='#change']")
    security_pwdTab_oldpwd = (By.CSS_SELECTOR, "input#old")
    security_pwdTab_newpwd = (By.CSS_SELECTOR, "input#new")
    security_pwdTab_repeatpwd = (By.CSS_SELECTOR, "input#reNew")
    security_pwdTab_modifybtn = (By.CSS_SELECTOR, "button[ng-click='modifyPassword()']")

    # 账户绑定页面
    security_bindTab_key = (By.CSS_SELECTOR, "a[href^='#verify']")
    security_bindTab_email = (By.CSS_SELECTOR, "")
    security_bindTab_mobile_text = (By.CSS_SELECTOR, "input#phone")
    security_bindTab_mobile_unbindbtn = (
    By.CSS_SELECTOR, "#verify > form > div:nth-child(4) > div.col-sm-3 > div.btn.btn-block.btn-outline")
    security_bindTab_mobile_bindbtn = (
    By.CSS_SELECTOR, "#verify > form > div:nth-child(4) > div.col-sm-3 > div.btn.btn-block.btn-primary")
    security_bindTab_mobile_piccodetext = (By.CSS_SELECTOR, "input[ng-model*='imageCode']")
    security_bindTab_mobile_picrefresh = (By.CSS_SELECTOR, "span[ng-click$='ImageCode()']")
    security_bindTab_mobile_imageCode = (By.CSS_SELECTOR, "div.col-sm-3.captcha > img")
    security_bindTab_mobile_updatePic = (By.CSS_SELECTOR, "span[ng-click='refreshImageCode()']")
    security_bindTab_mobile_smscode = (By.CSS_SELECTOR, "input[ng-model='smsCode']")
    security_bindTab_mobile_sendSMSbtn = (By.CSS_SELECTOR, "div[ng-click$='bindPhone()']")
    security_bindTab_mobile_Confirmbtn = (By.CSS_SELECTOR, "button[ng-click$='confirmPhoneBind()']")
    # 校验
    Result = (By.CSS_SELECTOR, "div#messageTipConentId")


class purchaseVip(object):
    level_oneMonth = ''
    level_halfYear = ''
    level_oneYear = ''

    channel_wechat = (By.CSS_SELECTOR, "ul > li[ng-click*='wechat']")
    channel_alipay = (By.CSS_SELECTOR, "ul > li[ng-click*='alipay']")

    rechargeAccount = (By.CSS_SELECTOR, "div.pay-main-field > div:nth-child(1) > input")
    rechargeAmount = (By.CSS_SELECTOR, "div.pay-main-field > div:nth-child(2) > div > input")
    rechargeInfo = (By.CSS_SELECTOR, "div.pay-main-field > div.field-item.ng-scope > div")
    purchasebtn = (By.CSS_SELECTOR, "div[ng-click*='selectedVip']")
    rechargebtn = (By.CSS_SELECTOR, "div.field-item > input[ng-click*='recharge()']")


class signIn(object):
    username = (By.NAME, "email")
    password = (By.CSS_SELECTOR, "input[ng-model='password']")
    login = (By.CSS_SELECTOR, "a[ng-click*='login()']")
    checktext = (By.ID, "total-err")
    signsuccess = (By.CSS_SELECTOR, "a.dropdown-toggle.profile")


class signUp(object):
    username = (By.CSS_SELECTOR, "input[ng-model='username']")
    password = (By.CSS_SELECTOR, "input[ng-model='password']")
    cellphone = (By.CSS_SELECTOR, "input[ng-model$='phone']")
    smsCode = (By.CSS_SELECTOR, "input[ng-model$='smsCode']")
    sendSMScode = (By.CSS_SELECTOR, "div[ng-click$='sendSMSCode()']")
    policyinfo = (By.LINK_TEXT, "a[ng-click$='goLicense()']")
    signupbtn = (By.CSS_SELECTOR, "a[ng-click*='register()']")
    checktext = "div.form-group.text-danger.ng-binding"
    checkrepeatinfo = "#__UserSitePageContent__ > div > div > form > div:nth-child(1)"
    repeattext = "div.text-danger.ng-binding"
    success = (By.CSS_SELECTOR, "img[ng-src*='wiki_success.png']")
    backbtn = (By.CSS_SELECTOR, "div[ng-click='goBack()']")
    gotohome = (By.CSS_SELECTOR, "div[ng-click='goUserHome()']")
