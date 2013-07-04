from drunken_bishop import hex_byte_to_binary
from drunken_bishop import bit_pairs


def test_hex_byte_to_binary():
    assert hex_byte_to_binary('00') == '00000000'
    assert hex_byte_to_binary('01') == '00000001'
    assert hex_byte_to_binary('10') == '00010000'
    assert hex_byte_to_binary('d4') == '11010100'
    assert hex_byte_to_binary('ff') == '11111111'


def test_bit_pairs():
    assert bit_pairs('10101100') == ['00', '11', '10', '10']
    assert bit_pairs('00011011') == ['11', '10', '01', '00']
