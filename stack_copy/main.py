#!/usr/bin/env python3
"""program entry point of stack-copy"""

import argparse
from dataclasses import dataclass
import stacking
import files

@dataclass
class Metadata:
    name = "scp"
    description = "a cross platform python shell utility for gui-like copy-pasting using a temporary directory as a stack"
    version = "0.0.0"
    epilogue = ""

def main():
    # init constants
    metadata = Metadata()
    stack = stacking.Stack()
    # parse args
    args = parse_args(metadata)
    print(args)
    # execute funtion
    try:
        args.func
    except AttributeError:
        print("no function given")
    else:
        args.func(stack=stack, args=args)


def parse_args(program: Metadata) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=program.name, description=program.description, epilog=program.epilogue)
    # subparsers
    subparsers = parser.add_subparsers(title="subcommands", help="subcommand help")
    ## copy
    copier = subparsers.add_parser("copy", help="copy a file or directory")
    copier.set_defaults(func=copy)
    copier.add_argument("PATH", help="path to copy")
    ## cut
    cutter = subparsers.add_parser("cut", help="cut a file or directory")
    cutter.set_defaults(func=cut)
    cutter.add_argument("PATH", help="path to copy")
    ## paste
    paster = subparsers.add_parser("paste", help="paste a copied file or directory")
    paster.set_defaults(func=paste)
    paster.add_argument("-o", "--output", metavar="PATH", help="output path name")
    # parse args
    args = parser.parse_args()
    return args

def copy(stack: stacking.Stack, args: argparse.Namespace):
    files.copy(stack=stack, path=args.PATH)

def cut(stack: stacking.Stack, args: argparse.Namespace):
    files.cut(stack=stack, path=args.PATH)

def paste(stack: stacking.Stack, args: argparse.Namespace):
    files.paste(stack=stack, destination=args.output)

if __name__ == "__main__":
    main()
