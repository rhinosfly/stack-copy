"""the logic behind cut/copy/paste"""


import shutil
from stacking import Stack
from pathlib import Path


def copy(stack: Stack, path: Path):
    # TODO: add optional backup; currently just stores path
    # TODO: add optional larger stack, currently clears every time
    # TODO: check path validity
    # clear stack
    stack.stack = []
    # push path to stack
    stack.push(path.absolute())


def paste(stack: Stack, destination: Path|None):
    # check if stack is empty
    if len(stack.stack) < 1:
        return
    # peek stack into src
    src: Path = stack.peek()
    # get dst
    if destination is None:
        destination = src.name()
    # copy from src to dst
    shutil.copy(src, destination)

def cut(stack: Stack, path: Path):
    print("cut is unimplemented")
