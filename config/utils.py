# utils.py
from functools import wraps
import pytest
from PIL import Image
from airtest.core.api import *
import pytesseract

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
def snop_screen(x1,y1,x2,y2):
    """
    截屏并识别内容
    :return:
    """
    try:
        # 截图
        screenshot_path = "photo1.png"
        snapshot(filename=screenshot_path)  # 使用Airtest截图
        # 打开图片并进行裁剪
        img = Image.open(r'D:\myProject\UITEST-02-new\photo1.png')
        region = (x1, y1, x2, y2)
        cropped_img = img.crop(region)
        # 灰度处理
        gray_img = cropped_img.convert('L')
        # OCR识别
        table_num = pytesseract.image_to_string(gray_img, lang='chi_sim')  # 可根据需要更改语言包
        print("结婚后",table_num)
        print("识别结果:", table_num.strip())
        return table_num.strip()
    except Exception as e:
        print(f"截图或识别失败: {e}")
        return None