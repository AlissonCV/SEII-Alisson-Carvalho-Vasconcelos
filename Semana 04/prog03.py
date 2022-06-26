#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("quadrado", help="quadrado de um número", type=int)
args = parser.parse_args()

print("\n")
print(args.quadrado**2)
print("\n")

