# -*- coding: utf-8 -*-
# Copyright 2020 - 2022 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
**Prefixed Package**

Numbers with support for formatting with SI and IEC prefixes
"""


from math import floor, log10
import re
import sys

__version__ = '0.5.0'

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
    # !: Add space before prefix
    r'(?P<prefix_space>!)?'
    # width: integer
    r'(?P<width>\d+)?'
    # grouping_option: ,_
    r'(?P<grouping>[,_])?'
    # margin:
    r'(?:%(?P<margin>-?\d+))?'
    # .precision: integer
    r'(?:\.(?P<precision>\d+))?'
    # spec_type: Single non-numeric character
    r'(?P<type>\D)?$'
)
RE_PREFIX = re.compile(
    r'(?P<value>[-+]?\d+\.?(?:\d+)?(?:[eE]?\d)?) ?(?P<prefix>(?:[a-zA-Z\u03bc]|\xce\xbc)i?)$'
)

SI_PREFIXES = {
    10**-30: 'q',  # Quecto
    10**-27: 'r',  # Ronto
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
    10**27: 'R',  # Ronna
    10**30: 'Q',  # Quetta
}
SI_SMALLEST = 10 ** -30

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

SI_SMALL = range(-30, 0, 3)
SI_LARGE = range(3, 33, 3)
IEC_RANGE = range(10, 90, 10)

SPEC_FIELDS = ('fill', 'align', 'sign', 'alt', 'zero', 'width', 'grouping')


def raise_from_none(exc):  # pragma: no cover
    """
    Convenience function to raise from None in a Python 2/3 compatible manner
    """
    raise exc


if sys.version_info[0] >= 3:  # pragma: no branch
    exec('def raise_from_none(exc):\n    raise exc from None')  # pylint: disable=exec-used

DEPRECATED = {'j': 'k', 'J': 'm'}


def _convert(value, spec):
    """
    Convert value to value, prefix pair based on format spec
    value, prefix, and spec are returned
    spec may be modified to account for prefix length
    """

    absolute_value = abs(value)

    if spec['type'] in 'hH':
        base, prefixes = 10, SI_PREFIXES
        span = SI_LARGE if absolute_value >= 1.0 else SI_SMALL
    else:
        base, prefixes = 2, IEC_PREFIXES
        span = IEC_RANGE if absolute_value >= 1.0 else tuple()

    margin = 1.0 if spec['margin'] is None else (100.0 + float(spec['margin'])) / 100.0

    if span is SI_SMALL and 0 < absolute_value < SI_SMALLEST * margin:
        magnitude = SI_SMALLEST
    else:
        magnitude = 0
        for exp in span:
            next_mag = base**exp
            # Use floor division rather than comparison for float variance
            if absolute_value // (next_mag * margin):
                magnitude = next_mag
            else:
                break

    if magnitude:
        value /= magnitude
        prefix = '%s%s%s' % ('' if spec['prefix_space'] is None else ' ',
                             prefixes[magnitude],
                             'i' if spec['type'] in 'kK' else '')

        if spec['width'] is not None:
            width = int(spec['width'])
            if width:
                spec['width'] = str(width - len(prefix))

    else:
        prefix = ''

    return value, prefix, spec


# pylint: disable=super-with-arguments
class Float(float):
    """
    Subclass of the built-in :py:class:`float` class

    Key differences:

    - When a math operation is performed with another real number type
      (:py:class:`float`, :py:class:`int`), the result will be a
      :py:class:`prefixed.Float` instance.

    - Additional presentation types ``'h'``, ``'H'``, ``'k'``, ``'K'``,
      ``'m'``, and ``'M'`` are supported for f-strings and :py:func:`format`.

      +---------+-------------------------------------------------------------------+
      | Type    | Meaning                                                           |
      +=========+===================================================================+
      | ``'h'`` | SI format. Outputs the number with closest divisible SI prefix.   |
      |         | (k, M, G, ...)                                                    |
      +---------+-------------------------------------------------------------------+
      | ``'H'`` | Same as ``'h'`` with precision indicating significant digits.     |
      +---------+-------------------------------------------------------------------+
      | ``'k'`` | IEC Format. Outputs the number with closest divisible IEC prefix. |
      |         | (Ki, Mi, Gi, ...)                                                 |
      +---------+-------------------------------------------------------------------+
      | ``'K'`` | Same as ``'k'`` with precision indicating significant digits.     |
      +---------+-------------------------------------------------------------------+
      | ``'m'`` | Short IEC Format. Same as ``'k'`` but only a single character.    |
      |         | (K, M, G, ...)                                                    |
      +---------+-------------------------------------------------------------------+
      | ``'M'`` | Same as ``'m'`` with precision indicating significant digits.     |
      +---------+-------------------------------------------------------------------+
      |         |                                                                   |
      +---------+-------------------------------------------------------------------+
      | ``'j'`` | Alias for ``'k'`` - DEPRECATED                                    |
      +---------+-------------------------------------------------------------------+
      | ``'J'`` | Alias for ``'m'`` - DEPRECATED                                    |
      +---------+-------------------------------------------------------------------+

    - When initializing from strings, SI and IEC prefixes are honored

      .. code-block:: python

        >>> Float('2k')
        Float(2000.0)

        >>> Float('2Ki')
        Float(2048.0)

    - An additional format flag '!' is available which adds a space before the prefix

      .. code-block:: python

        >>> f'{Float(3250):!.2h}'
        '3.25 k'

    - When the ``'H'``, ``'K``, or ``'M'`` presentation types are used, precision is treated as
      the number of significant digits to include. Standard rounding will occur for the final digit.

      .. code-block:: python

        >>> f'{Float(1246):.3h}'
        '1.246k'

        >>> f'{Float(1246):.3H}'
        '1.25k'

      By default, trailing zeros are removed.

      .. code-block:: python

        >>> f'{Float(1000):.3H}'
        '1k'

      To preserve trailing zeros, include the ``'#'`` flag.

      .. code-block:: python

        >>> f'{Float(1000):#.3H}'
        '1.00k'

    - An additional field, margin, can be specified which lowers or raises the threshold for
      for each prefix by the given percentage.
      Margin is specified before precision with the syntax  ``%[-]digit+``.

      .. code-block:: python

        >>> f'{Float(950):.2h}'
        '950.00'

        >>> f'{Float(950):%-5.2h}'
        '0.95k'

        >>> f'{Float(1000):%5.2h}'
        '1000.00'

        >>> f'{Float(1050):%5.2h}'
        '1.05k'

