#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(admin_info, user_info, content):
    msg_from = admin_info.email  # 发送方邮箱
    passwd = admin_info.passwd  # 填入发送方邮箱的授权码
    msg_to = user_info.email  # 收件人邮箱

    subject = "Han's Job Push"  # 主题
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("success")
    except s.SMTPException as e:
        print("fail")
    finally:
        s.quit()