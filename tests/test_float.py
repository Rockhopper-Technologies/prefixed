# -*- coding: utf-8 -*-
# Copyright 2020 - 2022 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Test file for prefixed.Float
"""

import sys

from prefixed import Float

if sys.version_info[0] < 3:
    import unittest2 as unittest
else:
    import unittest


class TestFloat(unittest.TestCase):
    """
    General tests for prefixed.Float
    """

    def test_repr(self):
        """
        Test repr output
        """

        self.assertEqual(repr(Float(1.0)), 'Float(1.0)')

    def test_str(self):
        """
        Test repr output
        """

        self.assertEqual(str(Float(1.0)), '1.0')


# pylint: disable=expression-not-assigned
class TestFloatFormatting(unittest.TestCase):
    """
    Tests for prefixed.Float input and output
    """

    def test_output_zero(self):
        """
        Output when value is zero
        """

        zero = Float(0)
        self.assertEqual(format(zero, '.2h'), '0.00')
        self.assertEqual(format(zero, '.2H'), '0')
        self.assertEqual(format(zero, '#.3H'), '0.00')
        self.assertEqual(format(zero, '.2k'), '0.00')
        self.assertEqual(format(zero, '.2m'), '0.00')
        self.assertEqual(format(zero, '.2K'), '0')
        self.assertEqual(format(zero, '.2M'), '0')
        self.assertEqual(format(zero, '#.3K'), '0.00')
        self.assertEqual(format(zero, '#.3M'), '0.00')

    def test_output_si_large_pos(self):
        """
        Output for large (>=1) positive numbers in SI format
        """

        tests = (
            # (float, .2h, .2H, #.3H)
            (1, '1.00', '1', '1.00'),
            (11, '11.00', '11', '11.0'),
            (101, '101.00', '100', '101'),
            (1010, '1.01k', '1k', '1.01k'),
            (10010, '10.01k', '10k', '10.0k'),
            (100010, '100.01k', '100k', '100k'),
            (1.01e6, '1.01M', '1M', '1.01M'),
            (1.001e7, '10.01M', '10M', '10.0M'),
            (1.0001e8, '100.01M', '100M', '100M'),
            (1.01e9, '1.01G', '1G', '1.01G'),
            (1.001e10, '10.01G', '10G', '10.0G'),
            (1.0001e11, '100.01G', '100G', '100G'),
            (1.01e12, '1.01T', '1T', '1.01T'),
            (1.001e13, '10.01T', '10T', '10.0T'),
            (1.0001e14, '100.01T', '100T', '100T'),
            (1.01e15, '1.01P', '1P', '1.01P'),
            (1.001e16, '10.01P', '10P', '10.0P'),
            (1.0001e17, '100.01P', '100P', '100P'),
            (1.01e18, '1.01E', '1E', '1.01E'),
            (1.001e19, '10.01E', '10E', '10.0E'),
            (1.0001e20, '100.01E', '100E', '100E'),
            (1.01e21, '1.01Z', '1Z', '1.01Z'),
            (1.001e22, '10.01Z', '10Z', '10.0Z'),
            (1.0001e23, '100.01Z', '100Z', '100Z'),
            (1.01e24, '1.01Y', '1Y', '1.01Y'),
            (1.001e25, '10.01Y', '10Y', '10.0Y'),
            (1.0001e26, '100.01Y', '100Y', '100Y'),
            (1.01e27, '1.01R', '1R', '1.01R'),
            (1.001e28, '10.01R', '10R', '10.0R'),
            (1.0001e29, '100.01R', '100R', '100R'),
            (1.01e30, '1.01Q', '1Q', '1.01Q'),
            (1.001e31, '10.01Q', '10Q', '10.0Q'),
            (1.0001e32, '100.01Q', '100Q', '100Q'),

            # Larger than largest magnitude
            (1.01e33, '1010.00Q', '1000Q', '1010Q'),
            (1.001e34, '10010.00Q', '10000Q', '10000Q'),
            (1.0001e35, '100010.00Q', '100000Q', '100000Q'),

            (10, '10.00', '10', '10.0'),
            (1e2, '100.00', '100', '100'),
            (1e3, '1.00k', '1k', '1.00k'),
            (1e4, '10.00k', '10k', '10.0k'),
            (1e5, '100.00k', '100k', '100k'),
            (1e6, '1.00M', '1M', '1.00M'),
            (1e7, '10.00M', '10M', '10.0M'),
            (1e8, '100.00M', '100M', '100M'),
            (1e9, '1.00G', '1G', '1.00G'),
            (1e10, '10.00G', '10G', '10.0G'),
            (1e11, '100.00G', '100G', '100G'),
            (1e12, '1.00T', '1T', '1.00T'),
            (1e13, '10.00T', '10T', '10.0T'),
            (1e14, '100.00T', '100T', '100T'),
            (1e15, '1.00P', '1P', '1.00P'),
            (1e16, '10.00P', '10P', '10.0P'),
            (1e17, '100.00P', '100P', '100P'),
            (1e18, '1.00E', '1E', '1.00E'),
            (1e19, '10.00E', '10E', '10.0E'),
            (1e20, '100.00E', '100E', '100E'),
            (1e21, '1.00Z', '1Z', '1.00Z'),
            (1e22, '10.00Z', '10Z', '10.0Z'),
            (1e23, '100.00Z', '100Z', '100Z'),
            (1e24, '1.00Y', '1Y', '1.00Y'),
            (1e25, '10.00Y', '10Y', '10.0Y'),
            (1e26, '100.00Y', '100Y', '100Y'),
            (1e27, '1.00R', '1R', '1.00R'),
            (1e28, '10.00R', '10R', '10.0R'),
            (1e29, '100.00R', '100R', '100R'),
            (1e30, '1.00Q', '1Q', '1.00Q'),
            (1e31, '10.00Q', '10Q', '10.0Q'),
            (1e32, '100.00Q', '100Q', '100Q'),

            # Larger than largest magnitude
            (1e33, '1000.00Q', '1000Q', '1000Q'),
            (1e34, '10000.00Q', '10000Q', '10000Q'),
            (1e35, '100000.00Q', '100000Q', '100000Q'),
        )

        for test in tests:
            with self.subTest(test=test):
                self.assertEqual(format(Float(test[0]), '.2h'), test[1])
                self.assertEqual(format(Float(test[0]), '.2H'), test[2])
                self.assertEqual(format(Float(test[0]), '#.3H'), test[3])

    def test_output_si_small_pos(self):
        """
        Output for small (<1) positive numbers in SI format
        """

        tests = (
            # (float, .2h, .2H, #.3H)
            (1e-1, '100.00m', '100m', '100m'),
            (1e-2, '10.00m', '10m', '10.0m'),
            (1e-3, '1.00m', '1m', '1.00m'),
            (1e-4, '100.00μ', '100μ', '100μ'),
            (1e-5, '10.00μ', '10μ', '10.0μ'),
            (1e-6, '1.00μ', '1μ', '1.00μ'),
            (1e-7, '100.00n', '100n', '100n'),
            (1e-8, '10.00n', '10n', '10.0n'),
            (1e-9, '1.00n', '1n', '1.00n'),
            (1e-10, '100.00p', '100p', '100p'),
            (1e-11, '10.00p', '10p', '10.0p'),
            (1e-12, '1.00p', '1p', '1.00p'),
            (1e-13, '100.00f', '100f', '100f'),
            (1e-14, '10.00f', '10f', '10.0f'),
            (1e-15, '1.00f', '1f', '1.00f'),
            (1e-16, '100.00a', '100a', '100a'),
            (1e-17, '10.00a', '10a', '10.0a'),
            (1e-18, '1.00a', '1a', '1.00a'),
            (1e-19, '100.00z', '100z', '100z'),
            (1e-20, '10.00z', '10z', '10.0z'),
            (1e-21, '1.00z', '1z', '1.00z'),
            (1e-22, '100.00y', '100y', '100y'),
            (1e-23, '10.00y', '10y', '10.0y'),
            (1e-24, '1.00y', '1y', '1.00y'),
            (1e-25, '100.00r', '100r', '100r'),
            (1e-26, '10.00r', '10r', '10.0r'),
            (1e-27, '1.00r', '1r', '1.00r'),
            (1e-28, '100.00q', '100q', '100q'),


            (1e-29, '10.00q', '10q', '10.0q'),
            (1e-30, '1.00q', '1q', '1.00q'),

            # Smaller than smallest magnitude
            (1e-31, '0.10q', '0.1q', '0.100q'),
            (1e-32, '0.01q', '0.01q', '0.0100q'),
            (1e-33, '0.00q', '0.001q', '0.00100q'),
        )

        for test in tests:
            with self.subTest(test=test):
                self.assertEqual(format(Float(test[0]), '.2h'), test[1])
                self.assertEqual(format(Float(test[0]), '.2H'), test[2])
                self.assertEqual(format(Float(test[0]), '#.3H'), test[3])

    def test_output_iec_pos(self):
        """
        Output for positive numbers in IEC format
        """

        tests = (
            # (float, .2k, .2m, .2K, .2M, #.3K, #.3M)
            (2, '2.00', '2.00', '2', '2', '2.00', '2.00'),
            (2**10, '1.00Ki', '1.00K', '1Ki', '1K', '1.00Ki', '1.00K'),
            (2**20, '1.00Mi', '1.00M', '1Mi', '1M', '1.00Mi', '1.00M'),
            (2**30, '1.00Gi', '1.00G', '1Gi', '1G', '1.00Gi', '1.00G'),
            (2**40, '1.00Ti', '1.00T', '1Ti', '1T', '1.00Ti', '1.00T'),
            (2**50, '1.00Pi', '1.00P', '1Pi', '1P', '1.00Pi', '1.00P'),
            (2**60, '1.00Ei', '1.00E', '1Ei', '1E', '1.00Ei', '1.00E'),
            (2**70, '1.00Zi', '1.00Z', '1Zi', '1Z', '1.00Zi', '1.00Z'),
            (2**80, '1.00Yi', '1.00Y', '1Yi', '1Y', '1.00Yi', '1.00Y'),
        )

        for test in tests:
            with self.subTest(test=test):
                self.assertEqual(format(Float(test[0]), '.2k'), test[1])
                self.assertEqual(format(Float(test[0]), '.2m'), test[2])
                self.assertEqual(format(Float(test[0]), '.2K'), test[3])
                self.assertEqual(format(Float(test[0]), '.2M'), test[4])
                self.assertEqual(format(Float(test[0]), '#.3K'), test[5])
                self.assertEqual(format(Float(test[0]), '#.3M'), test[6])

    def test_input_output_si_large(self):
        """
        Large (>1) numbers input matches output
        """

        for num in ('1.00', '11.00', '101.00',
                    '1.01k', '10.01k', '100.01k',
                    '1.01M', '10.01M', '100.01M',
                    '1.01G', '10.01G', '100.01G',
                    '1.01T', '10.01T', '100.01T',
                    '1.01P', '10.01P', '100.01P',
                    '1.01E', '10.01E', '100.01E',
                    '1.01Z', '10.01Z', '100.01Z',
                    '1.01Y', '10.01Y', '100.01Y',
                    '0.00', '10.00', '100.00',
                    '1.00k', '10.00k', '100.00k',
                    '1.00M', '10.00M', '100.00M',
                    '1.00G', '10.00G', '100.00G',
                    '1.00T', '10.00T', '100.00T',
                    '1.00P', '10.00P', '100.00P',
                    '1.00E', '10.00E', '100.00E',
                    '1.00Z', '10.00Z', '100.00Z',
                    '1.00Y', '10.00Y', '100.00Y'):

            self.assertEqual(format(Float(num), '.2h'), num)
            self.assertEqual(format(Float('-' + num), '.2h'), '-' + num)
            self.assertEqual(format(Float('+' + num), '.2h'), num)

    def test_input_output_si_small(self):
        """
        Large (>1) numbers input matches output
        """

        for num in ('100.00m', '10.00m', '1.00m',
                    '100.00μ', '10.00μ', '1.00μ',
                    '100.00n', '10.00n', '1.00n',
                    '100.00p', '10.00p', '1.00p',
                    '100.00f', '10.00f', '1.00f',
                    '100.00a', '10.00a', '1.00a',
                    '100.00z', '10.00z', '1.00z',
                    '100.00y', '10.00y', '1.00y',
                    '100.01m', '10.01m', '1.01m',
                    '100.01μ', '10.01μ', '1.01μ',
                    '100.01n', '10.01n', '1.01n',
                    '100.01p', '10.01p', '1.01p',
                    '100.01f', '10.01f', '1.01f',
                    '100.01a', '10.01a', '1.01a',
                    '100.01z', '10.01z', '1.01z',
                    '100.01y', '10.01y', '1.01y'):

            self.assertEqual(format(Float(num), '.2h'), num)
            self.assertEqual(format(Float('-' + num), '.2h'), '-' + num)
            self.assertEqual(format(Float('+' + num), '.2h'), num)

    def test_input_output_iec(self):
        """
        Large (>1) numbers input matches output
        """

        for num in ('1.00', '11.00', '101.00',
                    '1.01Ki', '10.01Ki', '100.01Ki',
                    '1.01Mi', '10.01Mi', '100.01Mi',
                    '1.01Gi', '10.01Gi', '100.01Gi',
                    '1.01Ti', '10.01Ti', '100.01Ti',
                    '1.01Pi', '10.01Pi', '100.01Pi',
                    '1.01Ei', '10.01Ei', '100.01Ei',
                    '1.01Zi', '10.01Zi', '100.01Zi',
                    '1.01Yi', '10.01Yi', '100.01Yi',
                    '0.00', '10.00', '100.00',
                    '1.00Ki', '10.00Ki', '100.00Ki',
                    '1.00Mi', '10.00Mi', '100.00Mi',
                    '1.00Gi', '10.00Gi', '100.00Gi',
                    '1.00Ti', '10.00Ti', '100.00Ti',
                    '1.00Pi', '10.00Pi', '100.00Pi',
                    '1.00Ei', '10.00Ei', '100.00Ei',
                    '1.00Zi', '10.00Zi', '100.00Zi',
                    '1.00Yi', '10.00Yi', '100.00Yi'):

            short_form = num[:-1] if num[-1] == 'i' else num
            self.assertEqual(format(Float(num), '.2k'), num)
            self.assertEqual(format(Float(num), '.2m'), short_form)
            self.assertEqual(format(Float('-' + num), '.2k'), '-' + num)
            self.assertEqual(format(Float('-' + num), '.2m'), '-' + short_form)
            self.assertEqual(format(Float('+' + num), '.2k'), num)
            self.assertEqual(format(Float('+' + num), '.2m'), short_form)

    def test_unicode(self):
        """
        For Python 2, test Unicode strings behave the same
        """

        for num in (u'1.00', u'11.00', u'101.00',
                    u'1.01Ki', u'10.01Ki', u'100.01Ki',
                    u'1.01Mi', u'10.01Mi', u'100.01Mi',
                    u'1.01Gi', u'10.01Gi', u'100.01Gi',
                    u'1.01Ti', u'10.01Ti', u'100.01Ti',
                    u'1.01Pi', u'10.01Pi', u'100.01Pi',
                    u'1.01Ei', u'10.01Ei', u'100.01Ei',
                    u'1.01Zi', u'10.01Zi', u'100.01Zi',
                    u'1.01Yi', u'10.01Yi', u'100.01Yi',
                    u'0.00', u'10.00', u'100.00',
                    u'1.00Ki', u'10.00Ki', u'100.00Ki',
                    u'1.00Mi', u'10.00Mi', u'100.00Mi',
                    u'1.00Gi', u'10.00Gi', u'100.00Gi',
                    u'1.00Ti', u'10.00Ti', u'100.00Ti',
                    u'1.00Pi', u'10.00Pi', u'100.00Pi',
                    u'1.00Ei', u'10.00Ei', u'100.00Ei',
                    u'1.00Zi', u'10.00Zi', u'100.00Zi',
                    u'1.00Yi', u'10.00Yi', u'100.00Yi'):

            short_form = num[:-1] if num[-1] == 'i' else num
            self.assertEqual(format(Float(num), '.2k'), num)
            self.assertEqual(format(Float(num), '.2m'), short_form)
            self.assertEqual(format(Float('-' + num), '.2k'), '-' + num)
            self.assertEqual(format(Float('-' + num), '.2m'), '-' + short_form)
            self.assertEqual(format(Float('+' + num), '.2k'), num)
            self.assertEqual(format(Float('+' + num), '.2m'), short_form)

    def test_invalid_prefix(self):
        """
        Invalid prefix provided
        """

        with self.assertRaises(ValueError):
            Float('100D')

    def test_invalid_type(self):
        """
        Invalid type provided
        """

        with self.assertRaises(TypeError):
            Float(3j)

    def test_space(self):
        """
        A single space between value and prefix is accepted
        """

        self.assertEqual(format(Float('3 k'), '.2h'), '3.00k')

        with self.assertRaises(ValueError):
            Float('100\tk')

    def test_invalid_format_spec(self):
        """
        Invalid format spec provided
        """

        with self.assertRaises(ValueError):
            format(Float(3), '100.f')

    def test_standard_format_type(self):
        """
        Standard format type provided
        """

        self.assertEqual(format(Float(3), '.2f'), format(3.0, '.2f'))

    def test_no_format_type(self):
        """
        No format type provided
        """

        self.assertEqual(format(Float(3), '.2'), format(3.0, '.2'))

    def test_no_precision(self):
        """
        No precision provided
        """

        self.assertEqual(format(Float(3000), 'h'), '%fk' % 3.0)
        self.assertEqual(format(Float(3001), 'H'), '3.001k')
        self.assertEqual(format(Float(3001), '#H'), '3.00100k')
        self.assertEqual(format(Float(4147.2), 'k'), '%fKi' % 4.05)
        self.assertEqual(format(Float(4147.2), 'm'), '%fK' % 4.05)
        self.assertEqual(format(Float(4147.2), 'K'), '4.05Ki')
        self.assertEqual(format(Float(4147.2), 'M'), '4.05K')
        self.assertEqual(format(Float(4147.2), '#K'), '4.05000Ki')
        self.assertEqual(format(Float(4147.2), '#M'), '4.05000K')

    def test_width(self):
        """
        Width specified
        """

        self.assertEqual(format(Float(3000), '6.2h'), ' 3.00k')
        self.assertEqual(format(Float(3000), '4.2h'), '3.00k')
        self.assertEqual(format(Float(3000), '00.2h'), '3.00k')

    def test_exclamation(self):
        """
        Flag for space before prefix
        """

        self.assertEqual(format(Float(3000), '!7.2h'), ' 3.00 k')
        self.assertEqual(format(Float(3000), '!4.2h'), '3.00 k')
        self.assertEqual(format(Float(3000), '!.2h'), '3.00 k')

    def test_margin(self):
        """
        Confirm variable margins
        """

        self.assertEqual(format(Float(950), '.2h'), '950.00')
        self.assertEqual(format(Float(950), '%-5.2h'), '0.95k')
        self.assertEqual(format(Float(1000), '%-5.2h'), '1.00k')
        self.assertEqual(format(Float(949.9), '%-5.2h'), '949.90')

        self.assertEqual(format(Float(1000), '%5.2h'), '1000.00')
        self.assertEqual(format(Float(1049), '%5.2h'), '1049.00')
        self.assertEqual(format(Float(1050), '%5.2h'), '1.05k')

    def test_deprecated(self):
        """
        Confirm deprecated format specifiers function
        """

        self.assertEqual(format(Float(2048), '.2j'), '2.00Ki')
        self.assertEqual(format(Float(2048), '.2J'), '2.00K')

        # Unicode for Python 2
        self.assertEqual(format(Float(2048), u'.2j'), '2.00Ki')
        self.assertEqual(format(Float(2048), u'.2J'), '2.00K')


class TestFloatMath(unittest.TestCase):
    """
    Tests for prefixed.Float math
    """

    def test_abs(self):
        """
        Absolute value
        """

        val1 = abs(Float(1000))
        val2 = abs(Float(-1000))

        self.assertEqual(val1, val2)
        self.assertEqual(val1, Float(1000))
        self.assertEqual(val1, 1000.0)
        self.assertIsInstance(val1, Float)
        self.assertIsInstance(val2, Float)

    def test_signs(self):
        """
        Positive and negative signs
        """

        val = - Float(1000)
        self.assertEqual(val, -1000.0)
        self.assertIsInstance(val, Float)

        val = - Float(-1000)
        self.assertEqual(val, 1000.0)
        self.assertIsInstance(val, Float)

        val = + Float(1000)
        self.assertEqual(val, 1000.0)
        self.assertIsInstance(val, Float)

        val = + Float(-1000)
        self.assertEqual(val, -1000.0)
        self.assertIsInstance(val, Float)

    def test_add(self):
        """
        Addition
        """

        samples = (
            (Float(1.0), 1),
            (Float(1.0), 1.0),
            (1, Float(1.0)),
            (1.0, Float(1.0))
        )

        for num1, num2 in samples:
            sum1 = num1 + num2
            self.assertEqual(sum1, 2.0)
            self.assertIsInstance(sum1, Float)

        with self.assertRaises(TypeError):
            Float(1.0) + object()

        with self.assertRaises(TypeError):
            object() + Float(1.0)

    def test_sub(self):
        """
        Subtraction
        """

        samples = (
            (Float(2.0), 1),
            (Float(2.0), 1.0),
            (2, Float(1.0)),
            (2.0, Float(1.0))
        )

        for num1, num2 in samples:
            diff = num1 - num2
            self.assertEqual(diff, 1.0)
            self.assertIsInstance(diff, Float)

        with self.assertRaises(TypeError):
            Float(1.0) - object()

        with self.assertRaises(TypeError):
            object() - Float(1.0)

    def test_mul(self):
        """
        Multiplication
        """

        samples = (
            (Float(2.0), 2),
            (Float(2.0), 2.0),
            (2, Float(2.0)),
            (2.0, Float(2.0))
        )

        for num1, num2 in samples:
            prod = num1 * num2
            self.assertEqual(prod, 4.0)
            self.assertIsInstance(prod, Float)

        with self.assertRaises(TypeError):
            Float(2.0) * object()

        with self.assertRaises(TypeError):
            object() * Float(2.0)

    def test_div(self):
        """
        Division
        """

        samples = (
            (Float(2.0), 2),
            (Float(2.0), 2.0),
            (2, Float(2.0)),
            (2.0, Float(2.0))
        )

        for num1, num2 in samples:
            quot = num1 / num2
            self.assertEqual(quot, 1.0)
            self.assertIsInstance(quot, Float)

        with self.assertRaises(TypeError):
            Float(2.0) / object()

        with self.assertRaises(TypeError):
            object() / Float(2.0)

    def test_floor_div(self):
        """
        Floor division
        """

        samples = (
            (Float(2.4), 2),
            (Float(2.4), 2.0),
            (2, Float(1.5)),
            (2.4, Float(2.0))
        )

        for num1, num2 in samples:
            quot = num1 // num2
            self.assertEqual(quot, 1.0)
            self.assertIsInstance(quot, Float)

        with self.assertRaises(TypeError):
            Float(2.0) // object()

        with self.assertRaises(TypeError):
            object() // Float(2.0)

    def test_mod(self):
        """
        Modulus
        """

        samples = (
            (Float(3.0), 2),
            (Float(3.0), 2.0),
            (3, Float(2.0)),
            (3.0, Float(2.0))
        )

        for num1, num2 in samples:
            rem = num1 % num2
            self.assertEqual(rem, 1.0)
            self.assertIsInstance(rem, Float)

        with self.assertRaises(TypeError):
            Float(3.0) % object()

        with self.assertRaises(TypeError):
            object() % Float(3.0)

    def test_divmod(self):
        """
        Division modulus
        """

        samples = (
            (Float(3.0), 2),
            (Float(3.0), 2.0),
            (3, Float(2.0)),
            (3.0, Float(2.0))
        )

        for num1, num2 in samples:
            quot, rem = divmod(num1, num2)
            self.assertEqual(quot, 1.0)
            self.assertIsInstance(quot, Float)
            self.assertEqual(rem, 1.0)
            self.assertIsInstance(rem, Float)

        with self.assertRaises(TypeError):
            divmod(Float(3.0), object())

        with self.assertRaises(TypeError):
            divmod(object(), Float(3.0))

    def test_pow(self):
        """
        Exponentiation
        """

        samples = (
            (Float(3.0), 2),
            (Float(3.0), 2.0),
            (3, Float(2.0)),
            (3.0, Float(2.0))
        )

        for num1, num2 in samples:
            prod = pow(num1, num2)
            prod2 = num1**num2

            self.assertEqual(prod, prod2)
            self.assertEqual(prod, 9.0)
            self.assertIsInstance(prod, Float)
            self.assertIsInstance(prod2, Float)

        with self.assertRaises(TypeError):
            pow(Float(3.0), object())

        with self.assertRaises(TypeError):
            pow(object(), Float(3.0))

        with self.assertRaises(TypeError):
            Float(3.0) ** object()

        with self.assertRaises(TypeError):
            object() ** Float(3.0)
