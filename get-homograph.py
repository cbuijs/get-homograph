#!/usr/bin/env python3
'''
===========================================================================
 get-homograph.py v0.01-20200420 Copyright 2020 by cbuijs@chrisbuijs.com
===========================================================================

 Show domain punycoded homographs

 Uses "homoglyphs":
 https://github.com/life4/homoglyphs

===========================================================================
'''

# Standard Stuff
import sys, socket

# Homoglyphs
# pip3 install homoglyphs
import homoglyphs as hg

######################################################################

if __name__ == '__main__':

    # Init homoglyphs with English, Bulgarian, Russian and Greek
    homoglyphs = hg.Homoglyphs(languages={'en', 'bg', 'ru', 'el'})

    # Grep input from stdin
    for line in sys.stdin:

        # Strip leading/ending dots/spaces
        entry = line.strip().strip('.').lower()

        # Get TLD
        if entry.count('.') > 0:
            tld = entry.split('.')[-1]

            # Only generate for IDN enabled TLDs
            if tld in ('ac', 'ar', 'asia', 'at', 'biz', 'br', 'cat', 'ch', 'cl', 'cn', 'com', 'de', 'dk', 'es', 'fi', 'gr', 'hu', 'il', 'info', 'io', 'ir', 'is', 'jp', 'kr', 'li', 'lt', 'lu', 'lv', 'museum', 'name', 'net', 'no', 'nu', 'nz', 'org', 'pl', 'pr', 'se', 'sh', 'tel', 'th', 'tm', 'tw', 'ua', 'vn'):

                # Strip TLD
                entry = '.'.join(entry.split('.')[:-1])

                # Output all possible punycoded homograph domains
                for combo in homoglyphs.get_combinations(entry):
                    sys.stdout.write('{0}.{1}\t{2}.{1}\n'.format(combo.encode('idna').decode('ascii'), tld, entry))

# Done!
sys.exit(0)

