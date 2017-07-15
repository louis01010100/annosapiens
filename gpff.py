#!/usr/bin/env python

import sys
import re

pattern = re.compile('^LOCUS\s')

try :
    for line in sys.stdin:
        line.strip('\n')
        if pattern.match(line):
            columns = line.split()
            print('{acc}\t{length}'.format(acc=columns[1], length=columns[2]))
except KeyboardInterrupt:
    sys.exit(1)
