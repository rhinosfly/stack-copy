#!/usr/bin/env python3
"""program entry point of stack-copy"""

import argparse
from dataclasses import dataclass

@dataclass
class Metadata:
    name = "scp"
    description = "a cross platform python shell utility for gui-like copy-pasting using a temporary directory as a stack"
    version = "0.0.0"
    epilogue = ""

def main():
    metadata = Metadata()
    args = parse_args(metadata)
    _ = args


def parse_args(program: Metadata) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=program.name, description=program.description, epilog=program.epilogue)
    # subparsers
    subparsers = parser.add_subparsers(help="subcommand help")
    ## copy
    copy = subparsers.add_parser("copy", help="copy a file or directory")
    copy.add_argument("PATH", help="path to copy")
    ## cut
    cut = subparsers.add_parser("cut", help="cut a file or directory")
    cut.add_argument("PATH", help="path to copy")
    ## paste
    paste = subparsers.add_parser("paste", help="paste a copied file or directory")
    paste.add_argument("-o", "--output", metavar="PATH", help="output path name")
    # parse args
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
