# !/usr/bin/python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

msg = MIMEMultipart()

att1 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="123.doc"'
msg.attach(att1)

att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(att2)

msg['to'] = 'whf920521@sina.com'
msg['from'] = '201126630423@zjut.edu.cn'
msg['subject'] = 'hello world'

try:
    server = smtplib.SMTP()
    server.connect('smtp.zjut.edu.cn')
    server.login('201126630423', 'PASSWORD')
    server.sendmail(msg['from'], msg['to'], msg.as_string())
    server.quit()
    print 'Successfuly'
except Exception, e:
    print str(e)
