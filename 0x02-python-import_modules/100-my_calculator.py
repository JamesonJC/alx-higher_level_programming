#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    op = sys.argv[len(sys.argv) - 2]
    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if (op == '+'):
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, add(a, b)))
    elif (op == '-'):
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, sub(a, b)))
    elif (op == '*'):
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, mul(a, b)))
    elif (op == '/'):
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, div(a, b)))
