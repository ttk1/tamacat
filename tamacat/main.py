import sys
import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs='*', default=['-'])
    return parser


def cat(file):
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()


def process(file_name):
    if file_name == '-':
        cat(sys.stdin)
    else:
        with open(file_name, 'r') as file:
            cat(file)


def main():
    parser = get_parser()
    args = parser.parse_args()
    for file_name in args.FILE:
        process(file_name)
