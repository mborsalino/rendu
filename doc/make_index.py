#!/bin/env python3
import os

here = os.path.dirname(os.path.realpath(__file__))

with open(f'{here}/pub_doc/index.html', 'w') as ofh:
    ofh.write('<html>\n')
    ofh.write('  <ul>\n')
    with open(f'{here}/pub_doc/api_versions.txt', 'r') as ifh:
        for version in ifh:
            ofh.write(f'<li><a href=./archive/rendu_{version}/index.html>rendu_{version}</a></li>')
    ofh.write('  </ul>\n')
    ofh.write('</html>\n')
