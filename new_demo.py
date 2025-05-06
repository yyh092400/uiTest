# -*- encoding=utf8 -*-
__author__ = "25033"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/R8YY30G5M6F?cap_method=ADBCAP&touch_method=MAXTOUCH&",])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

touch(Template(r"tpl1745738264181.png", record_pos=(-0.227, 0.835), resolution=(1080, 2400)))


touch(Template(r"tpl1745738409715.png", record_pos=(-0.221, 0.776), resolution=(1080, 2400)))
touch(Template(r"tpl1745738661614.png", record_pos=(0.401, -0.386), resolution=(1080, 2400)))

poco("android.widget.FrameLayout").offspring("android.view.ViewGroup").offspring("android.widget.ScrollView").offspring("com.wemew.teapro:id/recycler_view").child("android.widget.FrameLayout")[1].offspring("com.wemew.teapro:id/recycler_view_goods").child("android.widget.LinearLayout")[1].child("android.widget.LinearLayout").offspring("com.wemew.teapro:id/iv_add").click()


touch(Template(r"tpl1745739374286.png", record_pos=(0.305, 0.768), resolution=(1080, 2400)))
touch(Template(r"tpl1745739334191.png", record_pos=(0.403, 0.3), resolution=(1080, 2400)))
touch(Template(r"tpl1745739236740.png", record_pos=(-0.08, 0.911), resolution=(1080, 2400)))
touch(Template(r"tpl1745739395608.png", record_pos=(0.301, 0.768), resolution=(1080, 2400)))

poco("com.wemew.teapro:id/tv_next").click()
touch(Template(r"tpl1745739567634.png", record_pos=(0.308, 0.881), resolution=(1080, 2400)))
touch(Template(r"tpl1745739495179.png", record_pos=(-0.003, 0.89), resolution=(1080, 2400)))
poco("com.wemew.teapro:id/iv_increase").click()

touch(Template(r"tpl1745739697802.png", record_pos=(0.321, 0.91), resolution=(1080, 2400)))
poco(text="auto支付").click()

poco(text="auto支付").click()
touch(Template(r"tpl1745740090259.png", record_pos=(0.232, 0.776), resolution=(1080, 2400)))
touch(Template(r"tpl1745740039111.png", record_pos=(0.008, 0.902), resolution=(1080, 2400)))
