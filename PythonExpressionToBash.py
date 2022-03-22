import ast
from typing import List
#from os import system

def main():
    PythonExpressionToRegisterBash("a = 10")
    print()

    PythonExpressionToRegisterBash("a = -10")
    print()
    
    PythonExpressionToRegisterBash("a = 10 + 20")
    print()
    
    PythonExpressionToRegisterBash("a = (10 + 20 + 30 + 40) / 4")
    print()

    PythonExpressionToRegisterBash("a = (10 + 20 + 30 + 40) // 4")
    print()

    PythonExpressionToRegisterBash("a = (-10 + 20 + 30 + 40) / 4")
    print()

    PythonExpressionToRegisterBash("a = (-10 + 20 + -(30) + 40) / 4")
    print()


    PythonExpressionToRegisterBash("a = -((-10 + 20 + -(30) + 40) / 4)")
    PythonExpressionToRegisterBash("a = -(-((-10 + 20 + -(30) + 40) / 4))")
    print()

    PythonExpressionToRegisterBash("a = a + b")
    print()

    PythonExpressionToRegisterBash("a = b + c")
    print()

    PythonExpressionToRegisterBash("a = b ** c")
    print()

    PythonExpressionToRegisterBash("a = b % c")
    print()

def PythonExpressionToRegisterBash(expr: str):
    print("# genfrom:", expr)
    astm = ast.parse(expr, mode="exec")
    #print(ast.dump(astm, indent=2))

    visit(astm)
    #print("echo bash $x")
    #print("echo python", int(eval(expr)))


def visit(node):
    
    node_type = type(node)
    # print()
    # print(str(type(node)))

    visit_switch = {
        ast.Module: visit_module,
        list: visit_list,
        ast.Assign: visit_assign,
        ast.Expr: visit_expr,
        ast.Name: visit_name,
        ast.UnaryOp: visit_unaryop,
        ast.USub: visit_usub,   
        ast.UAdd: visit_uadd,   
        ast.BinOp: visit_binop,
        ast.Add: visit_opadd,
        ast.Sub: visit_opsub,
        ast.Mult: visit_opmult,
        ast.Div: visit_opdiv,
        ast.FloorDiv: visit_opfloordiv,
        ast.Pow: visit_oppow,
        ast.Mod: visit_opmod,
        ast.Constant: visit_constant
    }

    visit_switch[node_type](node)

def visit_module(module: ast.Module):
    visit(module.body)
    print()

def visit_list(ls: List):
    for x in ls:
        visit(x)

def visit_assign(assign: ast.Assign):
    if len(assign.targets) > 1:
        raise Exception("Multiple assignments not supported")
    
    complexvalue = assign.value is not ast.Constant
    
    id: ast.Name = assign.targets[0]
    if complexvalue:
        visit(assign.value)    
        print()
        print(str(id.id)+"=$x;")
    else:
        print(str(id.id)+"=", end="")
        visit(assign.value)
        print(";")

def visit_expr(expr: ast.Expr):
    visit(expr.value)


def visit_name(name: ast.Name):
    print("$" + str(name.id), end="")

def visit_unaryop(unaryop: ast.UnaryOp):
    """
    UnaryOp := USub operand
            |  UAdd operand
            ;
    
    operand := Constant
            |  UnaryOp
            |  BinOp
    """

    complexoperand = unaryop.operand is not ast.Constant

    if complexoperand:
        visit(unaryop.operand)
        print("x=$(( ", end="")
        visit(unaryop.op)
        print(" $x ));", end="")
    else:
        print("x=$(( ", end="")
        visit(unaryop.op)
        visit(unaryop.operand)
        print(" ));", end="")

def visit_usub(usub: ast.USub):
    print("-", end="")

def visit_uadd(opsub: ast.UAdd):
    print("", end="")

def visit_binop(binop: ast.BinOp):
    """
    ast.BinOp := left op right;

    left := ast.Constant
         |  ast.BinOp
         |  ast.UnaryOp
         ;

    right := ast.Constant
          |  ast.UnaryOp
          ;
    """
    complexleft = not type(binop.left) in (ast.Constant, ast.Name)
    complexright = not type(binop.right) in (ast.Constant, ast.Name)
    

    if complexleft and complexright:
        visit(binop.right)
        print("y=$x;", end="")
        visit(binop.left)
        print("x=$(( $x ", end="")
        visit(binop.op)
        print(" $y ));", end="")
    elif complexleft:
        visit(binop.left)
        print("x=$(( $x", end="")
        visit(binop.op)
        visit(binop.right)
        print(" ));", end="")
    elif complexright:
        visit(binop.right)
        print("x=$(( ", end="")
        visit(binop.left)
        visit(binop.op)
        print(" $x ));", end="")
    else:
        print("x=$(( ", end="")
        visit(binop.left)
        visit(binop.op)
        visit(binop.right)
        print(" ));", end="")

def visit_opadd(opadd: ast.Add):
    print("+", end="")

def visit_opsub(opsub: ast.Sub):
    print("-", end="")

def visit_opmult(opmult: ast.Mult):
    print("*", end="")

def visit_opdiv(opdiv: ast.Div):
    print("/", end="")

def visit_opfloordiv(opfloordiv: ast.FloorDiv):
    print("/", end="")

def visit_oppow(oppow: ast.Pow):
    print("**", end="")

def visit_opmod(opmod: ast.Mod):
    print("%", end="")

def visit_constant(constant: ast.Constant):
    print(constant.value, end="")


if __name__ == '__main__':
    main()
