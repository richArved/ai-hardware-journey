"""Python-Referenzpruefer fuer die Digital-Demo, kein neues Pflichtprogramm.

python3 pruefe_demo.py
Der Haupttest vergleicht die drei wirklichen Digital-Ausgaenge mit A+B+Cin.
Digital wird headless gestartet; deine Schaltungen werden nicht veraendert.
"""
from itertools import product
from pathlib import Path
import os
import subprocess
import xml.etree.ElementTree as ET

FOLDER = Path(__file__).resolve().parent


def jar_path():
    candidates = [
        os.environ.get('DIGITAL_JAR'),
        Path.home() / 'Desktop/Digital/Digital/target/Digital.jar',
        Path.home() / 'Desktop/Digital/Digital.app/Contents/Java/Digital.jar',
        Path.home() / 'Downloads/Digital/Digital.jar',
    ]
    for path in candidates:
        if path and Path(path).is_file():
            return Path(path)
    raise SystemExit('Digital.jar fehlt. Setze DIGITAL_JAR auf den Pfad deiner Datei.')


def run_test(name, header, rows):
    folder = FOLDER / 'results'
    folder.mkdir(exist_ok=True)
    data = [header]
    data.extend(' '.join(str(value) for value in row) for row in rows)
    count = len(data) - 1
    root = ET.Element('circuit')
    ET.SubElement(root, 'version').text = '2'
    ET.SubElement(root, 'attributes')
    element = ET.SubElement(ET.SubElement(root, 'visualElements'), 'visualElement')
    ET.SubElement(element, 'elementName').text = 'Testcase'
    attrs = ET.SubElement(element, 'elementAttributes')
    label = ET.SubElement(attrs, 'entry')
    ET.SubElement(label, 'string').text = 'Label'
    ET.SubElement(label, 'string').text = f'{name}: alle {count} Kombinationen'
    entry = ET.SubElement(attrs, 'entry')
    ET.SubElement(entry, 'string').text = 'Testdata'
    ET.SubElement(ET.SubElement(entry, 'testData'), 'dataString').text = '\n'.join(data) + '\n'
    ET.SubElement(element, 'pos', x='0', y='0')
    ET.SubElement(root, 'wires')
    testfile = folder / f'{name}_tests.dig'
    ET.ElementTree(root).write(testfile, encoding='utf-8', xml_declaration=True)
    command = ['java', '-Djava.awt.headless=true', '-cp', str(jar_path()),
               'CLI', 'test', '-circ', str(FOLDER / f'{name}.dig'),
               '-tests', str(testfile), '-verbose']
    result = subprocess.run(command, capture_output=True, text=True, timeout=120)
    (folder / f'{name}_test.txt').write_text(result.stdout + result.stderr)
    print(result.stdout.strip())
    if result.returncode:
        raise SystemExit('Digital-Test fehlgeschlagen; Details stehen in results/.')
    return count


def main_rows():
    for a in range(256):
        for b in range(256):
            for cin in (0, 1):
                # Unabhaengiger Vergleich mit der normalen Addition.
                expected = int(a + b + cin >= 256)
                input_bits = [int(bit) for bit in f'{a:08b}{b:08b}']
                yield input_bits + [cin, expected, expected, expected]


def block_rows():
    for row in product((0, 1), repeat=9):
        # Header: G3 P3 G2 P2 G1 P1 G0 P0 Cin.
        carry = row[8]
        for i in (6, 4, 2, 0):
            g = row[i]
            p = row[i + 1]
            carry = g | (p & carry)
        yield list(row) + [carry]


if __name__ == '__main__':
    count = 0
    count += run_test('bit_gp', 'A B G P',
                      ([a, b, a & b, a | b] for a, b in product((0, 1), repeat=2)))
    count += run_test('carry_stufe', 'G P Cin Cout',
                      ([g, p, cin, g | (p & cin)] for g, p, cin in product((0, 1), repeat=3)))
    count += run_test('gruppe_verbinden', 'GH PH GL PL G P',
                      ([gh, ph, gl, pl, gh | (ph & gl), ph & pl]
                       for gh, ph, gl, pl in product((0, 1), repeat=4)))
    count += run_test('block4_carry', 'G3 P3 G2 P2 G1 P1 G0 P0 Cin Cout', block_rows())
    count += run_test('Lookahead_Vergleich_8bit',
                      'A7 A6 A5 A4 A3 A2 A1 A0 B7 B6 B5 B4 B3 B2 B1 B0 Cin C8_Ripple C8_Block C8_Gruppe',
                      main_rows())
    print(f'Insgesamt {count} Testfaelle bestanden.')
