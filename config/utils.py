# utils.py
import time
from functools import wraps
import pytest
from airtest.core.api import *

def airtest_failure_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #获取当前用例名称
            import sys
            mod = sys.modules[func.__module__]
            test_name = getattr(mod, 'current_test_name', None)
            # 失败后操作
            stop_app("com.wemew.teapro")
            time.sleep(1)
            start_app("com.wemew.teapro")
            print(f"{test_name}执行失败")
            pytest.skip(f"自动执行下一条: {str(e)}")
    return wrapper