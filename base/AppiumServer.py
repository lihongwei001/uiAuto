import subprocess
import psutil
from subprocess import PIPE,Popen

def run_appium_in_new_cmd():
    """
    在新的cmd窗口中运行appium命令。
    """
    # 使用start命令在新窗口中启动cmd并执行appium命令
    try:
        check_ven = subprocess.Popen(['where','appium'],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout, stderr = check_ven.communicate()
        if b'\\appium' in stdout:
            command = 'start cmd /k appium'
            subprocess.Popen(command, shell=True)
        else:
            print('请校验您的环境，确认是否已经安装appium或者已经配置环境变量')
    except FileNotFoundError as e:
        print(f"命令执行出错，可能相关命令不存在: {e}")
    except subprocess.SubprocessError as e:
        print(f"子进程启动出现问题: {e}")