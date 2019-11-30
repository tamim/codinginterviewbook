def is_redundant(expr):
    stack = []

    for item in expr:
        if item in "(+-*/":
            stack.append(item)
        elif item in ")":
            last_item = stack.pop()
            if last_item == "(":
                return True
            while "(" != stack.pop():
                continue
    return False

if __name__ == "__main__":
    expr = "a + b"
    print(expr, is_redundant(expr))

    expr = "(a)"
    print(expr, is_redundant(expr))

    expr = "(a + b + c)"
    print(expr, is_redundant(expr))


    expr = "((a + b + c + d + e))"
    print(expr, is_redundant(expr))