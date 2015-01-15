import smtplib
import os

email = (input("receiving email address: "))
msg1 = (("line 1/3: "))
msg2 = (("line 2/3: "))
msg3 = (("line 3/3: "))

file = open("email.txt", "a")
file.write(msg1 + "\n" + msg2 + "\n" + msg3)

from email.mime.text import MIMEText

fp = open("email.txt", "rb")
msg = MIMEText(fp.read())
fp.close()

msg['EMERGENCY'] = 'The contents of %s' % textfile
msg['From'] = zips_programs@yahoo.co.uk
msg['To'] = (email)

s = smtplib.SMTP('localhost')
s.sendmail(zips_programs@yahoo.co.uk, [(email)], msg.as_string())
s.quit()
