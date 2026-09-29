# Day 9: Multiplexers, Decoders and Priority Encoders

## What I learned

I learned how a multiplexer is built and how it selects one of its data inputs. I also learned what encoders and decoders do, including how a priority encoder decides which input wins when several inputs are active.

I worked through different ways of building these components, including implementations using logic gates. I also built Majority3 and XOR3 using multiplexers.

## My circuits

The images below were exported directly from my saved Digital files. They show my actual wiring, not replacement example circuits. The images are snapshots of the files at the time of this write-up.

### 2:1 multiplexer

[Digital file](praxis/schaltungen/mux2to1.dig)

![My 2:1 multiplexer](praxis/abbildungen/mux2to1.svg)

### 4:1 multiplexer built from gates

[Digital file](praxis/schaltungen/mux4_gatter.dig)

![My 4:1 multiplexer built from gates](praxis/abbildungen/mux4_gatter.svg)

### 4:1 multiplexer built from three 2:1 multiplexers

[Digital file](praxis/schaltungen/3muxto4_gatter.dig)

![My 4:1 multiplexer built from three 2:1 multiplexers](praxis/abbildungen/3muxto4_gatter.svg)

### 3:8 decoder

[Digital file](praxis/schaltungen/decoder3_gatter.dig)

![My 3:8 decoder](praxis/abbildungen/decoder3_gatter.svg)

### 8:3 priority encoder

[Digital file](praxis/schaltungen/priority8_gatter.dig)

![My 8:3 priority encoder](praxis/abbildungen/priority8_gatter.svg)

### Majority3 using a multiplexer

[Digital file](praxis/schaltungen/majority3_mux.dig)

![My Majority3 circuit using a multiplexer](praxis/abbildungen/majority3_mux.svg)

### XOR3 using a multiplexer

[Digital file](praxis/schaltungen/XOR3_mux.dig)

![My XOR3 circuit using a multiplexer](praxis/abbildungen/XOR3_mux.svg)

## Results and checks

The saved circuits were checked against every input combination using Digital. The Python script [schaltungstests.py](praxis/schaltungstests.py) generates the missing test cases and runs the circuit tests. Detailed results are saved in [testergebnisse](praxis/testergebnisse/).

| Circuit | Test rows | Result |
| --- | --- | --- |
| 2:1 multiplexer | 8 | All passed. |
| 4:1 multiplexer built from gates | 64 | All passed. |
| 4:1 multiplexer built from three 2:1 multiplexers | 64 | All passed. |
| 3:8 decoder | 8 | All passed. |
| 8:3 priority encoder | 256 | All passed for Q2, Q1, Q0 and NONE. |
| Majority3 using a multiplexer | 8 | All 8 failed: Y is the inverse of the expected Majority3 output. |
| XOR3 using a multiplexer | 8 | All 8 failed: Y is the inverse of the expected XOR3 output (XNOR3). |

For example, with all inputs at 0, both Majority3 and XOR3 should output 0, but both saved circuits output 1. Their wiring still needs correcting. The tests were added without changing the circuit wiring; the two unnamed output pins were labelled Y.

## Mistakes and corrections

One wiring mistake was an accidental connection between the NOT outputs for I2 and I1 in the priority encoder. These signals need to stay separate. The saved encoder now passes all 256 embedded test rows.

I still made too many careless mistakes. I want to review these circuits again so that I can build and check them more confidently.

## How this learning day went

This learning day took me a lot of time because I got sick. I could not concentrate and work through everything in one go like on the other days. Instead, I had to do small parts each day until I finally finished on Sunday.

I do not find the topic itself particularly complicated, but I definitely still need some review. Especially with the wiring, I need to slow down and check the details instead of making careless mistakes.

## Open follow-up

Correct the inverted outputs in Majority3 and XOR3, then rerun the full circuit checks. The Day 8 Python work on `combine` and `covers` was planned for Saturday; this write-up does not confirm that it has been completed.
