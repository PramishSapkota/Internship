import ast
code = '''
def greet(name):
    print("Hello, " + name + "!")
    
greet("John")
'''
tree = ast.parse(code)
print(ast.dump(tree, indent = 2))

'''
O/p:
Module(
  body=[
    FunctionDef(
      name='greet',
      args=arguments(
        args=[
          arg(arg='name')]),
      body=[
        Expr(
          value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
              BinOp(
                left=BinOp(
                  left=Constant(value='Hello, '),
                  op=Add(),
                  right=Name(id='name', ctx=Load())),
                op=Add(),
                right=Constant(value='!'))]))]),
    Expr(
      value=Call(
        func=Name(id='greet', ctx=Load()),
        args=[
          Constant(value='John')]))])
'''