'''
A future is an object that wraps a function call. That function call is run in 
the background, in a thread or a separate process. The future object has methods to 
check whether the computation has completed and to get the results. We can think 
of it as a computation where the results will arrive in the future, and we can do 
something else while waiting for them.
'''
import ast
from typing import NamedTuple, Set
from pathlib import Path

class ImportResult(NamedTuple):
    path:Path
    imports: Set[str]

    @property
    def focus(self) -> bool:
        return 'typing' in self.imports
    
class ImportVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.imports:Set[str] = set()

    def visit_Import(self, node: ast.Import) -> None:
        for alais in node.names:
            self.imports.add(alais.name)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module:
            self.imports.add(node.module)

def find_imports(path:Path) -> ImportResult:
    tree = ast.parse(path.read_text())
    iv = ImportVisitor()
    iv.visit(tree)
    return ImportResult(path, iv.imports)