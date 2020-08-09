# -*- coding: utf-8 -*-
# Copyright 2020 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
**Prefixed Package**

Numbers with support for formatting with SI and IEC prefixes
"""


import re

__version__ = '0.0.2'

try:
    BASESTRING = basestring
except NameError:
    BASESTRING = str

RE_FORMAT_SPEC = re.compile(
    # fill: requires align - capture if second char is align char
    r'(?P<fill>.(?=[\<\>\=\^]))?'
    # align: <>=^
    r'(?P<align>[\<\>\=\^])?'
    # sign +-(space)
    r'(?P<sign>[\+\- ])?'
    # # Alternative form (Only numeric classes)
    r'(?P<alt>\#)?'
    # 0: same as 0=, Ignored if fill/align is given
    r'(?P<zero>0)?'
    # width: integer
    r'(?P<width>\d+)?'
    # grouping_option: ,_
    r'(?P<grouping>[,_])?'
    # .precision: integer
    r'(?:\.(?P<precision>\d+))?'
    # spec_type: Single non-numeric character
    r'(?P<type>\D)?$'
)
RE_PREFIX = re.compile(r'(?P<value>\d+\.?(?:\d+)?[eE]?(?:\d)?)(?P<prefix>[a-zA-Zμ]i?)\D*$')

SI_PREFIXES = {
    10**-24: 'y',  # Yocto
    10**-21: 'z',  # Zepto
    10**-18: 'a',  # Atto
    10**-15: 'f',  # Femto
    10**-12: 'p',  # Pico
    10**-9: 'n',  # Nano
    10**-6: 'μ',  # Micro
    10**-3: 'm',  # Milli
    10**3: 'k',  # Kilo
    10**6: 'M',  # Mega
    10**9: 'G',  # Giga
    10**12: 'T',  # Tera
    10**15: 'P',  # Peta
    10**18: 'E',  # Exa
    10**21: 'Z',  # Zetta
    10**24: 'Y',  # Yotta
}

SI_MAGNITUDE = {val: key for key, val in SI_PREFIXES.items()}

IEC_PREFIXES = {
    2**10: 'K',  # Kibi
    2**20: 'M',  # Mebi
    2**30: 'G',  # Gibi
    2**40: 'T',  # Tebi
    2**50: 'P',  # Pedi
    2**60: 'E',  # Exbi
    2**70: 'Z',  # Zebi
    2**80: 'Y',  # Yobi
}

IEC_MAGNITUDE = {val: key for key, val in IEC_PREFIXES.items()}

SI_NEG = range(-27, -3, 3)
SI_POS = range(3, 27, 3)
IEC_POS = range(10, 90, 10)

SPEC_FIELDS = ('fill', 'align', 'sign', 'alt', 'zero', 'width', 'grouping')


class Float(float):
    """
    Subclass of the built-in float class

    Key differences:
        - Format type 'h' will output with an SI prefix (ex: k for 1000)
        - Format type 'j' will output with an IEC prefix (ex: Ki for 1024)
        - Format type 'J' will output with an IEC prefix minus the i (ex: K for 1024)
        - When initializing from strings, SI and IEC prefixes are honored
            - SI Example: Float('3k')
            - IEC Example: Float('3Ki')
    """

    def __new__(cls, value=0.0):

        if isinstance(value, BASESTRING):
            match = RE_PREFIX.match(value)
            if match:
                prefix = match.group('prefix')
                if prefix[-1] == 'i':
                    magnitude = IEC_MAGNITUDE.get(prefix[0])
                else:
                    magnitude = SI_MAGNITUDE.get(prefix)
                if magnitude:
                    return super(Float, cls).__new__(cls, float(match.group('value')) * magnitude)

        return super(Float, cls).__new__(cls, value)

    def __repr__(self):

        return 'Float(%s)' % super(Float, self).__repr__()

    def __format__(self, format_spec):

        match = RE_FORMAT_SPEC.match(format_spec)
        if match is None:
            raise ValueError('Invalid format specifier')

        spec = match.groupdict()
        spec_type = spec['type']

        if spec_type is None or spec_type not in 'hjJ':
            return super(Float, self).__format__(format_spec)

        magnitude = 0
        if spec_type == 'h':
            base, prefixes = 10, SI_PREFIXES
            span = SI_POS if self > 0 else SI_NEG
        else:
            base, prefixes = 2, IEC_PREFIXES
            span = IEC_POS if self > 0 else tuple()

        for exp in span:
            next_mag = base**exp
            if self > next_mag:
                magnitude = next_mag
            else:
                break

        if magnitude:
            value = float(self) / magnitude
            prefix = prefixes[magnitude]

            if spec_type == 'J':
                prefix += 'i'

            if spec['width'] is not None:
                width = int(spec['width'])
                if width:
                    spec['width'] = str(width - len(prefix))

        else:
            value = float(self)
            prefix = ''

        new_spec = ''.join(spec[key] for key in SPEC_FIELDS if spec[key] is not None)
        if spec['precision'] is None:
            new_spec += 'f'
        else:
            new_spec = '%s.%sf' % (new_spec, spec['precision'])

        return '%s%s' % (value.__format__(new_spec), prefix)

    def __abs__(self):
        return self.__class__(super(Float, self).__abs__())

    def __add__(self, value):
        try:
            return self.__class__(super(Float, self).__add__(value))
        except TypeError:
            return NotImplemented

    def __div__(self, value):
        """
        Old style division. Implemented to support Python 2.7
        """
        try:
            return self.__class__(super(Float, self).__div__(value))  # pylint: disable=no-member
        except TypeError:
            return NotImplemented

    def __divmod__(self, value):
        try:
            return tuple(self.__class__(val) for val in super(Float, self).__divmod__(value))
        except TypeError:
            return NotImplemented

    def __floordiv__(self, value):
        try:
            return self.__class__(super(Float, self).__floordiv__(value))
        except TypeError:
            return NotImplemented

    def __mod__(self, value):
        try:
            return self.__class__(super(Float, self).__mod__(value))
        except TypeError:
            return NotImplemented

    def __mul__(self, value):
        try:
            return self.__class__(super(Float, self).__mul__(value))
        except TypeError:
            return NotImplemented

    def __neg__(self):
        return self.__class__(super(Float, self).__neg__())

    def __pos__(self):
        return self.__class__(super(Float, self).__pos__())

    def __pow__(self, value):
        try:
            return self.__class__(super(Float, self).__pow__(value))
        except TypeError:
            return NotImplemented

    def __radd__(self, value):
        try:
            return self.__class__(super(Float, self).__radd__(value))
        except TypeError:
            return NotImplemented

    def __rdiv__(self, value):
        """
        Old style division. Implemented to support Python 2.7
        """
        try:
            return self.__class__(super(Float, self).__rdiv__(value))  # pylint: disable=no-member
        except TypeError:
            return NotImplemented

    def __rdivmod__(self, value):
        try:
            return tuple(self.__class__(val) for val in super(Float, self).__rdivmod__(value))
        except TypeError:
            return NotImplemented

    def __rfloordiv__(self, value):
        try:
            return self.__class__(super(Float, self).__rfloordiv__(value))
        except TypeError:
            return NotImplemented

    def __rmod__(self, value):
        try:
            return self.__class__(super(Float, self).__rmod__(value))
        except TypeError:
            return NotImplemented

    def __rmul__(self, value):
        try:
            return self.__class__(super(Float, self).__rmul__(value))
        except TypeError:
            return NotImplemented

    def __rpow__(self, value):
        try:
            return self.__class__(super(Float, self).__rpow__(value))
        except TypeError:
            return NotImplemented

    def __rsub__(self, value):
        try:
            return self.__class__(super(Float, self).__rsub__(value))
        except TypeError:
            return NotImplemented

    def __rtruediv__(self, value):
        try:
            return self.__class__(super(Float, self).__rtruediv__(value))
        except TypeError:
            return NotImplemented

    def __sub__(self, value):
        try:
            return self.__class__(super(Float, self).__sub__(value))
        except TypeError:
            return NotImplemented

    def __truediv__(self, value):
        try:
            return self.__class__(super(Float, self).__truediv__(value))
        except TypeError:
            return NotImplemented
