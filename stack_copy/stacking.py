"""module for manipulating a generic stack"""

from pathlib import Path
from typing import Any
import json

class Stack:
    """a generic stack

    only in program memory until loaded or dumped"""

    def __init__(self, file: Path):
        self.stack: list[Any] = []
        create_dir(file.parent)
        create_file(file)
        self.file  = file

    def push(self, thing: Any):
        self.stack.append(thing)
    
    def pop(self) -> Any:
        return self.stack.pop()

    def peek(self) -> Any:
        return self.stack[-1]

    def load(self, file: Path|None = None):
        if file is None:
            file = self.file
        with open(file) as f:
            stack_str = json.load(f)
        stack_path = [Path(x) for x in stack_str]
        self.stack = stack_path

    def dump(self, file: Path|None = None) :
        if file is None:
            file = self.file
        stack_str = [str(x) for x in self.stack]
        with open(file, "w") as f:
            json.dump(stack_str, f)


def create_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def create_file(path: Path):
    if path.exists():
        return
    with open(path, 'w') as file:
        file.write("[]")
