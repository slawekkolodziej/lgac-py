"""
Tool for controlling LG air conditioner from Raspberry PI
"""
import wiringpi as pi
from lg import Remote

pi.wiringPiSetup()
pi.pinMode(0, pi.GPIO.OUTPUT)
pi.digitalWrite(0, pi.GPIO.HIGH)

REMOTE = Remote()

REMOTE.set_mode("COOLING", "1", 18, "ON")

print REMOTE.debug()

# serial = pi.serialOpen('/dev/ttyAMA0', 9600)

# pi.serialClose(serial)