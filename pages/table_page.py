import time

from config.utils import Utils

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *


class TablePage:
    def __init__(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        self.utils = Utils()

    # 登陆
    def public_login(self):
        """
        登陆,判断是否需要登陆
        :return:
        """
        login_button = self.poco("com.wemew.teapro:id/tv_login_msg")
        if login_button:
            # 登陆
            self.poco("com.wemew.teapro:id/check_pwd").click()
            self.poco("com.wemew.teapro:id/et_account").set_text("18398939934")
            self.poco("com.wemew.teapro:id/et_pwd").set_text("1234567")
            self.poco("com.wemew.teapro:id/tv_login_msg").click()
        # 断言登陆是否成功
        self.utils.safe_assert_exist(
            Template(r"photoes/tpl1745742985563.png", record_pos=(-0.311, -0.982), resolution=(1080, 2400)),
            "账号密码登陆断言失败！")

    # 查询不同状态的桌台
    def public_query_table_status(self, status):
        """
        查询空闲桌台
        :param: status
        :return:
        """
        if status == "空闲":
            # 筛选空闲桌台
            self.poco("com.wemew.teapro:id/tv_table_state_empty").click()
            # 读取空闲桌台号
            table_num = self.poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
                "android:id/content").offspring(
                "com.wemew.teapro:id/app_bar_main").offspring("com.wemew.teapro:id/view_pager").child(
                "android.widget.FrameLayout").offspring(
                "com.wemew.teapro:id/recycler_view_tab").child("android.widget.FrameLayout")[0].offspring(
                "com.wemew.teapro:id/tv_tab_num").get_text()
            return table_num
        elif status == "全部区域":
            self.poco("com.wemew.teapro:id/tv_all_key").click()

    # 按桌台号查询桌台
    def public_query_table_by_num(self, table_num=None):
        """
        按桌台号搜索
        :param table_num:桌台号
        :return:
        """
        self.poco("com.wemew.teapro:id/et_search_table").set_text(table_num)
        self.poco("com.wemew.teapro:id/tv_search_table").click()

    def public_click_table_first(self):
        """
        点击第一张桌台
        """
        self.poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
            "android:id/content").offspring("com.wemew.teapro:id/app_bar_main").offspring(
            "com.wemew.teapro:id/view_pager").child("android.widget.FrameLayout").offspring(
            "com.wemew.teapro:id/recycler_view_tab").child("android.widget.FrameLayout")[0].offspring(
            "com.wemew.teapro:id/ll_grey_block_root").click()

    # 点击桌台
    def public_click_table(self, table_num):
        """
        点击桌台
        :param table_num:桌台号
        :return:
        """
        self.poco(text=table_num).click()

    # 操作桌台
    @staticmethod
    def public_oprate_table(method, table_status="normal", open_type=None):
        """
        桌台的基本操作，开台、翻台、点单等
        :return:
        """
        if method == "开台":
            if table_status == "normal":
                touch(Template(r"photoes/tpl1745738264181.png", record_pos=(-0.227, 0.835), resolution=(1080, 2400)))
            elif table_status == "reserve":
                touch(Template(r"photoes/tpl1745738264181.png", record_pos=(-0.239, 0.849), resolution=(1080, 2400)))
                if open_type == "普通开台":
                    touch(Template(r"photoes/tpl1745743830688.png", record_pos=(-0.197, 0.149),
                                   resolution=(1080, 2400)))
                elif open_type == "预订开台":
                    touch(Template(r"photoes/tpl1745743835476.png", record_pos=(0.197, 0.148),
                                   resolution=(1080, 2400)))
        elif method == "翻台":
            touch(Template(r"photoes/tpl1745740090259.png", record_pos=(0.232, 0.776), resolution=(1080, 2400)))
        elif method == "点单":
            touch(Template(r"photoes/tpl1745738409715.png", record_pos=(-0.221, 0.776), resolution=(1080, 2400)))
        elif method == "预订":
            touch(Template(r"photoes/tpl1745747062893.png", record_pos=(0.229, 0.866), resolution=(1080, 2400)))
        elif method == "锁台":
            pass
        elif method == "赠送":
            touch(Template(r"photoes/tpl1745747097220.png", record_pos=(0.247, 0.816), resolution=(1080, 2400)))
        elif method == "存酒":
            pass
        elif method == "取酒":
            pass
        elif method == "转台":
            pass
        elif method == "卡券核销":
            touch(Template(r"photoes/tpl1745747122534.png", record_pos=(-0.345, 1.016), resolution=(1080, 2400)))
        elif method == "团购核销":
            touch(Template(r"photoes/tpl1745747116510.png", record_pos=(-0.231, 0.807), resolution=(1080, 2400)))

    # 确认开台
    def public_confirm_open_table(self):
        """
        确认开台
        :return:
        """
        self.poco("com.wemew.teapro:id/tv_next").click()

    # 加购商品
    def public_add_goods(self):
        """
        选择商品+套餐
        :return:
        """
        # 开始选择商品套餐
        touch(Template(r"photoes/tpl1745738661614.png", record_pos=(0.401, -0.386), resolution=(1080, 2400)))
        wait(Template(r"photoes/tpl1743587579470.png", record_pos=(-0.028, 0.273), resolution=(1080, 2400)),
             timeout=5, interval=0.2)
        # 选择套餐
        touch(Template(r"photoes/tpl1743587579470.png", record_pos=(-0.028, 0.273), resolution=(1080, 2400)))
        # 添加任选商品
        for i in range(0, 4):
            # +号
            touch((640, 1900))
        # 套餐加入购物车
        touch(Template(r"photoes/tpl1745739236740.png", record_pos=(-0.08, 0.911), resolution=(1080, 2400)))
        # 单品流程
        touch(Template(r"photoes/tpl1745830372202.png", record_pos=(0.4, -0.044), resolution=(1080, 2400)))
        touch(Template(r"photoes/tpl1745739395608.png", record_pos=(0.301, 0.768), resolution=(1080, 2400)))
        self.poco("com.wemew.teapro:id/iv_increase").click()
        touch(Template(r"photoes/tpl1745739495179.png", record_pos=(-0.003, 0.89), resolution=(1080, 2400)))
        # 选好了  去结算
        touch(Template(r"photoes/tpl1745739567634.png", record_pos=(0.308, 0.881), resolution=(1080, 2400)))

    @staticmethod
    def public_save_goods(save_type):
        """
        1.保存购物车  2.挂单   3.买单支付
        :return:
        """
        time.sleep(1)
        if save_type == "1":
            touch(Template(r"photoes/tpl1745747791703.png", record_pos=(-0.323, 0.994), resolution=(1080, 2400)))
        elif save_type == "2":
            touch(Template(r"photoes/tpl1745747807657.png", record_pos=(0.001, 0.994), resolution=(1080, 2400)))
        elif save_type == "3":
            touch(Template(r"photoes/tpl1745739697802.png", record_pos=(0.321, 0.91), resolution=(1080, 2400)))
        else:
            print("保存购物车/挂单/买单支付失败，请输入正确的类型:", save_type)

    # 选择支付方式
    def public_pay_method(self, pay_method):
        """
        选择支付方式
        :param pay_method:string,移动支付/会员支付/自定义支付
        :return:
        """
        time.sleep(1)
        if pay_method == "移动支付":
            self.poco(text="移动支付").click()
        elif pay_method == "会员支付":
            self.poco(text="会员支付").click()
        elif pay_method == "自定义支付":
            self.poco(text="auto支付").click()
        else:
            print("请输入正确的支付方式:", pay_method)

    @staticmethod
    # 确认收款，最后的支付步骤
    def public_confirm_pay():
        """
        确认收款，最后的支付步骤
        :return:
        """
        touch(Template(r"photoes/tpl1745747890035.png", record_pos=(0.003, 0.988), resolution=(1080, 2400)))

    # 桌台详情页，切换页面
    def public_switch_tab(self, page_num):
        """
        切换页面：桌台信息1/订单信息2/会员信息3/点单二维码4/
        切换购物车/挂单/已付款tab：购物车5/已付款6/挂单7
        :return:
        """
        if page_num == "1":
            self.poco(text="桌台信息").click()
        elif page_num == "2":
            self.poco(text="订单信息").click()
        elif page_num == "3":
            self.poco(text="会员信息").click()
        elif page_num == "4":
            self.poco(text="点单二维码").click()
        elif page_num == '5':
            self.poco("com.wemew.teapro:id/tv_car_title").click()
        elif page_num == "6":
            self.poco("com.wemew.teapro:id/tv_pay_title").click()
        elif page_num == '7':
            self.poco("com.wemew.teapro:id/tv_not_pay_title").click()
        else:
            print("请切换存在正确的tab", page_num)

    @staticmethod
    def public_buy_pay(pay_type):
        """
        从购物车或者挂单页面，买单支付
        :return:
        """
        if pay_type == "买单支付":
            touch(Template(r"photoes/tpl1745748594888.png", record_pos=(0.315, 0.986), resolution=(1080, 2400)))
        elif pay_type == '挂单':
            touch(Template(r"photoes/tpl1745748605107.png", record_pos=(-0.004, 0.987), resolution=(1080, 2400)))
        else:
            print("请输入正确的买单支付类型:", pay_type)

    def public_total_discount(self, discount_type, phone_num="18982590424"):
        """
        支付页面，选择折扣/优惠券/会员信息
        折扣/优惠券/会员信息
        :return:
        """
        time.sleep(1)
        if discount_type == "折扣":
            self.poco(text="折扣").click()
        elif discount_type == "优惠券":
            self.poco(text="优惠券").click()
            self.poco("com.wemew.teapro:id/et_input_coupon").set_text("18982590424")
            self.poco("com.wemew.teapro:id/tv_search_code").click()
            self.poco("android.widget.FrameLayout").offspring("com.wemew.teapro:id/cl_top_select").offspring(
                "com.wemew.teapro:id/fl_coupon_container").offspring("com.wemew.teapro:id/recycler_view").child(
                "android.widget.FrameLayout")[0].offspring("com.wemew.teapro:id/iv_select").click()
            touch(Template(r"photoes/tpl1745741509846.png", record_pos=(0.206, 0.946), resolution=(1080, 2400)))
        elif discount_type == "会员信息":
            # 选择会员信息
            self.poco(text="会员信息").click()
            self.poco("com.wemew.teapro:id/et_search").set_text(phone_num)
            self.poco("com.wemew.teapro:id/tv_search").click()
            touch(Template(r"photoes/tpl1745741249264.png", record_pos=(0.003, 0.986), resolution=(1080, 2400)))

    def public_refund(self, tab_page, num):
        """
        勾选商品，退品
        :param
            staus(str):购物车/已付款/挂单
            num(str):退品的种类数量
        :return:
        """
        # 勾选商品
        for i in range(0, int(num)):
            self.poco("android.widget.FrameLayout").offspring("com.wemew.teapro:id/fl_background").offspring(
                "com.wemew.teapro:id/view_pager").offspring("com.wemew.teapro:id/recycle_goods").child(
                "com.wemew.teapro:id/cl_root_order")[i].offspring("com.wemew.teapro:id/iv_delete_goods").click()
        # 退品
        if tab_page == "购物车":
            touch(Template(r"photoes/tpl1745748662436.png", record_pos=(-0.313, 0.988), resolution=(1080, 2400)))
        elif tab_page == "挂单" or tab_page == "已付款":
            touch(Template(r"photoes/tpl1745748757485.png", record_pos=(0.005, 0.99), resolution=(1080, 2400)))
            self.poco("com.wemew.teapro:id/tv_return_goods").click()

    def public_close_tab(self):
        """
        关闭桌台详情页面
        :return:
        """
        self.poco("android.widget.FrameLayout").offspring("com.wemew.teapro:id/fl_background").child(
            "android.widget.LinearLayout").offspring("android.widget.ImageView").click()

    def public_give_goods(self):
        """
        app赠送商品
        :return:
        """
        # 加单品
        self.poco(name="com.wemew.teapro:id/iv_increase", type="android.widget.ImageView").click()
        # 切换菜单
        self.poco(text="AUTO-套餐").click()
        # 加套餐
        self.poco("com.wemew.teapro:id/iv_commodity").click()
        touch(Template(r"photoes/tpl1743587579470.png", record_pos=(-0.028, 0.273), resolution=(1080, 2400)))
        # 添加任选商品
        for i in range(0, 4):
            # +号
            touch((640, 1900))
        # 加入赠送列表
        touch(Template(r"photoes/tpl1745834140586.png", record_pos=(-0.086, 0.998), resolution=(1080, 2400)))
        touch(Template(r"photoes/tpl1745749063985.png", record_pos=(0.291, 0.968), resolution=(1080, 2400)))
        touch(Template(r"photoes/tpl1745749084244.png", record_pos=(0.306, 0.974), resolution=(1080, 2400)))

    def public_use_coupon(self):
        """
        卡券核销
        :return:
        """
        self.poco("com.wemew.teapro:id/et_input_coupon").set_text("18982590424")
        self.poco("com.wemew.teapro:id/tv_search_gift").click()
        self.poco("android.widget.FrameLayout").offspring("com.wemew.teapro:id/cl_top_select").offspring(
            "com.wemew.teapro:id/cl_code").offspring("com.wemew.teapro:id/recycler_view").child(
            "android.widget.FrameLayout")[0].child("com.wemew.teapro:id/tv_use").click()
        self.poco("com.wemew.teapro:id/tv_set").click()
        self.poco("com.wemew.teapro:id/tv_add_car").click()
        self.poco("com.wemew.teapro:id/tv_submit").click()

    def public_group_purchase(self):
        """
        抖音美团  团购核销
        :return:
        """
        self.poco("com.wemew.teapro:id/et_input_code").set_text("1573")
        self.poco("com.wemew.teapro:id/tv_search_code").click()
        touch(Template(r"photoes/tpl1745749230096.png", record_pos=(0.244, 0.984), resolution=(1080, 2400)))

    def public_book_table(self):
        """
        预订桌台
        :return:
        """
        touch(Template(r"photoes/tpl1745749283330.png", record_pos=(-0.001, 0.981), resolution=(1080, 2400)))
        # 到店人数
        self.poco("com.wemew.teapro:id/etPeople").set_text("2")
        # 姓名
        self.poco("com.wemew.teapro:id/etUserName").set_text("测试预订")
        # 电话
        self.poco("com.wemew.teapro:id/etPhone").set_text("18982590424")
        # 预订备注
        self.poco("com.wemew.teapro:id/etRemark").set_text("预订备注：ui自动化")
        # 确认订座
        self.poco("com.wemew.teapro:id/tv_save_wine").click()

    def public_cancle_book_table(self):
        """
        取消预订
        :return:
        """
        # 搜索桌台
        self.poco("com.wemew.teapro:id/et_search").set_text("9527")
        touch(Template(r"photoes/tpl1745749309630.png", record_pos=(0.044, 0.262), resolution=(1080, 2400)))
        # 确认取消
        self.poco(text="确定").click()
        # 返回首页
        self.poco("com.wemew.teapro:id/default_title_back").click()

    def public_click_menu(self, menu_name):
        """
        点击app最上方的菜单
        :return:
        """
        if menu_name == "接订":
            self.poco(text="接订").click()
        elif menu_name == "打赏小费":
            self.poco(text="打赏小费").click()
        elif menu_name == "存酒审核":
            self.poco(text="存酒审核").click()
        elif menu_name == "取酒审核":
            self.poco(text="取酒审核").click()
        elif menu_name == "会员":
            self.poco(text="会员").click()

    def public_refresh_page(self):
        """
        刷新首页
        :return:
        """
        self.poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
            "android:id/content").offspring(
            "com.wemew.teapro:id/app_bar_main").offspring("com.wemew.teapro:id/view_pager").child(
            "android.widget.FrameLayout").child(
            "android.widget.LinearLayout").offspring("com.wemew.teapro:id/recycler_view_tab").child(
            "android.widget.FrameLayout")[1].offspring(
            "com.wemew.teapro:id/ll_grey_block_root").swipe([0.0207, 0.3041])

    def public_save_wine(self):
        """
        存酒
        :return:
        """
        # 选择商品
        for i in range(0, 2):
            self.poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
                "android:id/content").offspring(
                "com.wemew.teapro:id/app_bar_main").offspring("com.wemew.teapro:id/view_pager").offspring(
                "com.wemew.teapro:id/viewPager").child(
                "android.widget.FrameLayout").offspring("com.wemew.teapro:id/fm_anim").offspring(
                "com.wemew.teapro:id/recycler_view").child(
                "android.widget.LinearLayout")[0].offspring("android.widget.RelativeLayout").offspring(
                "com.wemew.teapro:id/iv_increase").click()
        # 下一步
        touch(Template(r"photoes/tpl1745749671071.png", record_pos=(0.165, 0.706), resolution=(1080, 2400)))
        # 确定
        touch(Template(r"photoes/tpl1745749686033.png", record_pos=(0.003, 0.896), resolution=(1080, 2400)))
        # 录入存酒信息
        # 姓名
        self.poco("com.wemew.teapro:id/et_save_name").set_text("ui自动化")
        # 手机号
        self.poco("com.wemew.teapro:id/et_save_phone").set_text("18982590424")
        # 选桌台
        self.poco("com.wemew.teapro:id/tv_select_table").click()
        self.poco(text="9527").click()
        # 服务员
        self.poco("com.wemew.teapro:id/tv_right").click()
        self.poco("com.wemew.teapro:id/tv_manager_name").click()
        self.poco(text="小小杨").click()
        # 营销
        self.poco("com.wemew.teapro:id/tv_manager_real").click()
        self.poco(text="小小杨").click()
        # 存酒备注
        self.poco("com.wemew.teapro:id/et_save_remark").set_text("存酒备注：ui自动化")
        # 确认存酒
        self.poco("com.wemew.teapro:id/tv_save_wine").click()
        # 返回
        self.poco("com.wemew.teapro:id/tv_back").click()

    def public_examine_wine(self, examine_type):
        """
        存酒审核
        :return:
        """
        if examine_type == "拒绝":
            touch(Template(r"photoes/tpl1745749779514.png", record_pos=(-0.18, 0.368), resolution=(1080, 2400)))
        elif examine_type == "同意":
            touch(Template(r"photoes/tpl1745749795806.png", record_pos=(0.319, 0.369), resolution=(1080, 2400)))
            # 二次确认(同意）
            touch(Template(r"photoes/tpl1745749825701.png", record_pos=(0.199, 0.152), resolution=(1080, 2400)))
        elif examine_type == "修改信息":
            touch(Template(r"photoes/tpl1745749812080.png", record_pos=(0.071, 0.366), resolution=(1080, 2400)))
        time.sleep(1)
        # 返回首页
        self.poco("com.wemew.teapro:id/default_title_back").click()
        time.sleep(1)

    def public_switch_menu(self, menu_name):
        """
        切换下栏菜单
        :return:
        """
        if menu_name == '首页':
            self.poco("com.wemew.teapro:id/r_home").click()
        elif menu_name == '订单':
            self.poco("com.wemew.teapro:id/r_vv_order").click()
        elif menu_name == '业绩':
            self.poco("com.wemew.teapro:id/r_community").click()
        elif menu_name == '接单':
            self.poco("com.wemew.teapro:id/r_leave").click()
        elif menu_name == '存取酒':
            self.poco("com.wemew.teapro:id/r_mine").click()

    def public_swipe_menu(self, direction):
        if direction == "left":
            self.poco("androidx.recyclerview.widget.RecyclerView").swipe([0.7203, 0.0043])
        elif direction == "right":
            self.poco("androidx.recyclerview.widget.RecyclerView").swipe([-0.6897, 0.0555])

    def public_get_wine(self):
        """
        取酒
        :return:
        """
        self.poco("com.wemew.teapro:id/et_search").set_text("18982590424")
        # 搜索
        self.poco("com.wemew.teapro:id/iv_search").click()
        # 全选   #正则匹配
        self.poco(textMatches=".*?全选")[0].click()
        # 下一步
        touch(Template(r"photoes/tpl1745750093316.png", record_pos=(0.185, 0.774), resolution=(1080, 2400)))
        time.sleep(1)
        # 确认取酒
        touch(Template(r"photoes/tpl1745750109910.png", record_pos=(0.005, 0.981), resolution=(1080, 2400)))
        time.sleep(1)
        # 返回
        self.poco("com.wemew.teapro:id/tv_back").click()

    @staticmethod
    def public_switch_wine_tab(tab_name):
        """
        切换存取酒tab
        :param tab_name: 存酒/取酒
        :return:
        """
        if tab_name == "存酒":
            touch(Template(r"photoes/tpl1745750145099.png", record_pos=(-0.249, -0.862), resolution=(1080, 2400)))
        elif tab_name == "取酒":
            touch(Template(r"photoes/tpl1745750164049.png", record_pos=(0.251, -0.864), resolution=(1080, 2400)))

    def public_get_wine_examine(self, examine_type):
        """
        取酒审核
        :return:
        """
        if examine_type == "修改信息":
            touch(Template(r"photoes/tpl1745750392825.png", record_pos=(-0.177, 0.41), resolution=(1080, 2400)))
        elif examine_type == "拒绝":
            touch(Template(r"photoes/tpl1745750413742.png", record_pos=(0.075, 0.414), resolution=(1080, 2400)))
        elif examine_type == "通过":
            touch(Template(r"photoes/tpl1745750422268.png", record_pos=(0.325, 0.416), resolution=(1080, 2400)))
            # 确认通过
            touch(Template(r"photoes/tpl1745750431032.png", record_pos=(0.194, 0.154), resolution=(1080, 2400)))
        time.sleep(1)
        # 返回首页
        self.poco("com.wemew.teapro:id/default_title_back").click()
        time.sleep(1)

    def public_add_members(self):
        """
        新增会员
        :return:
        """
        # 新增会员按钮+
        self.poco("com.wemew.teapro:id/iv_add").click()
        # 会员信息
        self.poco("com.wemew.teapro:id/et_1").set_text("ui自动化")
        self.poco("com.wemew.teapro:id/et_2").set_text("199999999999")
        self.poco("com.wemew.teapro:id/et_5").set_text("770099")
        self.poco("com.wemew.teapro:id/tv_select_vip_type").click()
        self.poco(text="默认卡类型").click()
        self.poco("com.wemew.teapro:id/tv_manager").click()
        self.poco(text="小小杨").click()
        self.poco("com.wemew.teapro:id/tv_next").click()
        time.sleep(1)

    def public_serch_member(self, phone):
        """
        搜索会员手机号
        :param phone:会员手机号
        :return:
        """
        self.poco("com.wemew.teapro:id/iv_search").click()
        self.poco("com.wemew.teapro:id/et_search").set_text(phone)
        touch((977, 2169))

    def public_operate_member(self, operate_type):
        """
        操作会员
        :param operate_type:操作类型，充值、消费、会员卡金转移、销卡、退费、开卡、续费
        :return:
        """
        # 点击会员  进入详情
        # self.poco("com.wemew.teapro:id/tv_3").click()
        if operate_type == "充值":
            self.poco("com.wemew.teapro:id/tv_recharge1").click()
        elif operate_type == "销卡":
            self.poco("com.wemew.teapro:id/tv_print").click()
            self.poco(text="确定").click()
            time.sleep(1)
        elif operate_type == "返回":
            self.poco("com.wemew.teapro:id/default_title_back").click()
            time.sleep(1)

    def public_member_recharge(self):
        """
        会员充值
        :return:
        """
        # 充值信息
        self.poco("com.wemew.teapro:id/et_recharge_money").set_text("1000")
        self.poco("com.wemew.teapro:id/et_customer_send").set_text("1000")
        # 截图当前页面  算出充值金额

        self.poco(text="选择").click()
        self.poco(text="小小杨").click()
        self.poco("com.wemew.teapro:id/tv_table").click()
        self.poco(text="9527").click()
        self.poco(text="auto支付").click()
        # 下滑
        swipe((419, 1651), (419, 1000))
        # 充值备注
        self.poco("com.wemew.teapro:id/et_remark_recharge").set_text("ui自动化充值备注")
        # 确认充值
        touch(Template(r"photoes/tpl1745750787289.png", record_pos=(0.225, 0.996), resolution=(1080, 2400)))
        time.sleep(2)
        # 截图充值记录里的充值金额
        # 对比两者金额是否一直

    @staticmethod
    def public_get_relative_position(x1, y1, x2, y2):
        """
        获取元素相对位置
        :param x1: 起始点的横坐标比例
        :param y1: 起始点的纵坐标比例
        :param x2: 结束点的横坐标比例
        :param y2: 结束点的纵坐标比例
        :return: 元素的起始和结束位置
        """
        # 获取设备宽高
        width, height = device().get_current_resolution()
        start_position = (width * x1, height * y1)
        end_position = (width * x2, height * y2)
        return start_position, end_position
