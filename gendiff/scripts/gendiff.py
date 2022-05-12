#!/usr/bin/env python3

"""Gendiff script."""

from gendiff.diff_generator import generate_diff
from gendiff.formatter import format
import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def main():
    """Run script."""
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    res = format(diff)
    print(res)


if __name__ == '__main__':
    main()
