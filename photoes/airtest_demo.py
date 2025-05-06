# -*- encoding=utf8 -*-
__author__ = "25033"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/R8YY30G5M6F?cap_method=ADBCAP&touch_method=MAXTOUCH&",])


# script content
print("start...")


touch(Template(r"tpl1745741249264.png", record_pos=(0.003, 0.986), resolution=(1080, 2400)))poco(text="折扣").click()poco("com.wemew.teapro:id/default_title_back").click()
poco(text="优惠券").swipe([0.0, -0.0016])
poco(text="优惠券").click()


poco(text="会员信息").click()

poco("com.wemew.teapro:id/tv_search").click()

poco("android.widget.FrameLayout").offspring("com.wemew.teapro:id/cl_top_select").offspring("com.wemew.teapro:id/fl_coupon_container").offspring("com.wemew.teapro:id/recycler_view").child("android.widget.FrameLayout")[0].offspring("com.wemew.teapro:id/iv_select").click()

touch(Template(r"tpl1745742985563.png", record_pos=(-0.311, -0.982), resolution=(1080, 2400)))

touch(Template(r"tpl1745741509846.png", record_pos=(0.206, 0.946), resolution=(1080, 2400)))


poco(text="移动支付").click()
poco(text="会员支付").click()touch(Template(r"tpl1745747890035.png", record_pos=(0.003, 0.988), resolution=(1080, 2400)))


poco("com.wemew.teapro:id/tv_login_msg").click()
touch(Template(r"tpl1745743830688.png", record_pos=(-0.197, 0.149), resolution=(1080, 2400)))
touch(Template(r"tpl1745747116510.png", record_pos=(-0.231, 0.807), resolution=(1080, 2400)))
touch(Template(r"tpl1745747807657.png", record_pos=(0.001, 0.994), resolution=(1080, 2400)))
touch(Template(r"tpl1745747791703.png", record_pos=(-0.323, 0.994), resolution=(1080, 2400)))
touch(Template(r"tpl1745747122534.png", record_pos=(-0.345, 1.016), resolution=(1080, 2400)))
touch(Template(r"tpl1745747097220.png", record_pos=(0.247, 0.816), resolution=(1080, 2400)))
touch(Template(r"tpl1745747062893.png", record_pos=(0.229, 0.866), resolution=(1080, 2400)))
touch(Template(r"tpl1745743835476.png", record_pos=(0.197, 0.148), resolution=(1080, 2400)))



poco(text="点单二维码").click()
poco(text="会员信息").click()
poco(text="订单信息").click()

poco("com.wemew.teapro:id/tv_car_title").click()
poco("com.wemew.teapro:id/tv_pay_title").click()
poco("com.wemew.teapro:id/tv_not_pay_title").click()

touch(Template(r"tpl1745748757485.png", record_pos=(0.005, 0.99), resolution=(1080, 2400)))
touch(Template(r"tpl1745748662436.png", record_pos=(-0.313, 0.988), resolution=(1080, 2400)))
touch(Template(r"tpl1745748605107.png", record_pos=(-0.004, 0.987), resolution=(1080, 2400)))
touch(Template(r"tpl1745748594888.png", record_pos=(0.315, 0.986), resolution=(1080, 2400)))

poco("com.wemew.teapro:id/ll_red_block_root").click()
poco("android.widget.FrameLayout").offspring("com.wemew.teapro:id/fl_background").child("android.widget.LinearLayout").offspring("android.widget.ImageView").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.wemew.teapro:id/fm_anim")[1].offspring("com.wemew.teapro:id/recycler_view").child("android.widget.LinearLayout")[0].offspring("android.widget.RelativeLayout").child("android.widget.LinearLayout").offspring("com.wemew.teapro:id/iv_increase").click()

touch(Template(r"tpl1745749084244.png", record_pos=(0.306, 0.974), resolution=(1080, 2400)))
touch(Template(r"tpl1745749309630.png", record_pos=(0.044, 0.262), resolution=(1080, 2400)))
touch(Template(r"tpl1745749283330.png", record_pos=(-0.001, 0.981), resolution=(1080, 2400)))
touch(Template(r"tpl1745749230096.png", record_pos=(0.244, 0.984), resolution=(1080, 2400)))
poco("com.wemew.teapro:id/default_title_back").click()
poco(text="存酒审核").click()

poco(text="接订").click()

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.wemew.teapro:id/app_bar_main").offspring("com.wemew.teapro:id/view_pager").offspring("com.wemew.teapro:id/viewPager").child("android.widget.FrameLayout").offspring("com.wemew.teapro:id/fm_anim").offspring("com.wemew.teapro:id/recycler_view").child("android.widget.LinearLayout")[0].offspring("android.widget.RelativeLayout").offspring("com.wemew.teapro:id/iv_increase").click()
touch(Template(r"tpl1745749825701.png", record_pos=(0.199, 0.152), resolution=(1080, 2400)))
touch(Template(r"tpl1745749812080.png", record_pos=(0.071, 0.366), resolution=(1080, 2400)))
touch(Template(r"tpl1745749795806.png", record_pos=(0.319, 0.369), resolution=(1080, 2400)))
touch(Template(r"tpl1745749779514.png", record_pos=(-0.18, 0.368), resolution=(1080, 2400)))
touch(Template(r"tpl1745749686033.png", record_pos=(0.003, 0.896), resolution=(1080, 2400)))touch(Template(r"tpl1745750164049.png", record_pos=(0.251, -0.864), resolution=(1080, 2400)))

touch(Template(r"tpl1745749671071.png", record_pos=(0.165, 0.706), resolution=(1080, 2400)))

