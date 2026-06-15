import ast

code = "x = 5 + 3"
tree = ast.parse(code)

# print(ast.dump(tree, indent=2))

'''
O/p:
Module(
  body=[
    Assign(
      targets=[
        Name(id='x', ctx=Store())],
      value=BinOp(
        left=Constant(value=5),
        op=Add(),
        right=Constant(value=3)))])
'''

compiled  = compile(tree,'<string>', mode='exec')
print(type(compiled))
print(dir(compiled ))