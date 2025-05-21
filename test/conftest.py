
def pytest_runtest_setup(item):
    """
    将当前用例存起来
    :param item:
    :return:
    """
    # 将当前测试名称注入到 pytest 的模块中
    item.module.__dict__['current_test_name'] = item.name
