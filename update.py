#!/usr/bin/python
# Update RPM Requires: fields from allowed_requires.conf
# Copyright (c) 2014 Jolla Ltd.
# Contact: Thomas Perl <thomas.perl@jolla.com>


from __future__ import print_function

import sys

REQUIRES = 'sdk-harbour-rpmvalidator/allowed_requires.conf'

SOURCE_FILENAME = 'sailfish-api.spec.in'
TARGET_FILENAME = 'rpm/sailfish-api.spec'

MARKER = '# -- REQUIRES HERE --'

def read_file(filename):
    return open(filename).read().splitlines()

def want_requirement(requirement):
    if requirement.startswith('#'):
        return False
    elif requirement == '':
        return False
    elif requirement.startswith('qt5-'):
        return True

    return False

qt5_requires = [x for x in read_file(REQUIRES) if want_requirement(x)]

def inject_requires(filename, requirements):
    for line in open(filename).read().splitlines():
        if line == MARKER:
            yield '# Begin requirements inserted by {}'.format(sys.argv[0])
            for requirement in requirements:
                print(' - {}'.format(requirement))
                yield 'Requires: {}'.format(requirement)
            yield '# End requirements inserted by {}'.format(sys.argv[0])
            continue

        yield line

print('Writing: {}'.format(TARGET_FILENAME))
with open(TARGET_FILENAME, 'w') as fp:
    for line in inject_requires(SOURCE_FILENAME, qt5_requires):
        print(line, file=fp)
