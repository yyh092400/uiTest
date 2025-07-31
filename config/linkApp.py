# -*- encoding=utf8 -*-
__author__ = "25033"

import logging
import warnings


from airtest.core.api import *
from airtest.report.report import simple_report


class LinkApp:
    def  __init__(self,*args,**kwargs):
        logging.getLogger("airtest").setLevel(logging.ERROR)
        # 忽略特定警告（可选）
        warnings.filterwarnings("ignore", message=".*Currently using ADB screenshots.*")
        #手机序列号：R8YY30G5M6F
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/R8YY30G5M6F?cap_method=JAVACAP&ori_method=ADBORI&touch_method=ADBTOUCH&",])

