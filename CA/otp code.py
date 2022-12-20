import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('spbhagwat01@gmail.com',password="suqd pkdu rpyo gmif")
otp = ''.join([str(random.randint(0,9)) for i in range(4)])
msg = 'Hello,Your OTP is '+str(otp)
server.sendmail('spbhagwat01@gmail.com','vpbhagwat26@gmail.com', msg)
server.quit()
print(otp)
print(msg)
print(server)