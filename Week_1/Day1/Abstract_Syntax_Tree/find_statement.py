import ast

class PrintChecker(ast.NodeVisitor):

    def visit_Call(self, node):

        if (
            isinstance(node.func, ast.Name)
            and node.func.id == "print"
        ):
            print("Print statement found")

        self.generic_visit(node)
        
node = ast.parse('print("hello")')
x = PrintChecker()
x.visit(node)