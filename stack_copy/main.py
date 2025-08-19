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


def parse_args(program: Metadata) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=program.name, description=program.description, epilog=program.epilogue)
    parser.add_argument("src", help="path to copy")
    parser.add_argument("dst", help="path to paste to")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
