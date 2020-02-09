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