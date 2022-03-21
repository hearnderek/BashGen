def expand(v: str) -> str:
    return "${" + v + "}"

def expandList(xs: str) -> str:
    return "${" + xs + "[@]}"

def toBashExpression(arthExpr: str) -> str:
    return "$(( " + arthExpr + " ))"