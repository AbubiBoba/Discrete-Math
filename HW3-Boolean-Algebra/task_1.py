import hashlib
import math
from enum import Enum

class Base(Enum):
    HEX = 16
    DEC = 10
    BIN = 2

def get_hash(s : str, base : Base = Base.BIN) -> str:
    s_utf8 = s.encode("UTF-8")
    hash_obj = hashlib.sha256(s_utf8)
    if base == Base.HEX:
        return hash_obj.hexdigest()
    if base == Base.DEC:
        return str(int(hash_obj.hexdigest(), 16))
    if base == Base.BIN:
        return bin(int(hash_obj.hexdigest(), 16))[2:].zfill(256)

def slice_hash(hash_to_slice: str, length_of_part: int) -> list:
    slices = []
    for i in range(1, (len(hash_to_slice) // length_of_part) + 1):
        slices.append(hash_to_slice[length_of_part * (i - 1): length_of_part * i])
    return slices

def print_Function(result: str):
    arity = math.ceil(math.log2(len(result)))
    alphabet = []
    for i in range(ord('a'), ord('z') + 1):
        alphabet.append(chr(i))

    for l in range(0, arity):
        print(alphabet[l], end=" | ")
    print("F")
    print((4 * arity + 1) * '-')
    for bits in range(0, pow(2, arity)):
        b = ('0' * (arity - len(bin(bits)[2:]))) + bin(bits)[2:]
        for i in b:
            print(i, end=" | ")
        print(result[bits])
        print((4 * arity + 1) * '-')

def main():
    s = "DM Fall 2023 HW3"

    print("SHA-256 hash")
    print(get_hash(s, base=Base.HEX))
    print(get_hash(s, base=Base.DEC))
    print(get_hash(s, base=Base.BIN))
    print("")

    h = get_hash(s, base=Base.BIN)

    print("Slices")
    for h_slice in slice_hash(h, 32):
        print(h_slice)
    print("")

    r = slice_hash(h, 32)
    d = 0
    for ri in r:
        d ^= int(ri, 2)

    magic = int("0x24d03294", 16)
    w = d ^ magic

    w = ('0' * (32 - len(bin(w)[2:]))) + bin(w)[2:]
    print("0x24d03294 XOR ri")
    print(w)
    print("")

    print_Function(w)

if __name__ == "__main__":
    main()
