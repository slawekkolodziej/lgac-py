"""
Tool for controlling LG air conditioner from Raspberry PI
"""
import pigpio
PIN = 18
pi = pigpio.pi()
pi.set_mode(PIN, pigpio.OUTPUT)
# pi.hardware_clock(PIN, 38000)

pi.write(PIN, 0)


from lg import Remote, BUFFER_SIZE
REMOTE = Remote()
REMOTE.set_mode("COOLING", "1", 18, "ON")

def space(time):
    """
    """
    pi.hardware_PWM(PIN, 38000, 0)
    delay(time)

def mark(time):
    """
    """
    pi.hardware_PWM(PIN, 38000, 1000000)
    delay(time)

def delay(usec):
    if usec > 4:
        start = pi.get_current_tick()
        end = start + usec - 4

        if end < start:
            while pi.get_current_tick() > start:
                pass
        while pi.get_current_tick() < end:
            pass

for n in range(0, BUFFER_SIZE):
    if n & 1:
        space(REMOTE.codes[n])
    else:
        mark(REMOTE.codes[n])

pi.write(PIN, 0)