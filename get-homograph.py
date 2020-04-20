#!/usr/bin/env python3
'''
===========================================================================
 get-homograph.py v0.01-20200420 Copyright 2020 by cbuijs@chrisbuijs.com
===========================================================================

 Show domain homograph

===========================================================================
'''

# Standard Stuff
import sys, socket

# Homoglyphs
import homoglyphs as hg

######################################################################

if __name__ == '__main__':

    homoglyphs = hg.Homoglyphs(languages={'en', 'bg', 'ru', 'el'})

    for line in sys.stdin:
        entry = line.strip().strip('.').lower()
        if entry.count('.') > 0:
            ext = entry.split('.')[-1]
            if ext in ('ac', 'ar', 'asia', 'at', 'biz', 'br', 'cat', 'ch', 'cl', 'cn', 'com', 'de', 'dk', 'es', 'fi', 'gr', 'hu', 'il', 'info', 'io', 'ir', 'is', 'jp', 'kr', 'li', 'lt', 'lu', 'lv', 'museum', 'name', 'net', 'no', 'nu', 'nz', 'org', 'pl', 'pr', 'se', 'sh', 'tel', 'th', 'tm', 'tw', 'ua', 'vn'):
                entry = '.'.join(entry.split('.')[:-1])
                for combo in homoglyphs.get_combinations(entry):
                    sys.stdout.write('{0}.{1}\t{2}.{1}\n'.format(combo.encode('idna').decode('ascii'), ext, entry))

sys.exit(0)

