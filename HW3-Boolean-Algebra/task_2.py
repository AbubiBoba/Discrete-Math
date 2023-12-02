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


def invert(s: str) -> str:
    s = s.replace("\\land", "###")
    s = s.replace("\\lor", "\\land")
    s = s.replace("###", "\\lor")
    alphabet = []
    for i in range(ord('A'), ord('Z') + 1):
        alphabet.append(chr(i))
    for letter in alphabet:
        s = s.replace("\\overline{" + letter + "}", '#')
        s = s.replace(letter, "\\overline{" + letter + "}")
        s = s.replace('#', letter)
    return s


def main():
    print("'n' if you want to work with nth function")
    print("'v' to work with function vector")
    print("'xor' to xor")
    print("'->' to work with CNF constructor-inverter")
    m = input("Input mode: ")
    if m == 'n':
        arity = int(input("Input function arity: "))
        n = int(input("Input function number (0 -> 1): "))
        print(f"({arity})F_{n}")
        print_nth_function(arity, n)
    elif m == 'v':
        res = input("Input vector: ")
        print("F =", res)
        print_function(res)
    elif m == 'xor':
        a, b = map(int, input("Enter a and b to xor: ").split())
        print(a ^ b)
    elif m == "->":
        s = input("input latex formula to invert:\n")
        print(invert(s))


if __name__ == "__main__":
    main()
