"""
Library that genrates LG air conditioner remote codes
"""

from bit import setBit, testBit

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

class LGAC(object):
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
        pass

    def debug(self):
        """
        Dump buffer
        """
        pass

    def fill_buffer(self, pos, bits, value):
        """
        Fill buffer
        """
        i = bits
        while i > 0:
            index = 2 + 2 * (pos + bits-i)
            self.codes[index] = ZERO_AND_ONE_HIGH

            if testBit(value, i - 1) != 0:
                self.codes[index + 1] = ONE_LOW
            else:
                self.codes[index + 1] = ZERO_LOW

            if testBit(value, i - 1) != 0:
                bitset = 0
                bitset = setBit(bitset, (128 + i - pos - bits - 1) % 4)
                self.crc = self.crc + bitset

            i -= 1
