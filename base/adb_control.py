import logging
import os
import subprocess
from subprocess import PIPE, Popen
import time
from adbutils.shell import is_percent

class App_control:
    def __init__(self,device_id):
        self.device = device_id
    def adb_connect(self):
        """
        连接设备
        :return:
        """
        try:
            connect = f'adb connect {self.device}'
            subprocess.Popen(connect, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            time.sleep(1)
            stdout,stderr = subprocess.Popen(connect, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if b'connected' in stdout:
                print(f'设备连接成功{stdout}')
                logging.info(f'设备{self.device}连接成功{stdout}')
                return True
            else:
                print(f'设备连接失败{stderr}')
                logging.info(f'设备{self.device}连接失败{stderr}')
                return False
        except FileNotFoundError as e:
            logging.error(f"命令执行出错，可能相关命令不存在: {e}")
            return False

    def adb_disconnecct(self):
        '''
        断开设备连接
        '''
        try:
            disconnect = f'adb disconnect {self.device}'
            subprocess.Popen(disconnect, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(disconnect, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if b'disconnected' in stdout:
                print(f'设备断开连接成功{stdout}')
                logging.info(f'设备{self.device}断开连接成功{stdout}')
                return True
            else:
                print(f'设备断开连接失败{stdout}')
                logging.info(f'设备{self.device}断开连接失败{stderr}')
                return False
        except FileNotFoundError as e:
            logging.error(f"命令执行出错，可能相关命令不存在: {e}")
            return False

    def start_activity(self,package,activity):
        '''
        启动app
        '''
        try:
            start_activity = f'adb -s {self.device} shell am start -n {package}/{activity}'
            subprocess.Popen(start_activity, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(start_activity, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if len(stderr) == 0:
                print(f'启动app成功{stdout}')
                logging.info(f'启动app成功{stdout}')
                return True
            else:
                print(f'启动app失败{stderr}')
                logging.info(f'启动app失败{stderr}')
                return False
        except Exception as e:
                print('启动app过程中有问题')
                logging.info(f'命令执行出错，可能相关命令不存在: {e}')

    def stop_activity(self,package):
        '''
        停止app
        '''
        try:
            stop_activity = f'adb -s {self.device} shell am force-stop {package}'
            subprocess.Popen(stop_activity, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(stop_activity, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if len(stderr) == 0:
                print(f'停止app成功{stdout}')
                logging.info(f'停止app成功{stdout}')
                return True
            else:
                print(f'停止app失败{stderr}')
                logging.info(f'停止app失败{stderr}')
                return False
        except Exception as e:
                print('停止app过程中有问题')
                logging.info(f'命令执行出错，可能相关命令不存在: {e}')
    def start_server(self,service):
        '''
        启动服务
        '''
        try:
            start_server = f'adb -s {self.device} shell am startservice{service}'
            subprocess.Popen(start_server, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(start_server, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if len(stderr) == 0:
                print(f'启动服务成功{stdout}')
                logging.info(f'启动服务成功{stdout}')
                return True
            else:
                print(f'启动服务失败{stderr}')
                logging.info(f'启动服务失败{stderr}')
                return False
        except Exception as e:
                print('启动服务过程中有问题')
                logging.info(f'命令执行出错，可能相关命令不存在: {e}')
    def stop_server(self,service):
        '''
        停止服务
        '''
        try:
            stop_server = f'adb -s {self.device} shell am stopservice{service}'
            subprocess.Popen(stop_server, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(stop_server, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if len(stderr) == 0:
                print(f'停止服务成功{stdout}')
                logging.info(f'停止服务成功{stdout}')
                return True
            else:
                print(f'停止服务失败{stderr}')
                logging.info(f'停止服务失败{stderr}')
                return False
        except Exception as e:
                print('停止服务过程中有问题')
                logging.info(f'命令执行出错，可能相关命令不存在: {e}')
    def input_keyevent(self,keycode):
        '''
        模拟按键
        '''
        try:
            input_keyevent = f'adb -s {self.device} shell input keyevent {keycode}'
            subprocess.Popen(input_keyevent, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(input_keyevent, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if len(stderr) == 0:
                print(f'模拟按键成功{stdout}')
                logging.info(f'模拟按键成功{stdout}')
                return True
            else:
                print(f'模拟按键失败{stderr}')
                logging.info(f'模拟按键失败{stderr}')
                return False
        except Exception as e:
                print('模拟按键过程中有问题')
                logging.info(f'命令执行出错，可能相关命令不存在: {e}')
    def send_command(self,command):
        '''
        发送命令
        '''
        try:
            send_command = f'adb -s {self.device} shell {command}'
            subprocess.Popen(send_command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(send_command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if len(stderr) == 0:
                print(f'发送命令成功{stdout}')
                logging.info(f'发送命令成功{stdout}')
                return True
            else:
                print(f'发送命令失败{stderr}')
                logging.info(f'发送命令失败{stderr}')
                return False
        except Exception as e:
                print('发送命令过程中有问题')
                logging.info(f'命令执行出错，可能相关命令不存在: {e}')
    def push_file(self,file_path,remote_path):
        '''
        推送文件到设备
        '''
        try:
            push_sh = f'adb -s {self.device} push {file_path} {remote_path}'
            subprocess.Popen(push_sh, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(push_sh, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            if b' No such file or directory'in stderr:
                print(f'推送文件失败{stderr}')
                logging.info(f'推送文件失败{stderr}')
                return False
            else:
                print(f'推送文件成功{stderr}')
                logging.info(f'推送文件成功{stderr}')
                return True
        except Exception as e:
                print('推送文件过程中有问题')
                logging.info(f'命令执行出错，可能相关命令不存在: {e}')

    def pull_file(self,remote_path,local_path):
        '''
        从设备拉取文件
        '''
        try:
            pull_sh = f'adb -s {self.device} pull {remote_path} {local_path}'
            subprocess.Popen(pull_sh, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            time.sleep(1)
            stdout,stderr = subprocess.Popen(pull_sh, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            print(stdout)
            print(stderr)
            if b' No such file or directory'in stderr:
                print(f'拉取文件失败{stderr}')
                logging.info(f'拉取文件失败{stderr}')
                return False
            else:
                print(f'拉取文件成功{stderr}')
                logging.info(f'拉取文件成功{stderr}')
                return True
        except Exception as e:
                print(f'拉取文件过程中有问题{e}')
                logging.info(f'命令执行出错，可能相关命令不存在: {e}')


app_control = App_control("10.192.188.209")
App_control.adb_connect(self=app_control)
App_control.pull_file(self=app_control,remote_path="/data/local/tmp/test.sh",local_path="D:apk/")
