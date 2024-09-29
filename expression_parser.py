import re
import itertools

def NOT(a):
    return not a

def AND(a ,b):
    return a & b

def OR(a, b):
    return a | b


def extract_vars(expression):
    return sorted(set(re.findall(r'[A-Za-z][A-Za-z0-9]*', expression)))

def parse_boolean_expression(expression):
    tokens = re.findall(r'[A-Za-z][A-Za-z0-9]*|[\&|!()]', expression)

    def evaluate_expression(tokens):
        def parse_literal():
            token = tokens.pop(0)
            if token == '(':
                result = parse_cube()
                tokens.pop(0)
                return result
            elif token == '!':
                return f'NOT({parse_literal()})'
            return token

        def parse_cube():
            result = parse_literal()
            while tokens and tokens[0] in '&|!':
                op = tokens.pop(0)
                if op == '&':
                    result = f'AND({result}, {parse_literal()})'
                elif op == '|':
                    result = f'OR({result}, {parse_literal()})'
            return result
        
        return parse_cube()
    
    return evaluate_expression(tokens)

def solve_bool_expression(expr, values):
    for var, value in values.items():
        expr = re.sub(rf'\b{var}\b', str(value), expr)
    return eval(expr)

def get_minterms(expression):
    minterms = []
    vars = extract_vars(expression)
    bool_expr = parse_boolean_expression(expression)
    tt_values = list(itertools.product([0, 1], repeat=len(vars)))

    for value in tt_values:
        vars_values = dict(zip(vars, value))
        if solve_bool_expression(bool_expr, vars_values):
            minterms.append(value)

    return minterms