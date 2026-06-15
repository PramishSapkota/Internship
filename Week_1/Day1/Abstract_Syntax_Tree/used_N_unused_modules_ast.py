import ast

code = """
import math
import numpy

print(math.sqrt(16))
"""

tree = ast.parse(code)
print(ast.dump(tree,indent=2))

imports = set()
used = set()

for node in ast.walk(tree):

    if isinstance(node, ast.Import):
        for alias in node.names:
            imports.add(alias.name)

    elif isinstance(node, ast.Name):
        used.add(node.id)

print("Imports:", imports)
print("Used:", used)
print("Unused:", imports - used)