poco("com.wemew.teapro:id/default_title_back").click()

poco("com.wemew.teapro:id/r_community").click()
poco("com.wemew.teapro:id/r_vv_order").click()
poco("com.wemew.teapro:id/r_home").click()
poco("com.wemew.teapro:id/r_community").swipe([0.0, -0.0016])
poco("com.wemew.teapro:id/r_leave").click()
poco("com.wemew.teapro:id/r_community").click()
poco("com.wemew.teapro:id/r_leave").click()
poco("com.wemew.teapro:id/r_mine").click()


touch(Template(r"tpl1745750109910.png", record_pos=(0.005, 0.981), resolution=(1080, 2400)))
touch(Template(r"tpl1745750093316.png", record_pos=(0.185, 0.774), resolution=(1080, 2400)))
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.wemew.teapro:id/app_bar_main").offspring("com.wemew.teapro:id/view_pager").offspring("com.wemew.teapro:id/viewPager").child("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").child("com.wemew.teapro:id/recycler_view").child("android.widget.FrameLayout")[0].child("com.wemew.teapro:id/root_start").offspring("com.wemew.teapro:id/check_box").click()

touch(Template(r"tpl1745750145099.png", record_pos=(-0.249, -0.862), resolution=(1080, 2400)))



touch(Template(r"tpl1745750408558.png", record_pos=(-0.099, -0.644), resolution=(1080, 2400)))
touch(Template(r"tpl1745750392825.png", record_pos=(-0.177, 0.41), resolution=(1080, 2400)))
touch(Template(r"tpl1745750431032.png", record_pos=(0.194, 0.154), resolution=(1080, 2400)))
touch(Template(r"tpl1745750422268.png", record_pos=(0.325, 0.416), resolution=(1080, 2400)))
touch(Template(r"tpl1745750413742.png", record_pos=(0.075, 0.414), resolution=(1080, 2400)))

poco("com.wemew.teapro:id/default_title_back").click()

poco("com.wemew.teapro:id/iv_add").click()
touch(Template(r"tpl1745830372202.png", record_pos=(0.4, -0.044), resolution=(1080, 2400)))
touch(Template(r"tpl1745830351756.png", record_pos=(0.396, 0.297), resolution=(1080, 2400)))poco("com.wemew.teapro:id/drawer_layout").swipe([-0.3557, 0.0122])

touch(Template(r"tpl1745830326659.png", record_pos=(0.403, -0.043), resolution=(1080, 2400)))
touch(Template(r"tpl1745750787289.png", record_pos=(0.225, 0.996), resolution=(1080, 2400)))
poco("com.wemew.teapro:id/tv_print").click()
poco("com.wemew.teapro:id/tv_recharge1").click()








poco(text="会员信息").click()poco("android.widget.FrameLayout").offspring("android.view.ViewGroup").offspring("android.widget.ScrollView").offspring("com.wemew.teapro:id/recycler_view").child("android.widget.FrameLayout")[1].offspring("com.wemew.teapro:id/recycler_view_goods").child("android.widget.LinearLayout")[1].child("android.widget.LinearLayout").offspring("com.wemew.teapro:id/iv_add")

poco("android.widget.FrameLayout").offspring("android.view.ViewGroup").offspring("android.widget.ScrollView").offspring("com.wemew.teapro:id/recycler_view").child("android.widget.FrameLayout")[1].offspring("com.wemew.teapro:id/recycler_view_goods").child("android.widget.LinearLayout")[1].child("android.widget.LinearLayout").offspring("com.wemew.teapro:id/iv_add")

poco("android.widget.FrameLayout").offspring("android.view.ViewGroup").offspring("android.widget.ScrollView").offspring("com.wemew.teapro:id/recycler_view").child("android.widget.FrameLayout")[1].offspring("com.wemew.teapro:id/recycler_view_goods").child("android.widget.LinearLayout")[1].child("android.widget.LinearLayout").offspring("com.wemew.teapro:id/iv_add").click()


touch(Template(r"tpl1745834140586.png", record_pos=(-0.086, 0.998), resolution=(1080, 2400)))

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.wemew.teapro:id/app_bar_main").offspring("com.wemew.teapro:id/view_pager").offspring("com.wemew.teapro:id/viewPager").child("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").child("com.wemew.teapro:id/recycler_view").child("android.widget.FrameLayout")[0].child("com.wemew.teapro:id/root_start").offspring("com.wemew.teapro:id/check_box").click()

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.wemew.teapro:id/app_bar_main").offspring("com.wemew.teapro:id/view_pager").offspring("com.wemew.teapro:id/viewPager").child("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").child("com.wemew.teapro:id/recycler_view").child("android.widget.FrameLayout")[0].child("com.wemew.teapro:id/root_start").offspring("com.wemew.teapro:id/check_box").click()


poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.wemew.teapro:id/fl_cover").offspring("android.widget.ImageView").click()

poco("androidx.recyclerview.widget.RecyclerView").swipe([0.6013, 0.0116])
poco("androidx.recyclerview.widget.RecyclerView").swipe([0.6913, 0.0014])
poco("androidx.recyclerview.widget.RecyclerView").swipe([-0.6399, -0.0203])
poco("androidx.recyclerview.widget.RecyclerView").swipe([-0.8296, -0.0116])
poco("androidx.recyclerview.widget.RecyclerView").swipe([0.8521, 0.0058])
poco("androidx.recyclerview.widget.RecyclerView").swipe([0.8039, -0.0014])
poco("androidx.recyclerview.widget.RecyclerView").swipe([0.7203, 0.0043])


