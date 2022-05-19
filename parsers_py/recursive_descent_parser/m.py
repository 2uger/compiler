import sys

from tokens import create_tokens, tokens
from recursive_descent_parser import parse, messages


def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print('Provide file name');
        return
    create_tokens(file_name)
    for t in tokens:
        print(t)
    parse(0)
    print(messages)

if __name__ == '__main__':
    main()
