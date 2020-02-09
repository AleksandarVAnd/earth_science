import smtplib
from email.mime.multipart import MIMEMultipart as Mmulti
from email.mime.text import MIMEText as Mtext
msg = Mmulti()
msg['From'] = 'aleksv.andonov@protonmail.com'
msg['To'] = '359883689998@sms.telenor.bg'
msg['Subject'] = 'VNIMANIE'
message = 'Opasni uslovia : '
msg.attach(Mtext(message))
mailserver = smtplib.SMTP('127.0.0.1', 587)
mailserver.set_debuglevel(2)
mailserver.login("aleksv.andonov@protonmail.com", "LSo5vg-TSDSYdBXhgcKBCg")
mailserver.sendmail('aleksv.andonov@protonmail.com', '359883689998@sms.telenor.bg', msg.as_string())

"""
send: b'Content-Type: multipart/mixed; boundary="===============6732086055219951364=="\r\nMIME-Version: 1.0\r\nFrom: aleksv.andonov@protonmail.com\r\nTo: 359883689998@sms.telenor.bg\r\nSubject: VNIMANIE\r\n\r\n--===============6732086055219951364==\r\nContent-Type: text/plain; charset="us-ascii"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: 7bit\r\n\r\nOpasni uslovia : \r\n--===============6732086055219951364==--\r\n.\r\n'
"""