"""the logic behind cut/copy/paste"""


import shutil
from stack import Stack
from pathlib import Path


def copy(stack: Stack, path: Path):
    # TODO: add optional backup; currently just stores path
    # TODO: add optional larger stack, currently clears every time
    # TODO: check path validity
    # clear stack
    stack.stack = []
    # push path to stack
    stack.push(path)


def paste(stack: Stack, destination: Path):
    # peek stack into src
    src: Path = stack.peek()
    # copy from src to dst
    shutil.copy(src, destination)

def cut(stack: Stack, path: Path):
    print("cut is unimplemented")