"""

    def __new__(cls, value=0.0):

        convert_value = value
        if isinstance(value, BASESTRING):
            match = RE_PREFIX.match(value)
            if match:
                prefix = match.group('prefix')
                if prefix[-1] == 'i':
                    magnitude = IEC_MAGNITUDE.get(prefix[0])
                else:
                    magnitude = SI_MAGNITUDE.get(prefix)

                if magnitude:
                    convert_value = float(match.group('value')) * magnitude

        try:
            new = super(Float, cls).__new__(cls, convert_value)
        except ValueError:
            raise_from_none(
                ValueError('Could not convert %s to Float: %r' % (value.__class__.__name__, value))
            )
        except TypeError:
            raise_from_none(
                TypeError("Can't convert %s to Float: %r" % (value.__class__.__name__, value))
            )

        return new

    def __repr__(self):

        return 'Float(%s)' % super(Float, self).__repr__()

    def __str__(self):
        return str(float(self))

    def __format__(self, format_spec):

        # Parse format spec
        match = RE_FORMAT_SPEC.match(format_spec)
        if match is None:
            raise ValueError('Invalid format specifier')

        spec = match.groupdict()

        # Handle deprecated spec types
        if spec['type'] in DEPRECATED:
            spec['type'] = DEPRECATED[spec['type']]

        # If not a spec we handle, use float.__format__(()
        if spec['type'] not in {'h', 'H', 'k', 'K', 'm', 'M'}:
            return super(Float, self).__format__(format_spec)

        # Determine value and prefix
        value, prefix, spec = _convert(float(self), spec)

        precision = int(spec['precision']) if spec['precision'] else None

        # Adjust precision for significant digits
        if spec['type'] in 'HKM':
            precision = precision or 6

            # Try to avoid floating point variance by limiting trailing decimals
            if value >= 1:
                value = round(value, precision + 1)

            # In Python 2.7, floor sometimes returns a float, so coerce with int
            int_digits = 1 if value == 0.0 else int(floor(log10(abs(value)))) + 1

            value = round(value, precision - int_digits)
            precision = max(0, precision - int_digits)

            if precision and not spec['alt']:
                preformat = value.__format__('.%df' % precision)
                precision -= (len(preformat) - len(preformat.rstrip('0')))

            # Remove trailing decimal when no decimal places are occupied
            elif spec['alt']:
                spec['alt'] = None

        # Compose new format spec
        new_spec = ''.join(spec[key] for key in SPEC_FIELDS if spec[key] is not None)
        if precision is None:
            new_spec += 'f'
        else:
            new_spec = '%s.%if' % (new_spec, precision)

        # Format with new format spec
        return '%s%s' % (value.__format__(new_spec), prefix)

    def __abs__(self):
        return self.__class__(super(Float, self).__abs__())

    def __add__(self, value):
        try:
            return self.__class__(super(Float, self).__add__(value))
        except TypeError:
            return NotImplemented

    def __div__(self, value):  # pragma: no cover
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

    def __rdiv__(self, value):  # pragma: no cover
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
