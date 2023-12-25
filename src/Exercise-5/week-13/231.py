# Unary and Binary Operators
# (Solved, 45 Lines)
'''Some mathematical operators are unary while others are binary. Unary operators act
on one value while binary operators act on two. For example, in the expression 2 *
-3 the * is a binary operator because it acts on both the 2 and the −3 while the - is
a unary operator because it only acts on the 3.

An operator’s symbol is not always sufficient to determine whether it is unary or
binary. For example, while the - operator was unary in the previous expression, the
same character is used to represent the binary - operator in an expression such as
2 - 3. This ambiguity, which is also present for the + operator, must be removed
before other interesting operations can be performed on a list of tokens representing
a mathematical expression.

Create a function that identifies unary + and - operators in a list of tokens and
replaces them with u+ and u- respectively. Your function will take a list of tokens
for a mathematical expression as its only parameter and return a new list of tokens
where the unary + and - operators have been substituted as its only result. A +
or - operator is unary if it is the first token in the list, or if the token that imme-
diately precedes it is an operator or open parenthesis. Otherwise the operator is
binary.

Write a main program that demonstrates that your function works correctly by
reading, tokenizing, and marking the unary operators in an expression entered by
the user. Your main program should not execute when your function is imported into
another program.
'''