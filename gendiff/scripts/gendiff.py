#!/usr/bin/env python3

"""Gendiff script."""

from gendiff.diff import generate_diff
import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def main():
    """Run script."""
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    res = generate_diff(args.first_file, args.second_file)
    print(res)


if __name__ == '__main__':
    main()
