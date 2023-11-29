import random
from django.core.mail import EmailMessage
import time
import pyotp

def generateOTP():
    
    otp = ""

    # Write logic for a simple otp generation using pyotp module

    totp = pyotp.TOTP('base32secret3232')
    otp = totp.now()

    return otp

def sendOTP():

    Subject = "OTP Verification"
    otp = generateOTP()
    print(otp)