# Day 7: From Truth Tables to SOP and POS

## What I did

This learning day ended up taking about one and a half days. I learned how to use minterms and maxterms, what canonical SOP and POS mean, and how to calculate row indices from the input bits. I also drew logic-gate circuits from Boolean expressions and learned about Majority3 and XOR3 as test functions. To finish, I worked through a Python tool that turns a truth table into SOP and POS expressions and checked its output.

## What I understood

A minterm combines all input variables using AND. Each variable appears once, either negated or not negated. The minterm is 1 for exactly one row of the truth table. A maxterm combines all input variables using OR and is 0 for exactly one row.

Canonical SOP (Sum of Products) connects the minterms of the rows where the output is 1 using OR. Canonical POS (Product of Sums) connects the maxterms of the rows where the output is 0 using AND.

Majority3 outputs 1 when at least two of the three inputs are 1. XOR3 outputs 1 when an odd number of its three inputs are 1.

## Results and checks

In the expressions below, `!` means NOT, `*` means AND, and `+` means OR.

**Exercise 7**

```text
SOP: A * !B + A * B
POS: (A + B) * (A + !B)
```

**Exercise 8a**

```text
Majority3 SOP: !A * B * C + A * !B * C + A * B * !C + A * B * C
Majority3 POS: (A + B + C) * (A + B + !C) * (A + !B + C) * (!A + B + C)

XOR3 SOP: !A * !B * C + !A * B * !C + A * !B * !C + A * B * C
XOR3 POS: (A + B + C) * (A + !B + !C) * (!A + B + !C) * (!A + !B + C)
```

## Special cases and invalid inputs

| Test case | Expected result | Actual result |
| --- | --- | --- |
| All outputs are 0 | `"0"` | `"0"` |
| All outputs are 1 | `"1"` | `"1"` |
| One variable, outputs `[0, 1]` | Function A | `"A"` |

The invalid-input checks also behaved as expected:

- Three output values for two variables raised `ValueError`.
- An output value of 2 raised `ValueError`.
- An empty list of input variables raised `ValueError`.

## Open questions and review

On paper, the logic behind minterms and maxterms makes a lot of sense to me. The same goes for SOP and POS. What I still find difficult is expressing these steps correctly in Python syntax.

Sometimes I mix up SOP and POS, often because I am not paying enough attention. I want to review these points again on Saturday.
