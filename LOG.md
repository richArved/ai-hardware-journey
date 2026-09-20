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
