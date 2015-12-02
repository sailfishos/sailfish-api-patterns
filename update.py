#!/usr/bin/python
# Create YAML pattern files from allowed_requires.conf
# Copyright (c) 2014 Jolla Ltd.
# Contact: Thomas Perl <thomas.perl@jolla.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from __future__ import print_function

import sys

REQUIRES = 'sdk-harbour-rpmvalidator/allowed_requires.conf'

fixed_requires = ["libsailfishapp", "SDL2", "SDL2_gfx", "SDL2_image",
                  "SDL2_mixer", "SDL2_net", "SDL2_ttf"]

# Bump this whenever the API gets new items
API_LEVEL = 3

SOURCE_FILENAME = 'template.yaml.in'
TARGET_FILENAME = 'patterns/sailfish-api-{}.yaml'.format(API_LEVEL)

MARKER = '# -- INSERT PACKAGES HERE --'

def read_file(filename):
    return open(filename).read().splitlines()

def want_requirement(requirement):
    if requirement.startswith('#'):
        # Ignore comments
        return False
    elif requirement == '':
        # Ignore empty lines
        return False
    elif requirement.startswith('qt5-'):
        # Right now, we are only interested in pre-installing all Qt 5 plugins
        # and imports, so that they are available from boosted processes.
        return True

    # If in doubt, don't add the requirement to the pattern
    return False

requires = [x for x in read_file(REQUIRES) if want_requirement(x)]
requires.extend(fixed_requires)

def inject_requires(filename, requirements):
    for line in open(filename).read().splitlines():
        if line == MARKER:
            yield '# Begin requirements inserted by {}'.format(sys.argv[0])
            for requirement in requirements:
                print(' - {}'.format(requirement))
                yield '    - {}'.format(requirement)
            yield '# End requirements inserted by {}'.format(sys.argv[0])
            continue

        yield line.replace('%LEVEL%', str(API_LEVEL))

print('Writing: {}'.format(TARGET_FILENAME))
with open(TARGET_FILENAME, 'w') as fp:
    for line in inject_requires(SOURCE_FILENAME, requires):
        print(line, file=fp)
