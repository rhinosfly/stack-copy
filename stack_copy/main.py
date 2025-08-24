#!/usr/bin/env python3
"""program entry point of stack-copy"""

import argparse
from dataclasses import dataclass
from . import stacking
from . import files
from pathlib import Path

@dataclass
class Metadata:
    name = "scp"
    description = "a cross platform python shell utility for gui-like copy-pasting using a temporary directory as a stack"
    version = "0.0.0"
    epilogue = ""

@dataclass
class Config:
    stack_location = Path(Path.home()/".local/share/scp/stack.json")

def main():
    # init constants
    metadata = Metadata()
    config = Config()
    stack = stacking.Stack(config.stack_location)
    # parse args
    args = parse_args(metadata)
    # execute funtion
    args.func(stack=stack, args=args)


def parse_args(program: Metadata) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=program.name, description=program.description, epilog=program.epilogue)
    # subparsers
    subparsers = parser.add_subparsers(title="subcommands", help="subcommand help", required=True)
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
    stack.load()
    files.copy(stack=stack, path=Path(args.PATH))
    stack.dump()

def cut(stack: stacking.Stack, args: argparse.Namespace):
    stack.load()
    files.cut(stack=stack, path=Path(args.PATH))
    stack.dump()

def paste(stack: stacking.Stack, args: argparse.Namespace):
    stack.load()
    files.paste(stack=stack, destination=Path(args.output))
    stack.dump()

if __name__ == "__main__":
    main()
