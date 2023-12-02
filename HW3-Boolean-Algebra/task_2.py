import math


def print_function(result: str):
    arity = math.ceil(math.log2(len(result)))
    alphabet = []
    for i in range(ord('a'), ord('z') + 1):
        alphabet.append(chr(i))

    for letter in range(0, arity):
        print("|", alphabet[letter], end=" ")
    print("| F |")
    print((arity + 1) * "|---" + "|")
    for bits in range(0, pow(2, arity)):
        b = ('0' * (arity - len(bin(bits)[2:]))) + bin(bits)[2:]
        for i in b:
            print("|", i, end=" ")
        print("|", result[bits], "|")


# prints N-th function boolean table in markdown style
def print_nth_function(arity: int, n: int):
    length = 2**arity
    bin_f = bin(n)[2:]
    bin_f = ('0' * (length - len(bin_f))) + bin_f
    print(f"F = {bin_f}")
    print_function(bin_f)


def main():
    arity = int(input("Input function arity: "))
    n = int(input("Input function number (0 -> 1): "))
    print(f"({arity})F_{n}")
    print_nth_function(arity, n)


if __name__ == "__main__":
    main()
