"""
Library that genrates LG air conditioner remote codes
"""

from bit import set_bit, test_bit

FIRST_BYTE = 136 # b10001000

STATE = {
    "ON": 0,
    "OFF": 24, # b11000
    "CHANGE_MODE": 1,
}

MODE = {
    "HEATING": 4, # b100
    "AUTO": 3, # b011
    "DEHUIDIFICATION": 1, # b001
    "COOLING": 0,
    "NONE": 0,
}

TEMPERATURE_OFFSET = 15

FAN = {
    "1": 1,
    "2": 0,
    "3": 2,
    "4": 4, # b100
    "NONE": 5, # b101
}

FIRST_HIGH = 8271
FIRST_LOW = 4298
ZERO_AND_ONE_HIGH = 439
ZERO_LOW = 647
ONE_LOW = 1709

BUFFER_SIZE = 59

class Remote(object):
    """
    Library that genrates LG air conditioner remote codes
    """

    def __init__(self):
        self.codes = []
        self.crc = 0

    def set_mode(self, mode, fan, temperature, state):
        """
        Generate code and put it in the buffer
        """
        self.codes[0] = FIRST_HIGH
        self.codes[1] = FIRST_LOW
        self.crc = 0

        self.fill_buffer(0, 8, FIRST_BYTE)
        self.fill_buffer(8, 5, state)

        if state == STATE['OFF']:
            self.fill_buffer(13, 3, MODE['NONE'])
        else:
            self.fill_buffer(13, 3, MODE[mode])

        if state == STATE['OFF']:
            self.fill_buffer(16, 4, 0)
        else:
            self.fill_buffer(16, 4, temperature - TEMPERATURE_OFFSET)

        self.fill_buffer(20, 1, 0) # jet

        if state == STATE['OFF']:
            self.fill_buffer(21, 3, FAN['NONE'])
        else:
            self.fill_buffer(21, 3, FAN[fan])

        self.fill_buffer(24, 4, self.crc)
        self.codes[BUFFER_SIZE - 1] = ZERO_AND_ONE_HIGH

    def fill_buffer(self, pos, bits, value):
        """
        Fill buffer
        """
        i = bits
        while i > 0:
            index = 2 + 2 * (pos + bits-i)
            self.codes[index] = ZERO_AND_ONE_HIGH

            if test_bit(value, i - 1) != 0:
                self.codes[index + 1] = ONE_LOW
            else:
                self.codes[index + 1] = ZERO_LOW

            if test_bit(value, i - 1) != 0:
                bitset = 0
                bitset = set_bit(bitset, (128 + i - pos - bits - 1) % 4)
                self.crc = self.crc + bitset

            i -= 1


    def debug(self):
        """
        Dump buffer
        """
        print self.codes[0:BUFFER_SIZE]
