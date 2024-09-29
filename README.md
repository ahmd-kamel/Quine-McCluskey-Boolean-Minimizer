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
# output will be --> [(True, False), (False, True)]