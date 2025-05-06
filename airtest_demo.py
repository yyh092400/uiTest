# -*- encoding=utf8 -*-
__author__ = "25033"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/R58MB0TCZNR?cap_method=JAVACAP&ori_method=ADBORI&touch_method=ADBTOUCH&",])


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



poco(text="微喵·虎斑").click()
poco(text="微喵·虎斑").click()
