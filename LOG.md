Goal: Build a solid understanding of AI hardware. Design working custom chips (ASICs) and check that the hardware works correctly.
Motivation: Understand how hardware works instead of seeing it as a black box.

## Week 1 — Learning Days 1–6 · Module 0

**Milestone M0.1:** achieved, with an additional experiment on transistor width and switching time.

### What I built

- Days 1–2: Notes about the semiconductor industry and the different steps from designing a chip to producing it.
- Day 3: Several ngspice circuits, including voltage dividers and RC charging and discharging experiments.
- Day 4: Python functions and tests for binary and hexadecimal numbers, two's complement, and overflow.
- Day 5: Logic circuits built from NAND gates and truth tables to check De Morgan's laws.
- Day 6: A CMOS inverter and a NAND circuit, with simulation data and plots. I also compared the NAND's fall time with two different nMOS widths in `Aufgabe_6_Detail.cir`.

### What I understand now

- I have a first overview of the semiconductor industry and how the different companies and production steps fit together.
- I can simulate simple circuits in ngspice and read voltage-divider results and capacitor charging curves.
- I understand how to convert binary, hexadecimal, and decimal numbers, how negative numbers are stored using two's complement, and how to recognise overflow.
- I understand the basic logic gates, HIGH and LOW voltage ranges, and how much disturbance a signal can tolerate.
- I understand why the pMOS transistors in a CMOS NAND are connected in parallel and the nMOS transistors in series. I can follow the path from the output to the supply or to ground.
- In our inverter model, the pMOS is made wider to balance the difference between the pMOS and nMOS models.
- I used the SPICE measurement command to compare how quickly the NAND output falls. With both nMOS widths changed from 1 µm to 2 µm, the fall time dropped from about 226 ns to 118 ns. That is approximately half, not exactly half.

### What I still want to practise

- I am still unsure about some ngspice commands and want to become more comfortable writing and explaining them myself.
- I want to understand the complete Python plotting process, from reading the data to creating the graph with matplotlib.
- I understand the graphs and numbers, but sometimes it is difficult to write down exactly what I mean. I want to use clearer and more precise wording.
- I still need some practice with De Morgan's laws and Boolean algebra, especially when simplifying expressions on my own.
- I want to practise identifying Drain, Gate, Source, and Body in a circuit and their order in a SPICE transistor line. I want to know this by heart without having to look it up.

### Main takeaway

A truth table tells me which logic value the output should have. The transistor circuit helps me understand how that value is produced. In the simulation, I can also see that the voltage does not change instantly. The output capacitor needs time to charge or discharge, and changing the transistor width changes how quickly that happens.

## Weekly review — Learning Days 8–9 · September 27, 2026

### What I built and practised

- I simplified ten Boolean functions using Karnaugh maps and checked the results with `qm_referenz.py`.
- I worked with Gray-code order, prime implicants and don't-cares, and learned the steps of the Quine–McCluskey algorithm.
- I built a 2:1 multiplexer, a 4:1 multiplexer from gates, and a 4:1 multiplexer from three 2:1 multiplexers.
- I also built a 3:8 decoder, an 8:3 priority encoder, and Majority3 and XOR3 using multiplexers.
- During the Day 9 write-up, Codex ran the embedded Digital tests: all 8 rows passed for the 2:1 multiplexer and all 256 rows passed for the priority encoder. The later full test run also passed all 64 rows for each 4:1 multiplexer and all 8 decoder rows. Majority3 and XOR3 each failed all 8 rows because their outputs are inverted; these two circuits still need correcting.

### What improved

I can now apply many Boolean algebra rules from memory without looking them up. The exercises on paper generally feel easy, and I understand better how to turn a Boolean expression into a circuit.

I also understand how a multiplexer selects an input, how a decoder selects an output, and how a priority encoder handles several active inputs.

### What I still want to practise

- I need to check my wiring more carefully. I still make careless mistakes when I try to move too quickly.
- Python is still the hardest part for me. My own `qm_lernversion.py` is still a scaffold; `combine` and `covers` remain open. They were planned for Saturday, but completion is not yet documented.
- I want to review Quine–McCluskey and correct Majority3 and XOR3 and rerun their tests.
- I plan to spend an extra 10–15 minutes each day practising Python. After Module 1, I want to revisit the sections I have marked and rewrite them with what I have learned by then.

### How this week went

Day 9 took much longer than planned because I got sick. I could not concentrate for long periods, so I worked through small parts each day until I finished the exercises on Sunday. I do not find the topic itself particularly complicated, but I still need some review and more careful checking.

I also spent too much time trying to get the Day 8 Python script and syntax perfect. I need a clearer stopping point so that I can come back to difficult parts later without holding up everything else.

### Next steps

Correct and retest the two inverted Day 9 circuits, continue the short Python practice sessions, and move on to Day 10. The Day 10 materials are prepared, but I have not completed that learning day yet.

### Main takeaway

Understanding the logic, writing the Python code and wiring the circuit are different skills. I can understand a solution on paper and still need help implementing it. I want to keep practising each part and be clear about what I have done myself and what still needs work.
