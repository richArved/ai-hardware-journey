# Day 8: Karnaugh Maps and Logic Minimization

## What I did

I learned how to simplify Boolean expressions using Karnaugh maps and how the Quine–McCluskey algorithm works. I worked through the exercises on paper and compared the results with the Python checker `qm_referenz.py`.

## What I understood

I understand the Gray-code order and why neighboring cells differ in only one input bit. I also feel confident working with prime implicants and don't-cares.

What stood out to me is that I can now apply many Boolean algebra rules from memory without looking them up. The exercises I solve by hand on paper generally feel very easy to me.

## My ten results and checks

In the expressions below, `!` means NOT, `*` means AND, and `+` means OR. A `-` in a pattern means that the input can be either 0 or 1.

The Python checker `qm_referenz.py` confirmed all specified truth-table rows for each case. Don't-care rows do not have a required output value.

| Case | Simplified SOP | Patterns | Terms | Literals | All specified rows checked? |
| --- | --- | --- | --- | --- | --- |
| 1 | `!A * !B` | `['00-']` | 1 | 2 | Yes |
| 2 | `B` | `['-1-']` | 1 | 1 | Yes |
| 3 | `!A * !C + A * C` | `['0-0', '1-1']` | 2 | 4 | Yes |
| 4 | `C + A * B` | `['--1', '11-']` | 2 | 3 | Yes |
| 5 | `!A * !B * C + !A * B * !C + A * !B * !C + A * B * C` | `['001', '010', '100', '111']` | 4 | 12 | Yes |
| 6 | `!B * !D` | `['-0-0']` | 1 | 2 | Yes |
| 7 | `!B` | `['-0--']` | 1 | 1 | Yes |
| 8 | `C * !D + !B * !C + !A * B * D` | `['--10', '-00-', '01-1']` | 3 | 7 | Yes |
| 9 | `!C` | `['--0']` | 1 | 1 | Yes |
| 10 | `D` | `['---1']` | 1 | 1 | Yes |

## Python and where I needed help

My biggest difficulty right now is translating the steps into Python. I can use very basic Python syntax to solve certain problems, but more compact code is still difficult for me to understand. I needed help working through the script and a version with simpler syntax.

My own `qm_lernversion.py` is still only a scaffold. `combine` and `covers` are still open and moved to Saturday.

I want to spend an extra 10–15 minutes each day reviewing Python. After Module 1, I plan to revisit the Python sections I have marked and rewrite them more compactly using what I have learned by then.

## Open questions and review

I still want to move quickly, and that sometimes leads to careless mistakes. I need to take enough time to check my work.

At the same time, I spent another day longer than planned trying to get the Python script and syntax just right. In the future, I need to set a clearer stopping point and come back to the difficult parts later instead of trying to get everything perfect straight away.

On Saturday, I will review the Quine–McCluskey algorithm and work on `combine` and `covers`. Tomorrow, I will move on to Day 9: multiplexers.
