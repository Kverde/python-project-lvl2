#!/usr/bin/env python3

"""Gendiff script."""

import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def main():
    """Run script."""
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # args = parser.parse_args()


if __name__ == '__main__':
    main()
