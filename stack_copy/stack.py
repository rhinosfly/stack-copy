"""module for manipulating a stack of directories"""

from pathlib import Path

class Stack:
    """a stack oject"""

    def __init__(self, path: Path):
        create_dir_if_dne(path)
        self.path = path
        self.stack: list[Path] = []

    def push(self, path: Path):
        pass
    
    def pop(self, path: Path):
        pass

def create_dir_if_dne(path: Path):
    path.mkdir(parents=True, exist_ok=True)
