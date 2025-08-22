"""module for manipulating a generic stack"""

from pathlib import Path
from typing import Any

class Stack:
    """a generic stack"""

    def __init__(self):
        self.stack: list[Any] = []

    def push(self, thing: Any):
        self.stack.append(thing)
    
    def pop(self) -> Any:
        return self.stack.pop()

    def peek(self) -> Any:
        return self.stack[-1]

def create_dir_if_dne(path: Path):
    path.mkdir(parents=True, exist_ok=True)
