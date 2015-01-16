import smtplib
msg = (input("enter your one line message: "))
target = (input("enter the recieving email address: "))

server = smtplib.SMTP('smtp.yahoo.co.uk', 587)

server.login("zips_programs@yahoo.co.uk", "Pythagoras123")

msg = "\n(msg)!"
server.sendmail("zips_programs@yahoo.co.uk", target, msg)
