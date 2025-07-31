import time

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException


class TablePage:
    def __init__(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


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
            self.poco("com.wemew.teapro:id/et_pwd").set_text("123456")
            self.poco("com.wemew.teapro:id/tv_login_pwd").click()
    def public_order(self):
        """
        开台-点单-选购商品-挂单
        :return:
        """
        table_num = self.public_query_table_status("空闲")

    # 按桌台号查询桌台
    def public_query_table_by_num(self, table_num=None):
        """
        按桌台号搜索
        :param table_num:桌台号
        :return:
        """
        self.poco("com.wemew.teapro:id/et_search_table").set_text(table_num)
        self.poco("com.wemew.teapro:id/tv_search_table").click()

    def public_find_free_table(self):
        """
        寻找空闲桌台
        """
        time.sleep(1)
        try:
            self.poco(text="空闲")[0].click()
        except PocoNoSuchNodeException as e:
            print("当前无空闲桌台 向下滑动")
            swipe(v1=(0.5, 0.8),v2=(0.5,0))
            self.poco(text="空闲")[0].click()
    def public_click_table(self, table_num):
        """
        点击桌台
        :param table_num:桌台号
        :return:
        """
        self.poco(text=table_num).click()
        time.sleep(1)
    #开台
    def public_open_table(self):
        """
        开台流程
        :return:桌台号
        """
        time.sleep(0.3)
        #
        # 定位桌台号
        table = self.poco("com.wemew.teapro:id/tv_tab_num").get_text()
        table_num = table.split("(")[0]
        touch((788, 2223))
        return table_num
    # 操作桌台
    def public_oprate_table(self,method, table_status="normal", open_type=None):
        """
        桌台的基本操作，开台、翻台、点单等
        :return:
        """
        time.sleep(1)
        if method == "开台":
            if table_status == "normal":
                self.poco("开台").click()
                time.sleep(0.3)
                #定位桌台号
                table = self.poco("com.wemew.teapro:id/tv_tab_num").get_text()
                table_num = table.split("(")[0]
                #确认开台
                touch((788,2223 ))
                return table_num
            elif table_status == "reserve":
                self.poco("开台").click()
                if open_type == "普通开台":
                    self.poco("普通开台").click()
                    #确认开台
                    touch((788,2223 ))
                elif open_type == "预订开台":
                    self.poco("预订开台").click()
                    # 确认开台
                    touch((788, 2223))
        elif method == "翻台":
            self.poco("翻台").click()
        elif method == "点单":
            self.poco("点单").click()
        elif method == "预订":
            self.poco("预订").click()
        elif method == "锁台":
            pass
        elif method == "赠送":
            self.poco("赠送").click()
        elif method == "存酒":
            self.poco("存酒").click()
        elif method == "取酒":
            self.poco("取酒").click()
        elif method == "转台":
            self.poco("转台").click()
        elif method == "卡券核销":
            self.poco("卡券核销").click()
        elif method == "团购核销":
            self.poco("团购核销").click()
        time.sleep(1)

    # 加购商品
    def public_add_goods(self,set_meal_type="普通套餐"):
        """
        选择商品+套餐
        :param: setMeal_type:套餐类型
        :return:
        """
        time.sleep(1.5)
        if set_meal_type == "普通套餐":
            touch((950, 735))
            time.sleep(0.5)
            for i in range(0, 5):
                # +号
                touch((699, 2030))
            self.poco("加入购物车").click()
        else:
            #普通套餐
            touch((950, 735))
            time.sleep(0.5)
            for i in range(0, 5):
                # +号
                touch((699, 2030))
            time.sleep(0.2)
            self.poco("加入购物车").click()

            # 全必选套餐
            touch((950, 1013))
            time.sleep(0.5)
            self.poco("加入购物车").click()

            # 全任选套餐
            touch((950, 1300))
            time.sleep(0.5)
            # +号
            for i in range(0, 2):
                touch((341, 2030))
            for i in range(0, 3):
                touch((699, 2030))
            self.poco("加入购物车").click()

            #可加价套餐
            touch((950, 1578))
            time.sleep(0.5)
            for i in range(0, 2):
                touch((341, 2030))
            # 点击  加入购物车
            self.poco("加入购物车").click()

            #可替换套餐
            touch((950, 1871))
            time.sleep(0.5)
            touch((155, 1603))
            # 下滑
            swipe((495, 1178), (495, 202))
            time.sleep(0.5)
            # 勾选  替换商品
            touch((223, 1483))
            self.poco("加入购物车").click()
        time.sleep(0.5)
        #选择单品分类
        touch((101,655))
        #点击 单品的选规格
        touch((950,1441))
        time.sleep(0.5)
        #点击 加入购物车
        self.poco("加入购物车").click()
        # 点击 单品的选规格
        touch((950, 1441))
        time.sleep(0.5)
        #选择多单位
        touch((337,1401))
        # 点击 加入购物车
        self.poco("加入购物车").click()
        #点击去结算
        self.poco("去结算").click()
    def public_save_goods(self,save_type):
        """
        1.保存购物车  2.挂单   3.买单支付
        :return:
        """
        time.sleep(1)
        if save_type == "1":
            self.poco("保存购物车").click()
        elif save_type == "2":
            self.poco("挂单").click()
        elif save_type == "3":
            self.poco("买单支付").click()
        else:
            print("保存购物车/挂单/买单支付失败，请输入正确的类型:", save_type)
        time.sleep(1)

        # 选择支付方式
    @staticmethod
    def public_pay_method(pay_method):
        """
        选择支付方式
        :param pay_method:string,移动支付/会员支付/自定义支付
        :return:
        """
        time.sleep(1)
        if pay_method == "移动支付":
            touch(Template(r"photoes/tpl1750090544107.png", record_pos=(-0.267, 0.14), resolution=(1080, 2400)))
        elif pay_method == "会员支付":
            touch(Template(r"photoes/tpl1750090548114.png", record_pos=(-0.283, 0.254), resolution=(1080, 2400)))
        elif pay_method == "自定义支付":
            touch(Template(r"photoes/tpl1750090551467.png", record_pos=(-0.284, 0.369), resolution=(1080, 2400)))
        else:
            print("请输入正确的支付方式:", pay_method)

    def public_combine_pay(self, pay_method1, pay_method2,money):
        """
        组合支付
        :param pay_method1: 移动支付/会员支付/自定义支付
        :param money:输入金额
        :param pay_method2:移动支付/会员支付/自定义支付
        :return:
        """
        self.public_pay_method(pay_method1)
        self.public_pay_method(pay_method2)
        if pay_method1 == "移动支付" and pay_method2 == "会员支付":
            pass
        elif pay_method1 == "移动支付" and pay_method2 == "自定义支付":
            pass
        elif pay_method1 == "会员支付" and pay_method2 == "自定义支付":
            # 选择会员支付
            # 组合支付  输入金额
            touch((200, 1777))
            text(money)


    # 确认收款，最后的支付步骤
    def public_confirm_pay(self):
        """
        确认收款，最后的支付步骤
        :return:
        """
        self.poco("确认收款").click()
        time.sleep(0.5)
        # 支付成功 确定页面
        self.poco("确定").click()
    @staticmethod
    def public_switch_tab(page_num):
        """
        切换页面：桌台信息1/订单信息2/会员信息3/点单二维码4/
        切换购物车/挂单/已付款tab：购物车5/已付款6/挂单7
        :return:
        """
        time.sleep(0.5)
        if page_num == "1":
            touch((132,545))
        elif page_num == "2":
            touch((380,545))
        elif page_num == "3":
            touch((640,545))
        elif page_num == "4":
            touch(895,545)
        elif page_num == '5':
            touch((198,807))
        elif page_num == "6":
            touch((524,807))
        elif page_num == '7':
            touch((874,807))
        else:
            print("请切换存在正确的tab", page_num)
        time.sleep(0.3)

    def public_buy_pay(self,pay_type):
        """
        从购物车或者挂单页面，买单支付
        :return:
        """
        time.sleep(0.5)
        if pay_type == "买单支付":
            touch(Template(r"photoes/tpl1745748594888.png", record_pos=(0.315, 0.986), resolution=(1080, 2400)))
        elif pay_type == '挂单':
            touch((538,2288))
        elif pay_type == "支付":
            self.poco("支付").click()
        else:
            print("请输入正确的买单支付类型:", pay_type)
        time.sleep(1)

    def public_total_discount(self, discount_type, phone_num='18982590424'):
        """
        支付页面，选择折扣/优惠券/会员信息
        折扣/优惠券/会员信息
        :return:
        """
        time.sleep(1)
        if discount_type == "打折":
            self.poco(text="打折").click()
            #按比例折扣 （8折）
            touch((278,931))
            text("8")
            # 折扣备注（zk）
            touch((204, 604))
            text("UI自动化-折扣备注")
            #确认折扣
            self.poco("确认").click()
        elif discount_type == "优惠券":
            self.poco("优惠券").click()
            touch((239,730))
            text(phone_num,search=True)
            touch((998,906))
            time.sleep(0.3)
        elif discount_type == "会员信息":
            # 选择会员信息
            self.poco("会员信息").click()
            time.sleep(0.5)
            touch((320,807))
            text(phone_num,search=True)
            self.poco("确认").click()
        time.sleep(1)

    def public_refund(self, tab_page):
        """
        勾选商品，退品
        :param
            tab_page(str):购物车/已付款/挂单
            num(str):退品的种类数量
        :return:
        """
        time.sleep(0.5)
        # 勾选商品
        touch((91,1040))
        # 退品
        if tab_page == "购物车":
            touch(Template(r"photoes/tpl1745748662436.png", record_pos=(-0.313, 0.988), resolution=(1080, 2400)))
        elif tab_page == "挂单" or tab_page == "已付款":
            touch(Template(r"photoes/tpl1745748757485.png", record_pos=(0.005, 0.99), resolution=(1080, 2400)))
            self.poco("com.wemew.teapro:id/tv_return_goods").click()
    @staticmethod
    def public_close_tab():
        """
        关闭桌台详情页面
        :return:
        """
        touch((1028,550))

    def public_give_goods(self):
        """
        app赠送商品
        :return:
        """
        # 加单品
        touch((982,668))
        touch((982,958))
        # 切换菜单
        self.poco(text="AUTO-套餐").click()
        # 加套餐
        self.poco(text="全必选套餐").click()
        self.poco("com.wemew.teapro:id/tv_add_car").click()
        self.poco(text="必选+任选（普通套餐）").click()
        touch((208,1038))
        # 添加任选商品
        for i in range(0, 4):
            # +号
            touch((307,1310))
        self.poco("com.wemew.teapro:id/tv_add_car").click()
        self.poco("com.wemew.teapro:id/tv_next").click()
        time.sleep(0.5)
        self.poco("com.wemew.teapro:id/tv_next").click()


    def public_use_coupon(self):
        """
        卡券核销
        :return:
        """
        #输入手机号
        touch((246,801))
        text("18982590424",search=True)
        touch((1004,984))
        #套餐选择
        self.poco("套餐选择").click()
        self.poco("确定").click()
        self.poco("确定核销").click()
        time.sleep(0.5)

    def public_group_purchase(self):
        """
        抖音美团  团购核销
        :return:
        """
        touch((306,414))
        text("123",search=True)
        self.poco("确定核销").click()

    def public_book_table(self):
        """
        预订桌台
        :return:
        """
        time.sleep(1)
        #下一步
        self.poco("com.wemew.teapro:id/tv_save_wine").click()
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
        self.poco("com.wemew.teapro:id/tv_cancel").click()
        # 确认取消
        self.poco(text="确定").click()
        # 返回首页
        self.poco("com.wemew.teapro:id/default_title_back").click()

    def public_click_menu(self, menu_name):
        """
        点击app最上方的菜单
        :return:
        """
        self.poco(text=menu_name).click()
    @staticmethod
    def public_refresh_page():
        """
        刷新首页
        :return:
        """
        swipe(v1=(507, 1285), v2=(507, 2127))

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
        """
        滑动app上方的菜单栏
        :param direction:left就是从左往右
        :return:
        """
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

    def public_add_members(self,phone):
        """
        新增会员
        :return:
        """
        # 新增会员按钮+
        self.poco("com.wemew.teapro:id/iv_add").click()
        # 会员信息
        self.poco("com.wemew.teapro:id/et_1").set_text("ui自动化")
        self.poco("com.wemew.teapro:id/et_2").set_text(phone)
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
        touch((283,312))
        text(text=phone,search=True)

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
        self.poco("com.wemew.teapro:id/tv_fix_table").click()
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
    def public_turn_table(self,turn_type,table_num=None):
        """

        :param table_num: 待转桌台号
        :param  turn_type: 变动类型：转台/联台/合并台
        :return:
        """
        if turn_type == "转台":
            #找空闲桌台
            table_num2 = self.poco("com.wemew.teapro:id/tv_tab_num")[0].get_text()
            print("待转台台号:", table_num2)
            self.public_click_table(table_num2)
            #确认转台
            self.poco("com.wemew.teapro:id/tv_next").click()
            return table_num2
        elif  turn_type == "联台":
            pass
        elif turn_type == "合并台":
            pass
        else:
            print("请输入正确的b变动台位类型", turn_type)
        time.sleep(1)
    def public_reward(self,pay_type=None):
        """
        打赏
        :param pay_type: 是否是组合支付
        :return:
        """
        self.poco("com.wemew.teapro:id/tv_pay_free").click()
        #选择开台桌台
        self.poco("com.wemew.teapro:id/tv_select_table").click()
        self.poco("android.widget.FrameLayout").offspring("com.wemew.teapro:id/recycle_table").child("android.widget.FrameLayout")[0].offspring("com.wemew.teapro:id/ll_red_block_root").click()
        #输入打赏金额
        self.poco("com.wemew.teapro:id/et_input_price").set_text("500")
        #打赏备注
        self.poco("com.wemew.teapro:id/et_input_remark").set_text("ui自动化-打赏备注")
        #发起打赏
        self.poco("com.wemew.teapro:id/tv_pay_free").click()
        if pay_type == "组合支付":
            self.poco(text="auto支付").click()
            self.poco(text="现金支付").click()
            touch((399,950))
            text("100")
            touch((923,2326))
        else:
            self.poco(text="auto支付").click()
        time.sleep(0.5)
        self.poco("com.wemew.teapro:id/tv_pay_free").click()
        time.sleep(0.5)
        self.poco("com.wemew.teapro:id/tv_pay_free").click()
    def public_taipiao(self,pay_type=None):
        """
        :param pay_type:是否是组合支付
        :return:
        """
        #输入充值金额
        self.poco("com.wemew.teapro:id/et_input_price").set_text("500")
        #提交
        self.poco("com.wemew.teapro:id/tv_pay_commit_tt").click()
        #选择支付方式
        if pay_type =="组合支付":
            self.poco(text="auto支付").click()
            self.poco(text="现金支付").click()
            touch((400,915))
            time.sleep(0.3)
            touch((305, 1708))
            touch((538, 2177))
            touch((954, 2166))
            touch((971, 2175))
        else:
            self.poco(text="auto支付").click()
        #确认收款
        self.poco("com.wemew.teapro:id/tv_pay_free").click()
        time.sleep(0.4)
        #返回首页
        self.poco("com.wemew.teapro:id/tv_pay_free").click()
    def public_taipiao_verify(self):
        """
        台票核销
        :return:
        """
        #切换到核销页面
        self.poco("com.wemew.teapro:id/check_ticket_dark").click()
        #选择桌台
        self.poco("com.wemew.teapro:id/tv_select_table_ct").click()
        self.poco("android.widget.FrameLayout").offspring("com.wemew.teapro:id/recycle_table").child(
            "android.widget.FrameLayout")[0].offspring("com.wemew.teapro:id/ll_red_block_root").click()
        #扫码台票核销
        self.poco("com.wemew.teapro:id/iv_scan_tt").click()
        self.poco("com.wemew.teapro:id/img_btn").click()
        touch((148,615))
        time.sleep(1)
        #提交核销
        self.poco("com.wemew.teapro:id/tv_check_commit_tt").click()
        time.sleep(1)
        for i in range(3):
            self.public_swipe_menu(direction="left")

    def public_line_up(self):
        """
        排队
        :return:
        """
        #取号
        self.poco("com.wemew.teapro:id/tv_save_wine").click()
        #输入手机号
        self.poco("com.wemew.teapro:id/et_phone").set_text("18982590424")
        #确定 排队信息
        self.poco("com.wemew.teapro:id/tv_fix_table").click()
        #查看排队情况
        touch((532,274))
        #获取排队手机号
        phone = self.poco("com.wemew.teapro:id/tv_phone").get_text()
        print("排队手机号：",phone)
        #叫号
        self.poco("com.wemew.teapro:id/tv_c_2").click()
        self.poco(text="确定").click()
        #入场
        self.poco("com.wemew.teapro:id/tv_c_3").click()
        #选择桌台 开台
        self.poco("com.wemew.teapro:id/tv_tab_num")[0].click()
        table_num = self.poco("com.wemew.teapro:id/tv_tab_num")[0].get_text()
        self.poco("com.wemew.teapro:id/tv_next").click()
        self.poco("com.wemew.teapro:id/tv_next").click()
        time.sleep(1)
        #返回首页
        self.poco("com.wemew.teapro:id/default_title_back").click()
        return table_num
    def public_recover_wine(self):
        """
        酒水回收
        :return:
        """
        #选择桌台
        self.poco(text="9527").click()
        time.sleep(0.5)
        #选择酒水
        touch(Template(r"photoes/tpl1747302071299.png", record_pos=(0.387, -0.497), resolution=(1080, 2400)))
        #整体回收
        self.poco("com.wemew.teapro:id/iv_increase_whole").click()
        #部分回收
        self.poco("com.wemew.teapro:id/iv_increase_dot").click()
        #瓶盖回收
        self.poco("com.wemew.teapro:id/iv_increase_bottom").click()
        #空瓶回收
        self.poco("com.wemew.teapro:id/iv_increase_empty").click()
        #确定回收
        self.poco("com.wemew.teapro:id/tv_sure_wine").click()
        self.poco("com.wemew.teapro:id/tv_next").click()
        #返回首页
        self.poco("com.wemew.teapro:id/default_title_back").click()
    def public_recover_wine_verify(self,verify_type):
        """
        酒水回收  审核
        :return:
        """
        if verify_type == "通过":
            self.poco("com.wemew.teapro:id/tv_pass").click()
        else:
            self.poco("com.wemew.teapro:id/tv_cancel").click()
        #返回首页
        self.poco("com.wemew.teapro:id/default_title_back").click()
    def public_add_staff(self):
        """
        添加员工
        :return:
        """
        #点击 新增员工
        self.poco("com.wemew.teapro:id/tv_right").click()
        #输入员工信息
        self.poco("com.wemew.teapro:id/et_name").set_text("ui自动化测试员工")
        self.poco("com.wemew.teapro:id/et_phone").set_text("19511862897")
        self.poco("com.wemew.teapro:id/et_position").set_text("ui自动化-职位")
        self.poco("com.wemew.teapro:id/et_login_pwd").set_text("123456")
        self.poco("com.wemew.teapro:id/et_repeat_pwd").set_text("123456")
        self.poco(text="ui自动化角色").click()
        #保存
        self.poco("com.wemew.teapro:id/tv_save").click()
        time.sleep(1)
    def public_operate_staff(self,operate_type):
        """
        停用/启用员工
        :return:
        """
        #搜索员工
        self.poco("com.wemew.teapro:id/et_search").set_text("19511862897")
        touch((522,232))
        time.sleep(0.8)
        touch((984,2173))
        if operate_type == "停用":
            #点击停用
            self.poco("com.wemew.teapro:id/tv_manager_people").click()
        else:
            #点击启用
            self.poco("com.wemew.teapro:id/tv_manager_people").click()
    def public_inventory_check(self):
        """
        库存盘点
        :return:
        """
        #选择商品
        self.poco("com.wemew.teapro:id/tv_select").click()
        self.poco("com.wemew.teapro:id/tv_select")[0].click()
        self.poco("com.wemew.teapro:id/et_set_price").set_text("100")
        self.poco("com.wemew.teapro:id/tv_sure").click()
        self.poco("com.wemew.teapro:id/tv_save_wine").click()
        time.sleep(0.5)
        self.poco("com.wemew.teapro:id/tv_save_wine").click()
        self.poco("com.wemew.teapro:id/default_title_back").click()
    def public_storage_in(self):
        """
        商品入库
        :return:
        """
        #选择入库类型
        self.poco("com.wemew.teapro:id/tv_type").click()
        self.poco(text="ui自动化入库").click()
        #选择商品
        self.poco("com.wemew.teapro:id/tv_select").click()
        self.poco('com.wemew.teapro:id/tv_select')[0].click()
        #输入数量和成本价
        self.poco("com.wemew.teapro:id/et_set_quantity").set_text("100")
        self.poco("com.wemew.teapro:id/et_set_price").set_text("100")
        #确认
        self.poco("com.wemew.teapro:id/tv_sure").click()
        self.poco("com.wemew.teapro:id/tv_save_wine").click()
        time.sleep(0.5)
        self.poco("com.wemew.teapro:id/tv_save_wine").click()
        self.poco("com.wemew.teapro:id/default_title_back").click()