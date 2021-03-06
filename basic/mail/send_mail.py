#!/user/bin/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email的地址和口令
# from_addr = input('From: ')
# password = input('Password: ')
from_addr = 'jandl1221@163.com'
password = 'VlzZ1221'
# 输入收件人地址
# to_addr = input('To: ')
to_addr = '616091158@qq.com'
# 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
smtp_server = 'smtp.163.com'

# msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
msg = MIMEMultipart()
# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('E:/picture/78063b49ly1fpxe93dklej20hs0hsjs1.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)


msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.helo(smtp_server)
server.ehlo(smtp_server)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

print('ok')