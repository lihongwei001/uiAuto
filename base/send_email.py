import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_email(from_addr, password, to_addr, smtp_server, subject, html_msg):
    msg = MIMEMultipart()#整合邮件头、正文和附件等信息
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(html_msg,'html', 'utf-8'))
    try:
        smtpobj = smtplib.SMTP_SSL(smtp_server)
        smtpobj.connect(smtp_server, 465)
        smtpobj.login(from_addr, password)
        smtpobj.sendmail(from_addr, to_addr, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("无法发送邮件:", e)
    finally:
        if 'smtpobj' in locals():
            smtpobj.quit()

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '3178413043@qq.com'
password = 'zcjubwmfszmwdgec'  # 授权码，非登录密码
# 发信服务器
smtp_server = 'smtp.qq.com'
# 邮件内容
subject = 'report'
with open(r"D:\PythonProject\uiAuto\report\20241111095049report.html",'r',encoding='utf-8') as f:
    html_msg = f.read()
# 调用函数发送邮件，这里to_addr是接收方的邮箱地址，可以根据需要修改
to_addr = '1518236303@qq.com'
send_email(from_addr, password, to_addr, smtp_server, subject, html_msg)