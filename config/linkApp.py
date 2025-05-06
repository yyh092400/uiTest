# -*- encoding=utf8 -*-
__author__ = "25033"
from airtest.core.api import *

class LinkApp:
    def  __init__(self,*args,**kwargs):
        #手机序列号：R8YY30G5M6F
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/R8YY30G5M6F?cap_method=JAVACAP&ori_method=ADBORI&touch_method=ADBTOUCH&",])