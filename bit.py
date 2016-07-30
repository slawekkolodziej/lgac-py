def test_bit(num, offset):
    """
    Test the num(int) if at the given offset bit is 1
    """
    mask = 1 << offset
    return num & mask

def set_bit(num, offset):
    """
    Set bit to at the given offset to 1
    """
    mask = 1 << offset
    return num | mask
