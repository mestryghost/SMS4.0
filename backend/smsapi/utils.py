import random
from django.core.mail import EmailMessage

def generateOTP():
    
    otp = ""

    # Write logic for a simple otp generation using pyotp module

    return otp

def sendOTP():

    Subject = "OTP Verification"
    otp = generateOTP()
    print(otp)