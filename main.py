from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
import yaml
from base import connect_adb,AppiumServer,start_app
from appium import webdriver
from appium.options.common.base import AppiumOptions
import chardet
import subprocess
import time
from subprocess import Popen

# def run_appium_in_new_cmd():
#     """
#     在新的cmd窗口中运行appium命令。
#     """
#     # 使用start命令在新窗口中启动cmd并执行appium命令
#     command = 'start cmd /k appium'
#     subprocess.Popen(command, shell=True)


# def press_key(driver):
#     driver.press_keycode(driver)

# def create_driver(app_config):
#     """
#     根据传入的应用配置信息创建Appium驱动。
#
#     :param app_config: 包含应用相关配置信息的字典，如包名、活动名等
#     """
#     # 创建 AppiumOptions 对象
#     options = AppiumOptions()
#     # 加载测试的配置选项和参数(Capabilities配置)
#     options.load_capabilities({
#         # 自动化测试的引擎
#         "automationName": "uiautomator2",
#         # 平台名称
#         "platformName": "Android",
#         # 从配置中获取系统版本
#         "platformVersion": app_config.get("platform_version"),
#         # 从配置中获取设备名称
#         "deviceName": app_config.get("device_name"),
#         # 从配置中获取待测试应用的包名
#         "appPackage": app_config.get("app_package"),
#         # 从配置中获取待测试应用的活动（Activity）名称
#         "appActivity": app_config.get("app_activity"),
#         # 设置使用 Unicode 编码方式发送字符串到设备的键盘
#         "unicodeKeyboard": "true",
#         # 设置重置设备的软键盘状态并隐藏键盘
#         "restKeyboard": "true"
#     })
#
#     # Appium服务器地址端口，本地用http://127.0.0.1:4723
#     appium_host = 'http://127.0.0.1:4723'
#
#     return webdriver.Remote(appium_host, options=options)


if __name__ == "__main__":
    connect_adb.connect_devices()
    AppiumServer.run_appium_in_new_cmd()# 启动Appium服务
    # 读取YAML文件并依次启动devicesInfo.yaml文件里的app
    with open(r'D:\PythonProject\appiumAuto\conf\devicesInfo.yaml', 'rb') as file:  # 以二进制模式打开文件，方便检测编码
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    with open(r'D:\PythonProject\appiumAuto\conf\devicesInfo.yaml', 'r', encoding=encoding) as file:
        app_configs = yaml.safe_load(file)['apps']
        for app_config in app_configs:
            driver =start_app.create_driver(app_config)  # 调用函数创建驱动
            driver.implicitly_wait(30)  # 隐式等待
    driver.quit()  # 关闭驱动
