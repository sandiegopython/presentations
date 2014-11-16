import os


def print_values(s):
    for c, val in zip(s.upper(), values_from_str(s)):
        print "{c}({val})".format(c=c, val=val),


def generate_key(byte_count=10):
    return os.urandom(byte_count)


def xor_strings(message, key):
    bytes1, bytes2 = bytearray(message), bytearray(key)
    return str(bytearray(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)))


def values_from_str(s):
    return [ord(c) for c in s.upper()]
