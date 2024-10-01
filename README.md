# Quine-McCluskey Introduction

The Quine McCluskey algorithm is a systematic way used for minimizing Boolean expressions. It is more suitable for handling complex Boolean functions with more than 4 variables, where methods like Karnaugh maps become difficult.

## Expression Parser (Minterms Extractor Module)
The definition of the minterm is the term that makes boolean function output become true and we can represent any boolean function as the summation of its minterms.
1. In the following module we need to first give the script a correct boolean expression then we parse this expression to the formal form using the following  function with aid of basic functions like  ``NOT(a)``, ``AND(a,b)`` and ``OR(a,b)`` :
- `` parse_boolean_expression()``
```python
from expression_parser import parse_boolean_expression

print(parse_boolean_expression('(!A&B) | (A&!B)'))
# output will be --> OR(AND(NOT(a), B), AND(A, NOT(B)))
```
2. The second step will be to extract variables and try to substitute by their correspondent values according to the truth table and evaluate the expression and check if result is true then this combination is a minters for the function if not neglect it:
- ``get_minterms(expression)``
```python
from expression_parser import get_minterms

print(get_minterms("(!A&B) | (A&!B)"))
# output will be --> [(1, 0), (0, 1)]
```
## McCluskey Minimizer (Expression Minimization Module)
The main idea of this module is to divide the minterms to groups based on the number of 1's in each minterm and start the comparison between minterms that differs in only one bit to see if a literal can be removed and turn them prime implicants (the prime implicant is an implicant that cannot be further reduced or combined with other implicants).

1. The core part of the Quine-McCluskey algorithm to find the prime implicants for a given set of Boolean minterms. The function takes a list of binary tuples representing the minterms and returns a list of prime implicants in binary tuple form.
- ``find_prime_implicants(minterms)``
```python
from expression_parser import get_minterms

expression = 'A|B'
prime_implicants = find_prime_implicants(get_minterms(expression))
print(prime_implicants)
# 'x' represent a don't care
# output will be --> [('x', 1), (1, 'x')]
```

2. This function converts any set of prime implicants into a human-readable Sum of Products form using the provided variable names.
- ``prime_implicants_to_sop(prime_implicants, variables)``
```python
from expression_parser import get_minterms, extract_vars

expression = 'A|B'
vars = extract_vars(expression)
prime_implicants = find_prime_implicants(get_minterms(expression))
sop = prime_implicants_to_sop(prime_implicants, vars)
print(sop)
# output will be --> B + A
```

### Overall Running Script
```shell
$python3 maccluskey_minimization.py '(A&B&C)|(!A&B&C)|(A&!B&C)|(A&B&!C)'
# output will be --> The minimized (SOP) expression: BC + AC + AB
```


## Time Complexity Issues
The overall time complexity is dominated by the prime implicant extraction step which is **O(N^2)** but the worst case complexity for Boolean minimization problems (in general) is exponential **O(2^M)**. This makes Quine-McCluskey less efficient for large numbers of variables which is why heuristic algorithms like **Espresso** (I am going to implement it soon) are often used in practice for larger problems.