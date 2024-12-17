import requests
import json
import traceback

def sendEmail(report_file,subject,receiver):
    """
    发送邮件报告
    para:
    receiver:接收邮件list
    report_file:报告的路径
    """
    try:
        receiver_list = []
        receiver = receiver.split(',')
        for i in receiver:
            if '@qq.com' not in i:
                receiver_list.append(i+'@qq.com')
        print(receiver_list)
        carbonCopy_list = ['3178413043@qq.com']
        html_content = open(report_file, 'rb').read()
        subject = subject
        receiver_list = ', '.join(receiver_list)
        carbonCopy_list = ', '.join(carbonCopy_list)

        body = {
            "token": "",
            "subject": subject,
            "tos": receiver_list,
            "content": html_content,
            "html": True,
            "ccs": carbonCopy_list
        }
        files = {'attachFiles': ('report.html', html_content)}
        send = requests.post('', data=body, files=files)
        print(json.dumps(send.json(), ensure_ascii=False, indent=4))
        print("Send successfully.")

    except:
        traceback.print_exc()
if __name__ == '__main__':
    sendEmail(r"D:\PythonProject\uiAuto\report\report.html",'测试报告','3178413043@qq.com')