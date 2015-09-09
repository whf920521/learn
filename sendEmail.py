# !/usr/bin/python

import smtplib

sender = 'whf920521@sina.com'
receivers = ['201126630423@zjut.edu.cn']

message = """From: From Person <whf920521@sina.com>
To: To Person <201126630423@zjut.edu.cn>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.sina.com')
    smtpObj.login('whf920521', 'PASSWORD')
    smtpObj.sendmail(sender, receivers, message)
    smtpObj.close()
    print "Successfuly sent email"
except Exception:
    print "Error: unable to send email"
