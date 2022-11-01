# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:29:24 2022

@author: trobi
"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

sender = 'trobinuk@gmail.com'
receiver = 'trobinuk@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'New Jobs on Indeed'
msg['From'] = sender
msg['To'] = receiver

part = MIMEBase('application','octet-stream')
part.set_payload(open ('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\Indeed.csv','rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename = "Indeed.csv"')
msg.attach(part)

s = smtplib.SMTP_SSL(host='smtp.gmail.com',port=465)#465
s.login(user = 'trobinuk@gmail.com',password='crzwaywbnlbwczlo')
s.sendmail(sender,receiver,msg.as_string())
s.quit()

