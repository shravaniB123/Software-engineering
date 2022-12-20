import random 
import senders_data as get
import smtplib
import unittest

class generate_otp(unittest.TestCase):


    #Getting Login credentials from sender_data file
    email = get.email
    password = get.password

    def __init__(self,receivers_name,receivers_email,n):
        self.receivers_name=receivers_name
        self.receivers_email=receivers_email
        self.n=n
        OTP=self.create_otp(self.n)

        #testing for otps length
        self.assertBetween(self.n,4,8)

        #validating emailid
        self.validation()
        
        self.send_email(OTP)

    def create_otp(self,n):
        self.n=n
        OTP=""
        for i in range(self.n):
            OTP+=str(random.randint(0,9))
        return (OTP)
    
    def __str__(self) :
        return ('{} has {} as an email'.format(self.receivers_name,self.receivers_email))

    
    def assertBetween(self, n, low, hi):
        if not (low <= n <= hi):
            raise AssertionError('Length of OTP is %r should be in between %r and %r' % (n, low, hi))
        print("------------------------------------------------------------")
    
    def validation(self):
        email="spbhagwat01@gmail.com"
        check_email =("@" and "gmail" and "."and "com") in email #self.receivers_email
        if check_email:
            print("No error in email")
        else:
            self.assertTrue(check_email)

    def send_email(self,OTP):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.email,self.password)

        msg=('Hi {}\n {} is your otp'.format(self.receivers_name,self.create_otp(self.n)))
        print(msg)
        server.sendmail(self.email,self.receivers_email,msg)
        server.quit()
        print("Email is sent!")

g=generate_otp('name','xxxxxxxxxxxxxxx@gmail.com',4)
        
        
