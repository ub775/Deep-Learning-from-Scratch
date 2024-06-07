from AND import AND
from OR import OR
from NAND import NAND

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

def main():
    print("x1 x2 output")
    for x in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"{x[0]}  {x[1]}   {XOR(x[0], x[1])}")

if __name__ == '__main__':
    main()