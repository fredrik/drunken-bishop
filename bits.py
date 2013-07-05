import itertools

def hex_byte_to_binary(hex_byte):
    """
    Convert a hex byte into a string representation of its bits,
    e.g. 'd4' => '11010100'
    """
    assert len(hex_byte) == 2
    dec = int(hex_byte, 16)
    return bin(dec)[2:].zfill(8)


def bit_pairs(binary):
    """
    Convert a word into bit pairs little-endian style.
    '10100011' => ['11', '00', '10', '10']
    """
    def take(n, iterable):
        "Return first n items of the iterable as a list"
        return list(itertools.islice(iterable, n))
    def all_pairs(iterable):
        while True:
            pair = take(2, iterable)
            if not pair:
                break
            yield ''.join(pair)
    pairs = list(all_pairs(iter(binary)))
    return list(reversed(pairs))
