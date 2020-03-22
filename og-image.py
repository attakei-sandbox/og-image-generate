#!/usr/bin/env python
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("source", help="Source URL")
parser.add_argument("-o", "--out", help="Output path")


def main(args: argparse.Namespace):
    pass


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
