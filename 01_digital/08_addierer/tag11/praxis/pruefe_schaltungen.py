"""Prueft DEINE Digital-Datei, ohne sie zu veraendern.

python3 pruefe_schaltungen.py schaltungen/volladdierer.dig
python3 pruefe_schaltungen.py schaltungen/ripple4.dig
Voraussetzung: Java und Digital.jar; bei Bedarf --jar PFAD.
Der externe Test ersetzt nicht die Timing-Analyse.
"""
import argparse
import os
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET


def testdaten(bits):
    if bits == 1:
        header = 'A B C_in S C_out'
    else:
        header = 'A3 A2 A1 A0 B3 B2 B1 B0 C_in S3 S2 S1 S0 C_out'
    lines = [header]
    for a in range(2 ** bits):
        for b in range(2 ** bits):
            for cin in range(2):
                total = a + b + cin
                s = total % (2 ** bits)
                cout = total // (2 ** bits)
                inputs = list(format(a, f'0{bits}b') + format(b, f'0{bits}b'))
                outputs = list(format(s, f'0{bits}b'))
                lines.append(' '.join(inputs + [str(cin)] + outputs + [str(cout)]))
    return '\n'.join(lines) + '\n', len(lines) - 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('circuit', type=Path)
    parser.add_argument('--jar', type=Path, default=Path(os.environ.get(
        'DIGITAL_JAR', str(Path.home() / 'Downloads/Digital/Digital.jar'))))
    args = parser.parse_args()
    bits_by_name = {'volladdierer': 1, 'ripple4': 4}
    if args.circuit.stem not in bits_by_name:
        raise SystemExit('Dateiname muss volladdierer.dig oder ripple4.dig sein.')
    if not args.circuit.is_file():
        raise SystemExit('Noch keine Schaltung vorhanden: Baue und speichere sie zuerst.')
    if not args.jar.is_file():
        raise SystemExit('Digital.jar nicht gefunden. Nutze --jar PFAD.')
    data, count = testdaten(bits_by_name[args.circuit.stem])
    folder = Path(__file__).resolve().parent / 'results'
    folder.mkdir(exist_ok=True)
    # -tests erwartet eine Digital-Datei mit Testcase-Baustein.
    root = ET.Element('circuit')
    ET.SubElement(root, 'version').text = '1'
    ET.SubElement(root, 'attributes')
    visual = ET.SubElement(ET.SubElement(root, 'visualElements'), 'visualElement')
    ET.SubElement(visual, 'elementName').text = 'Testcase'
    attrs = ET.SubElement(visual, 'elementAttributes')
    label = ET.SubElement(attrs, 'entry')
    ET.SubElement(label, 'string').text = 'Label'
    ET.SubElement(label, 'string').text = f'Alle {count} Kombinationen'
    entry = ET.SubElement(attrs, 'entry')
    ET.SubElement(entry, 'string').text = 'Testdata'
    ET.SubElement(ET.SubElement(entry, 'testData'), 'dataString').text = data
    ET.SubElement(visual, 'pos', x='100', y='100')
    ET.SubElement(root, 'wires')
    testfile = folder / (args.circuit.stem + '_tests.dig')
    ET.ElementTree(root).write(testfile, encoding='utf-8', xml_declaration=True)
    cmd = ['java', '-Djava.awt.headless=true', '-cp', str(args.jar.resolve()),
           'CLI', 'test', '-circ', str(args.circuit.resolve()),
           '-tests', str(testfile), '-verbose']
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except FileNotFoundError:
        raise SystemExit('Java nicht gefunden.')
    except subprocess.TimeoutExpired:
        raise SystemExit('Test nach 60 Sekunden abgebrochen. Schaltung auf Rueckkopplungen pruefen.')
    logfile = folder / (args.circuit.stem + '_test.txt')
    logfile.write_text(result.stdout + result.stderr)
    print(result.stdout)
    print(f'{count} Eingabekombinationen; Protokoll: {logfile}')
    if result.returncode != 0:
        print(result.stderr)
        raise SystemExit('Pruefung fehlgeschlagen. Details stehen im Protokoll.')


if __name__ == '__main__':
    main()
