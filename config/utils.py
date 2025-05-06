#工具类
from airtest.core.api import snapshot


class Utils:
    @staticmethod
    def safe_assert_exist(condition,message="断言失败!"):
        """
        安全的断言方法，判断元素是否存在
        :param condition:断言条件，可以是图片 也可以是元素
        :param message:断言失败 抛出message
        :return:
        """
        try:
            assert condition, message
        except AssertionError as e:
            print(f"断言失败: {e}")
            #失败截图
            snapshot(filename=message,msg=f"断言失败截图_{message}")
