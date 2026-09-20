# Tag 6: CMOS-NAND
## Aufbau
Die vorliegende Schaltung ist ein CMOS-NAND-Gatter bestehen aus einer Versorgungsquelle Vdd mit 3,3V. Darunter liegt eine Parallelschaltung bestehen aus einem pMOS (a) und einem pMOS (b).Das Leitbild hierfür ist !A + !B. Diese sind mit dem Ausgang (y) verbunden. Unter der Parallelschaltung folgt die Reihenschaltung bestehend aus nMos (a) und nMos (b), zwischen dieser Reihenschaltung liegt x als Zwischenknoten. nMOS (b) ist dabei mit Masse (0) verbunden

## Durchfuehrung
Die Durchführung wird in der Datei "Aufgabe_6_Detail.cir" dokumentiert.  Es wurde ein Periodendauer von 40u für den gesamten Zyklus einer Messung gewählt. Als Startdelay wurde 20u gewählt und die Flanken wurden mit 0.01u beziffert. Daraus folgt eine Einschaltdauer von 19.99u. Die 20u Startdelay wurden deshalb ausgewählt um zu sehen, wie sich der Ausgang im Ruhezustand verhält. Bei B wurde 10u Startdelay mit 20u Periodendauer eingestellt. Es wurden 3 seperate Wertetabellen dadurch angelegt v(a), v(b) und v(y)
## Ergebnis
In dem Ausgegeben Zeitverlauf sehen wir, dass Y bis zu ca. 30u konstant 3,3V beträgt. A beträgt bis ca. 20u genau 0V und mit der 0.01 Flanke steigt es zu 20.01 auf 3,3V. Bei B ist der erste Anstieg auf 3.3 zu 10.01u bis 20.01u jeweils mit 0.01u Flanke. Der nand2_zeitverlauf.png zeigt alle 3 Verläufe.

Die simulierten Ausgangsspannungen an den vier Prüfzeitpunkten ergeben folgende NAND-Wahrheitstabelle. A und B sind als Logikwerte angegeben; die Spannungswerte sind gerundet.

| Zeitpunkt | A | B | Ausgangsspannung V(Y) | Logikwert Y |
| --- | --- | --- | --- | --- |
| 5 µs | 0 | 0 | ≈ 3,3 V | HIGH (1) |
| 15 µs | 0 | 1 | ≈ 3,3 V | HIGH (1) |
| 25 µs | 1 | 0 | ≈ 3,3 V | HIGH (1) |
| 35 µs | 1 | 1 | ≈ 5,09 × 10⁻⁸ V (praktisch 0 V) | LOW (0) |

Messung mit Wnmos = 1um: tfall ca. 2.25u
Messung mit Wnmos = 2um: tfall ca. 1.17u
## Erklaerung
Bei 5u sehen wir das A und B = 0 sind, was zur Folge hat das Y = 1 --> High ist, da !A + !B das tragende Leitbild ist. Wiederum sehen wir bei 35u, dass A und B = 1 sind, weshalb die beiden pMOS mit dem Leitbild !A + !B 0 sind und nur die beinem nMOS leitend sind weshalb auch die Spannung nach Masse abfällt und somit ist Y = Low
Die Wahrheitstabelle beschreibt die stabilen Logikwerte. Der Transistoraufbau erklärt die leitenden Strompfade. Zusammen mit der Lastkapazität erklärt er außerdem, warum sich die Ausgangsspannung nicht augenblicklich ändert und beim Umschalten Energie umgesetzt wird.

Die beiden nMOS liegen in Reihe. Im vereinfachten Widerstandsmodell addieren sich ihre Einschaltwiderstände. Durch die Verdopplung beider Kanalbreiten sinkt der Widerstand des Entladepfads näherungsweise. Dadurch entlädt sich der Lastkondensator schneller. Die simulierte Fallzeit sinkt von etwa 226 ns auf 118 ns und damit annähernd auf die Hälfte.

## Grenzen und offene Fragen
Ich bin mit der ngspice Syntax noch sehr unsicher, zudem muss ich mir das Python plotting angucken. Auswerten der Grafiken und Zahlen verstehe ich schon, nur fällt es mir manchmal sehr schwer es so zu formulieren, dass es wirklich das meint, was ich denke. Dort bin ich auch noch zu ungenau.
