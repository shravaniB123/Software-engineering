import unittest 
import smtplib
import otp_version1 as O1


class BetweenAssertMixin(object):
    def assertBetween(self,x,low,high):
        if not (low <= x <= high):
            raise AssertionError('Length of OTP should be in between %r and %r' % (low,high))

class Test_otp(unittest.TestCase,BetweenAssertMixin):
    def testcase1(self):
        print("---------TestCase_No.1---------")
        #Check Email
        Name="Shravani"
        Email="spbhagwat01@gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Check OTP
        otp = O1.generate_OTP(4)
        self.assertBetween(len(otp),4,8)

        #Call Sendmail Function
        O1.send_email(Name,Email)
        print()

    def testcase2(self):
        #Checking Email with wrong email id
        print("---------TestCase_No.2---------")
        Name="Shravani"
        Email="spbhagwat01gmail.com"

        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "@" and "." and "com" and "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        otp = O1.generate_OTP(5)
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O1.send_email(Name,Email)
        print()

    def testcase3(self):
        #Checking Email
        print("---------TestCase_No.3---------")
        Name="Shravi"
        Email="spbhagwat01@gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        # Enter invalid otp length
        otp = O1.generate_OTP(9)
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O1.send_email(Name,Email)
        print()
        
unittest.main()
