import random
from django.core.mail import EmailMessage
import time
import pyotp

def generateOTP():
    
    otp = ""

    # Write logic for a simple otp generation using pyotp module
    totp = pyotp.TOTP('base32secret3232')
    totp.now() # => '492039'
        

    # OTP verified for current time
    totp.verify('492039') # => True
    time.sleep(30)
    totp.verify('492039') # => False
    pyotp.random_hex()

    return otp

def sendOTP():

    Subject = "OTP Verification"
    otp = generateOTP()
    print(otp)