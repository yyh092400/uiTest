# -*- encoding=utf8 -*-
__author__ = "25033"

import time

import pytest
from airtest.core.api import *
from pages.table_page import TablePage
from config.linkApp import LinkApp
import unittest

"""
to-do
增加断言  
1.图片元素是否存在断言
2.金额对比断言
3.每条用例  都操作空闲桌台  新增查询空闲桌台  每次取第一个
4.减少日志量  只抛出异常信息
"""


class TestCases(unittest.TestCase, LinkApp):

    # def __init__(self,*args,**kwargs):
    #     super(LinkApp,self).__init__(*args,**kwargs)  #调用LinkApp的初始化
    #     super(TestCases,self).__init__(*args,**kwargs)
    #     self.public = TablePage() #实例化共用方法
    #     # 打开app
    #     self.public.poco(text="微喵·虎斑").click()
    #     # 判断是否需要登陆
    #     self.public.public_login()
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # super(LinkApp, cls).setUpClass()  # 调用 LinkApp 的类初始化
        cls.public = TablePage()  # 实例化共用方法
        # 打开 app
        cls.public.poco(text="微喵·虎斑").click()
        # 判断是否需要登陆
        cls.public.public_login()

    @classmethod
    def tearDownClass(cls):
        # 关闭app
        # stop_app("com.wemew.teapro")
        pass
    @pytest.mark.order(1)
    def test_case_step1(self):
        """
        case1:开台-点单-选择单品套餐-直接买单支付-自定义支付-翻台
        :return:
        """
        #点击桌台
        self.public.public_click_table("9527")
        #开台
        self.public.public_oprate_table("开台")
        #点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        #加购商品套餐
        self.public.public_add_goods()
        #直接买单
        self.public.public_save_goods("3")
        #选择自定义支付方式
        time.sleep(1)
        self.public.public_pay_method("自定义支付")
        self.public.public_confirm_pay()
        #点击桌台
        self.public.public_click_table("9527")
        #翻台
        self.public.public_oprate_table("翻台")
        time.sleep(1)


    @pytest.mark.order(2)
    def test_case_step2(self):
        """
        case2:开台-点单-选择单品套餐-直接买单支付-会员支付-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 直接买单
        self.public.public_save_goods("3")
        #选择会员信息
        self.public.public_total_discount("会员信息")
        #选择会员支付
        self.public.public_pay_method("会员支付")
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")
        time.sleep(1)

    @pytest.mark.order(3)
    def test_case_step3(self):
        """
        开台-点单-选择单品套餐-挂单-会员支付-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        #挂单
        self.public.public_save_goods("2")
        # 点击桌台
        self.public.public_click_table("9527")
        #切换tab
        self.public.public_switch_tab("2")
        self.public.public_switch_tab("7")
        #去支付
        self.public.public_buy_pay("买单支付")
        #选择会员信息
        self.public.public_total_discount("会员信息")
        #选择会员支付
        self.public.public_pay_method("会员支付")
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")
        time.sleep(1)

    @pytest.mark.order(4)
    def test_case_step4(self):
        """
        开台-点单-选择单品套餐-加入购物车-会员支付-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 加入购物车
        self.public.public_save_goods("1")
        # 点击桌台
        self.public.public_click_table("9527")
        # 切换tab
        self.public.public_switch_tab("2")
        self.public.public_switch_tab("5")
        # 去支付
        self.public.public_buy_pay("买单支付")
        # 选择会员信息
        self.public.public_total_discount("会员信息")
        # 选择会员支付
        self.public.public_pay_method("会员支付")
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")
        time.sleep(1)

    @pytest.mark.order(5)
    def test_case_step5(self):
        """
        开台-点单-选择单品套餐-加入购物车-挂单-会员支付-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 加入购物车
        self.public.public_save_goods("1")
        # 点击桌台
        self.public.public_click_table("9527")
        # 切换tab
        self.public.public_switch_tab("2")
        self.public.public_switch_tab("5")
        #购物车里 挂单
        self.public.public_buy_pay("挂单")
        time.sleep(1)
        #切换到挂单界面 并去支付
        if "com.wemew.teapro:id/tv_send_maker":
            self.public.public_switch_tab("7")
        self.public.public_buy_pay("买单支付")
        # 选择会员信息
        self.public.public_total_discount("会员信息")
        # 选择会员支付
        self.public.public_pay_method("会员支付")
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")
        time.sleep(1)

    @pytest.mark.order(6)
    def test_case_step6(self):
        """
        开台-点单-选择单品-加入购物车-挂单-自定义支付-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 加入购物车
        self.public.public_save_goods("1")
        # 点击桌台
        self.public.public_click_table("9527")
        # 切换tab
        self.public.public_switch_tab("2")
        self.public.public_switch_tab("5")
        # 购物车里 挂单
        self.public.public_buy_pay("挂单")
        time.sleep(1)
        # 切换到挂单界面 并去支付
        if "com.wemew.teapro:id/tv_send_maker":
            self.public.public_switch_tab("7")
        self.public.public_buy_pay("买单支付")
        time.sleep(1)
        # 选择自定义支付
        self.public.public_pay_method("自定义支付")
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")
        time.sleep(1)

    @pytest.mark.order(7)
    def test_case_step7(self):
        """
        开台-点单-选择单品-加入购物车-挂单-组合支付-翻台(自定义支付+会员支付）
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 加入购物车
        self.public.public_save_goods("1")
        # 点击桌台
        self.public.public_click_table("9527")
        # 切换到购物车界面
        self.public.public_switch_tab("2")
        self.public.public_switch_tab("5")
        # 购物车里 挂单
        self.public.public_buy_pay(pay_type="挂单")
        time.sleep(1)
        # 切换到挂单界面 并去支付
        if "com.wemew.teapro:id/tv_send_maker":
            self.public.public_switch_tab("7")
        self.public.public_buy_pay("买单支付")
        time.sleep(1)
        ## 选择会员信息
        self.public.public_total_discount("会员信息")
        time.sleep(1)
        # 选择会员支付
        self.public.public_pay_method("会员支付")
        # 选择自定义支付
        self.public.public_pay_method("自定义支付")
        time.sleep(1)
        #组合支付  输入金额
        touch((335,909))
        touch((302,1704))
        touch((525,2177))
        touch((960,2166))
        touch((1010,1556))
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")
        time.sleep(1)

    @pytest.mark.order(8)
    def test_case_step8(self):
        """
        开台-点单-选择单品-加入购物车-挂单-自定义支付-退品退款-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 加入购物车
        self.public.public_save_goods("1")
        # 点击桌台
        self.public.public_click_table("9527")
        # 切换到购物车界面
        self.public.public_switch_tab("2")
        self.public.public_switch_tab("5")
        # 购物车里 挂单
        self.public.public_buy_pay(pay_type="挂单")
        time.sleep(1)
        # 切换到挂单界面 并去支付
        if "com.wemew.teapro:id/tv_send_maker":   #
            self.public.public_switch_tab("7")
        self.public.public_buy_pay("买单支付")
        time.sleep(1)
        # 选择自定义支付
        self.public.public_pay_method("自定义支付")
        self.public.public_confirm_pay()
        ## 点击桌台
        self.public.public_click_table("9527")
        self.public.public_switch_tab("2")
        self.public.public_switch_tab("6")
        #退菜
        self.public.public_refund("已付款","1")
        #关闭桌台详情页
        self.public.public_close_tab()
        #翻台
        self.public.public_click_table("9527")
        self.public.public_oprate_table("翻台")

    @pytest.mark.order(9)
    def test_case_step9(self):
        """
        开台-赠送-选择单品-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台并赠送
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("赠送")
        time.sleep(2)
        #赠送-选择商品
        self.public.public_give_goods()
        #翻台
        self.public.public_oprate_table("翻台")

    @pytest.mark.order(10)
    def test_case_step10(self):
        """
        开台-兑换礼品券-翻台
        :return:
        """
        # # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        self.public.poco(text="9527").click()
        #滑动
        self.public.poco("com.wemew.teapro:id/cl_red_table_info").swipe([0.1034, -0.6719])
        time.sleep(1)
        #点击卡券核销
        self.public.public_oprate_table("卡券核销")
        self.public.public_use_coupon()
        self.public.public_oprate_table("翻台")

    @pytest.mark.order(11)
    def test_case_step11(self):
        """
        开台-点单-选择单品套餐-买单支付-选择优惠券-支付-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 直接买单
        self.public.public_save_goods("3")
        time.sleep(1)
        #选择优惠券
        self.public.public_total_discount("优惠券")
        # 选择自定义支付方式
        self.public.public_pay_method("自定义支付")
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")

    @pytest.mark.order(12)
    def test_case_step12(self):
        """
        开台-团购核销-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("团购核销")
        self.public.public_group_purchase()
        time.sleep(1)
        #切换到桌台信息tab页
        self.public.public_switch_tab("1")
        #翻台
        self.public.public_oprate_table("翻台")

    @pytest.mark.order(13)
    def test_case_step13(self):
        """
        预定-预定开台-点单-选择单品-买单支付-翻台
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        self.public.public_oprate_table("预订")
        time.sleep(1)
        self.public.public_book_table()
        self.public.public_click_table("9527")
        #预订开台
        self.public.public_oprate_table(method="开台",table_status="reserve",open_type="预订开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 直接买单
        self.public.public_save_goods("3")
        # 选择自定义支付方式
        self.public.public_pay_method("自定义支付")
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")

    @pytest.mark.order(14)
    def test_case_step14(self):
        """
        预定-取消预定
        :return:
        """
        # 点击桌台
        self.public.public_click_table("9527")
        self.public.public_oprate_table("预订")
        time.sleep(1)
        self.public.public_book_table()
        #接订
        self.public.public_click_menu("接订")
        #取消预订
        self.public.public_cancle_book_table()
        #刷新首页
        self.public.public_refresh_page()

    @pytest.mark.order(15)
    def test_case_step15(self):
        """
        存酒-存酒审核
        :return:
        """
        #切换到存取酒界面
        self.public.public_switch_menu("存取酒")
        self.public.public_switch_wine_tab("存酒")
        #存酒
        self.public.public_save_wine()
        #返回首页
        self.public.public_switch_menu("首页")
        #滑动页面到存酒审核
        self.public.public_swipe_menu("right")
        #点击存酒审核
        self.public.public_click_menu("存酒审核")
        #审核通过
        self.public.public_examine_wine("同意")
        #滑动回首页：打赏菜单页
        self.public.public_swipe_menu("left")

    @pytest.mark.order(16)
    def test_case_step16(self):
        """
        取酒-取酒审核
        :return:
        """
        # 切换到存取酒界面
        self.public.public_switch_menu("存取酒")
        self.public.public_switch_wine_tab("取酒")
        #取酒
        self.public.public_get_wine()
        #返回首页
        self.public.public_switch_menu("首页")
        #滑动到取酒审核界面
        self.public.public_swipe_menu("right")
        #点击取酒审核菜单
        self.public.public_click_menu("取酒审核")
        #审核通过
        self.public.public_get_wine_examine("通过")
        #滑动菜单回 首页
        self.public.public_swipe_menu("left")

    @pytest.mark.order(17)
    def test_case_step17(self):
        """
        新建会员-充值-点单消费-销卡
        :return:
        """
        #点击会员菜单
        self.public.public_click_menu("会员")
        time.sleep(1)
        #新增会员
        self.public.public_add_members()
        #搜索会员
        self.public.public_serch_member("19999999999")
        #进入会员详情页
        self.public.poco("com.wemew.teapro:id/tv_3").click()
        self.public.public_operate_member("充值")
        #会员充值
        self.public.public_member_recharge()
        #返回首页
        self.public.public_operate_member("返回")
        self.public.public_operate_member("返回")
        #点单并使用会员支付
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 直接买单
        self.public.public_save_goods("3")
        # 选择会员信息
        self.public.public_total_discount("会员信息",phone_num="19999999999")
        # 选择会员支付
        self.public.public_pay_method("会员支付")
        self.public.public_confirm_pay()
        # 点击桌台
        self.public.public_click_table("9527")
        # 翻台
        self.public.public_oprate_table("翻台")
        #进入会员
        self.public.public_click_menu("会员")
        # 搜索会员
        self.public.public_serch_member("19999999999")
        #进入详情页 并销卡
        self.public.poco("com.wemew.teapro:id/tv_3").click()
        self.public.public_operate_member("销卡")
        #返回首页
        self.public.public_operate_member("返回")
    @pytest.mark.order(18)
    def test_case_step18(self):
        """
        开台-点单-手动折扣-会员支付-翻台
        :return:
        """
        self.public.public_click_table("9527")
        # 开台
        self.public.public_oprate_table("开台")
        # 点击桌台
        self.public.poco(text="9527").click()
        self.public.public_oprate_table("点单")
        # 加购商品套餐
        self.public.public_add_goods()
        # 直接买单
        self.public.public_save_goods("3")
        #录入会员信息
        self.public.public_total_discount("会员信息")
        #手动折扣
        self.public.public_total_discount("折扣")
        #选择会员支付
        self.public.public_pay_method("会员支付")
        #确认收款
        self.public.public_confirm_pay()
        #翻台
        self.public.public_click_table("9527")
        self.public.public_oprate_table("翻台")
    def test_case_step19(self):
        """
        开台-点单-挂单-转台-自定义支付-翻台
        :return:
        """
        self.public.public_click_table("9527")
        self.public.public_oprate_table("开台")
        self.public.public_click_table("9527")
        self.public.public_oprate_table("点单")
        self.public.public_add_goods()
        #挂单
        self.public.public_save_goods("2")
        self.public.public_click_table("9527")
        # 滑动
        self.public.poco("com.wemew.teapro:id/cl_red_table_info").swipe([0.1034, -0.6719])
        #转台
        self.public.public_oprate_table("转台")
        self.public.public_turn_table(turn_type="转台",table_num="M2")
        #点击转台后的桌台
        self.public.public_click_table("M2[9527转]")
        #支付
        self.public.public_switch_tab("2")
        self.public.public_switch_tab("7")
        # 去支付
        self.public.public_buy_pay("买单支付")
        #自定义支付方式
        self.public.public_pay_method("自定义支付")
        self.public.public_confirm_pay()
        #翻台
        self.public.public_click_table("M2[9527转]")
        self.public.public_oprate_table("翻台")
    def test_case_step20(self):
        """
        打赏-自定义支付
        :return:
        """
        self.public.public_click_menu("打赏小费")
        self.public.public_reward()
    def test_case_step21(self):
        """
        打赏-组合支付
        :return:
        """
        self.public.public_click_menu("打赏小费")
        self.public.public_reward(pay_type="组合支付")
    def test_case_step22(self):
        """
        台票-充值-自定义支付
        :return:
        """
        for i in range(3):
            self.public.public_swipe_menu("right")
        time.sleep(1)
        self.public.public_click_menu("台票")
        self.public.public_taipiao()
    def test_case_step23(self):
        """
        台票-充值-组合支付
        :return:
        """
        self.public.public_click_menu("台票")
        self.public.public_taipiao(pay_type="组合支付")
    def test_case_step24(self):
        """
        台票-核销
        :return:
        """
        #开新的桌台
        self.public.public_click_table("9527")
        self.public.public_oprate_table("开台")
        self.public.public_click_menu("台票")
        self.public.public_taipiao_verify()
        self.public.public_click_table("9527")
        self.public.public_oprate_table("翻台")
    def test_case_step25(self):
        """
        排队-取号-叫号-入场-开台-点单-自定义支付-翻台
        :return:
        """
        self.public.public_click_menu("排队")
        #排队
        self.public.public_line_up()
        #断言

        #点单
        self.public.public_click_table("9527")
        self.public.public_oprate_table("点单")
        self.public.public_add_goods()
        self.public.public_save_goods("3")
        self.public.public_pay_method("自定义支付")
        self.public.public_confirm_pay()
        self.public.public_click_table("9527")
        self.public.public_oprate_table("翻台")






#
# ck = TestCases()


