"""Generate exhaustive Digital test cases and run the actual saved circuits.

Run: python3 schaltungstests.py
Requires Java and Digital.jar (override its path with DIGITAL_JAR).
Only test blocks and missing output labels are changed, never wiring.
"""
from pathlib import Path
import os
import subprocess
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent


def testdaten(name):
    rows = []
    if name in ('mux4_gatter', '3muxto4_gatter'):
        header = 'S1 S0 D0 D1 D2 D3 Y'
        for number in range(64):
            bits = [int(bit) for bit in format(number, '06b')]
            selection = 2 * bits[0] + bits[1]
            data = bits[2:]
            rows.append(bits + [data[selection]])
    else:
        if name == 'decoder3_gatter':
            header = 'A2 A1 A0 Y0 Y1 Y2 Y3 Y4 Y5 Y6 Y7'
        else:
            header = 'S2 S1 S0 Y'
        for number in range(8):
            bits = [int(bit) for bit in format(number, '03b')]
            if name == 'decoder3_gatter':
                outputs = [int(index == number) for index in range(8)]
            elif name == 'majority3_mux':
                outputs = [int(sum(bits) >= 2)]
            else:
                outputs = [sum(bits) % 2]
            rows.append(bits + outputs)
    lines = [header]
    for row in rows:
        lines.append(' '.join(str(value) for value in row))
    return '\n'.join(lines) + '\n', len(rows)


def install_test(path, data):
    text = path.read_text()
    # Edit individual XML blocks to preserve the rest of the user's file.
    import re
    blocks = list(re.finditer(r'    <visualElement>.*?</visualElement>', text, re.S))
    test_found = False
    for match in reversed(blocks):
        element = ET.fromstring(match.group())
        kind = element.findtext('elementName')
        attrs = element.find('elementAttributes')
        if kind == 'Out' and not attrs.findall('entry'):
            entry = ET.SubElement(attrs, 'entry')
            ET.SubElement(entry, 'string').text = 'Label'
            ET.SubElement(entry, 'string').text = 'Y'
        elif kind == 'Testcase':
            element.find('.//dataString').text = data
            for entry in attrs.findall('entry'):
                if entry.findtext('string') == 'enabled':
                    attrs.remove(entry)
            test_found = True
        else:
            continue
        replacement = '    ' + ET.tostring(element, encoding='unicode').strip()
        text = text[:match.start()] + replacement + text[match.end():]
    if not test_found:
        root = ET.fromstring(text)
        positions = root.findall('./visualElements/visualElement/pos')
        y = max(int(pos.get('y')) for pos in positions) + 120
        block = f'''    <visualElement>
      <elementName>Testcase</elementName>
      <elementAttributes>
        <entry><string>Label</string><string>Full truth table</string></entry>
        <entry><string>Testdata</string><testData><dataString>{data}</dataString></testData></entry>
      </elementAttributes>
      <pos x="100" y="{y}"/>
    </visualElement>
'''
        text = text.replace('  </visualElements>', block + '  </visualElements>')
    ET.fromstring(text)
    path.write_text(text)


def main():
    for name in ('mux4_gatter', '3muxto4_gatter', 'decoder3_gatter', 'majority3_mux', 'XOR3_mux'):
        data, count = testdaten(name)
        install_test(BASE / 'schaltungen' / (name + '.dig'), data)
        print(f'{name}: {count} test rows installed', flush=True)
    jar = os.environ.get('DIGITAL_JAR', str(Path.home() / 'Downloads/Digital/Digital.jar'))
    results = BASE / 'testergebnisse'
    results.mkdir(exist_ok=True)
    failed = False
    for path in sorted((BASE / 'schaltungen').glob('*.dig')):
        result = subprocess.run(['java', '-Djava.awt.headless=true', '-cp', jar,
                                 'CLI', 'test', '-circ', str(path), '-verbose'], capture_output=True, text=True)
        (results / (path.stem + '.txt')).write_text(result.stdout + result.stderr)
        print(path.name + ': ' + result.stdout.strip(), flush=True)
        if result.returncode != 0:
            failed = True
            print(result.stderr)
    if failed:
        raise SystemExit('At least one circuit test failed. See testergebnisse/.')


if __name__ == '__main__':
    main()
