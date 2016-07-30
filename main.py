"""
Tool for controlling LG air conditioner from Raspberry PI
"""

import wiringpi as pi

pi.wiringPiSetup()
pi.pinMode(0, pi.GPIO.OUTPUT)
pi.digitalWrite(0, pi.GPIO.HIGH)
