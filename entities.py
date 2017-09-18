#!/usr/bin/env python3

"""Main entity framework."""

from modules import file_operations as io
import argparse

parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
parser.add_argument("-c", "--create", help="Create new entity.",
                    action="store", default="draf_entity")
parser.add_argument("-r", "--read", help="Read entity.")
parser.add_argument("--update", help="Update entity.")
parser.add_argument("--delete", help="Delete entity.")
parser.add_argument("-a", "--am",
                    help="Create adverse media template.",
                    action="store_true")
parser.add_argument("-i", "--id",
                    help="Entity ID",
                    action="store_true")
parser.add_argument("-p", "--pep",
                    help="Create PEP template",
                    action="store_true")


option = parser.parse_args()

if option.create and not option.pep or option.am:
    print("Creating entity:", option.create)
elif option.create and option.am:
    print("Creating adverse media entity:", option.create)
elif option.create and option.pep:
    print("Creating PEP entity:", option.create)
elif option.create and option.pep and option.am:
    print("Creating AM/PEP entity:", option.create)
else:
    print("WIP")