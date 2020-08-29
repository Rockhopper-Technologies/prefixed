# -*- coding: utf-8 -*-
# Copyright 2020 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Test file for prefixed.Float
"""

import unittest

from prefixed import Float


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

    # pylint: disable=too-many-statements
    def test_output_si_large_pos(self):
        """
        Output for large (>=1) positive numbers in SI format
        """

        self.assertEqual(format(Float(1), '.2h'), '1.00')
        self.assertEqual(format(Float(11), '.2h'), '11.00')
        self.assertEqual(format(Float(101), '.2h'), '101.00')
        self.assertEqual(format(Float(1010), '.2h'), '1.01k')
        self.assertEqual(format(Float(10010), '.2h'), '10.01k')
        self.assertEqual(format(Float(100010), '.2h'), '100.01k')
        self.assertEqual(format(Float(1010000), '.2h'), '1.01M')
        self.assertEqual(format(Float(10010000), '.2h'), '10.01M')
        self.assertEqual(format(Float(100010000), '.2h'), '100.01M')
        self.assertEqual(format(Float(1010000000), '.2h'), '1.01G')
        self.assertEqual(format(Float(10010000000), '.2h'), '10.01G')
        self.assertEqual(format(Float(100010000000), '.2h'), '100.01G')
        self.assertEqual(format(Float(1010000000000), '.2h'), '1.01T')
        self.assertEqual(format(Float(10010000000000), '.2h'), '10.01T')
        self.assertEqual(format(Float(100010000000000), '.2h'), '100.01T')
        self.assertEqual(format(Float(1010000000000000), '.2h'), '1.01P')
        self.assertEqual(format(Float(10010000000000000), '.2h'), '10.01P')
        self.assertEqual(format(Float(100010000000000000), '.2h'), '100.01P')
        self.assertEqual(format(Float(1010000000000000000), '.2h'), '1.01E')
        self.assertEqual(format(Float(10010000000000000000), '.2h'), '10.01E')
        self.assertEqual(format(Float(100010000000000000000), '.2h'), '100.01E')
        self.assertEqual(format(Float(1010000000000000000000), '.2h'), '1.01Z')
        self.assertEqual(format(Float(10010000000000000000000), '.2h'), '10.01Z')
        self.assertEqual(format(Float(100010000000000000000000), '.2h'), '100.01Z')
        self.assertEqual(format(Float(1010000000000000000000000), '.2h'), '1.01Y')
        self.assertEqual(format(Float(10010000000000000000000000), '.2h'), '10.01Y')
        self.assertEqual(format(Float(100010000000000000000000000), '.2h'), '100.01Y')

        self.assertEqual(format(Float(0), '.2h'), '0.00')
        self.assertEqual(format(Float(10), '.2h'), '10.00')
        self.assertEqual(format(Float(100), '.2h'), '100.00')
        self.assertEqual(format(Float(1000), '.2h'), '1.00k')
        self.assertEqual(format(Float(10000), '.2h'), '10.00k')
        self.assertEqual(format(Float(100000), '.2h'), '100.00k')
        self.assertEqual(format(Float(1000000), '.2h'), '1.00M')
        self.assertEqual(format(Float(10000000), '.2h'), '10.00M')
        self.assertEqual(format(Float(100000000), '.2h'), '100.00M')
        self.assertEqual(format(Float(1000000000), '.2h'), '1.00G')
        self.assertEqual(format(Float(10000000000), '.2h'), '10.00G')
        self.assertEqual(format(Float(100000000000), '.2h'), '100.00G')
        self.assertEqual(format(Float(1000000000000), '.2h'), '1.00T')
        self.assertEqual(format(Float(10000000000000), '.2h'), '10.00T')
        self.assertEqual(format(Float(100000000000000), '.2h'), '100.00T')
        self.assertEqual(format(Float(1000000000000000), '.2h'), '1.00P')
        self.assertEqual(format(Float(10000000000000000), '.2h'), '10.00P')
        self.assertEqual(format(Float(100000000000000000), '.2h'), '100.00P')
        self.assertEqual(format(Float(1000000000000000000), '.2h'), '1.00E')
        self.assertEqual(format(Float(10000000000000000000), '.2h'), '10.00E')
        self.assertEqual(format(Float(100000000000000000000), '.2h'), '100.00E')
        self.assertEqual(format(Float(1000000000000000000000), '.2h'), '1.00Z')
        self.assertEqual(format(Float(10000000000000000000000), '.2h'), '10.00Z')
        self.assertEqual(format(Float(100000000000000000000000), '.2h'), '100.00Z')
        self.assertEqual(format(Float(1000000000000000000000000), '.2h'), '1.00Y')
        self.assertEqual(format(Float(10000000000000000000000000), '.2h'), '10.00Y')
        self.assertEqual(format(Float(100000000000000000000000000), '.2h'), '100.00Y')

    def test_output_si_small_pos(self):
        """
        Output for large (<1) positive numbers in SI format
        """

        self.assertEqual(format(Float(0.1), '.2h'), '100.00m')
        self.assertEqual(format(Float(0.01), '.2h'), '10.00m')
        self.assertEqual(format(Float(0.001), '.2h'), '1.00m')
        self.assertEqual(format(Float(0.0001), '.2h'), '100.00μ')
        self.assertEqual(format(Float(0.00001), '.2h'), '10.00μ')
        self.assertEqual(format(Float(0.000001), '.2h'), '1.00μ')
        self.assertEqual(format(Float(0.0000001), '.2h'), '100.00n')
        self.assertEqual(format(Float(0.00000001), '.2h'), '10.00n')
        self.assertEqual(format(Float(0.000000001), '.2h'), '1.00n')
        self.assertEqual(format(Float(0.0000000001), '.2h'), '100.00p')
        self.assertEqual(format(Float(0.00000000001), '.2h'), '10.00p')
        self.assertEqual(format(Float(0.000000000001), '.2h'), '1.00p')
        self.assertEqual(format(Float(0.0000000000001), '.2h'), '100.00f')
        self.assertEqual(format(Float(0.00000000000001), '.2h'), '10.00f')
        self.assertEqual(format(Float(0.000000000000001), '.2h'), '1.00f')
        self.assertEqual(format(Float(0.0000000000000001), '.2h'), '100.00a')
        self.assertEqual(format(Float(0.00000000000000001), '.2h'), '10.00a')
        self.assertEqual(format(Float(0.000000000000000001), '.2h'), '1.00a')
        self.assertEqual(format(Float(0.0000000000000000001), '.2h'), '100.00z')
        self.assertEqual(format(Float(0.00000000000000000001), '.2h'), '10.00z')
        self.assertEqual(format(Float(0.000000000000000000001), '.2h'), '1.00z')
        self.assertEqual(format(Float(0.0000000000000000000001), '.2h'), '100.00y')
        self.assertEqual(format(Float(0.00000000000000000000001), '.2h'), '10.00y')
        self.assertEqual(format(Float(0.000000000000000000000001), '.2h'), '1.00y')

        self.assertEqual(format(Float(0.10001), '.2h'), '100.01m')
        self.assertEqual(format(Float(0.01001), '.2h'), '10.01m')
        self.assertEqual(format(Float(0.00101), '.2h'), '1.01m')
        self.assertEqual(format(Float(0.00010001), '.2h'), '100.01μ')
        self.assertEqual(format(Float(0.00001001), '.2h'), '10.01μ')
        self.assertEqual(format(Float(0.00000101), '.2h'), '1.01μ')
        self.assertEqual(format(Float(0.00000010001), '.2h'), '100.01n')
        self.assertEqual(format(Float(0.00000001001), '.2h'), '10.01n')
        self.assertEqual(format(Float(0.00000000101), '.2h'), '1.01n')
        self.assertEqual(format(Float(0.00000000010001), '.2h'), '100.01p')
        self.assertEqual(format(Float(0.00000000001001), '.2h'), '10.01p')
        self.assertEqual(format(Float(0.00000000000101), '.2h'), '1.01p')
        self.assertEqual(format(Float(0.00000000000010001), '.2h'), '100.01f')
        self.assertEqual(format(Float(0.00000000000001001), '.2h'), '10.01f')
        self.assertEqual(format(Float(0.00000000000000101), '.2h'), '1.01f')
        self.assertEqual(format(Float(0.00000000000000010001), '.2h'), '100.01a')
        self.assertEqual(format(Float(0.00000000000000001001), '.2h'), '10.01a')
        self.assertEqual(format(Float(0.00000000000000000101), '.2h'), '1.01a')
        self.assertEqual(format(Float(0.00000000000000000010001), '.2h'), '100.01z')
        self.assertEqual(format(Float(0.00000000000000000001001), '.2h'), '10.01z')
        self.assertEqual(format(Float(0.00000000000000000000101), '.2h'), '1.01z')
        self.assertEqual(format(Float(0.00000000000000000000010001), '.2h'), '100.01y')
        self.assertEqual(format(Float(0.00000000000000000000001001), '.2h'), '10.01y')
        self.assertEqual(format(Float(0.00000000000000000000000101), '.2h'), '1.01y')

    def test_output_iec_pos(self):
        """
        Output for positive numbers in IEC format
        """

        self.assertEqual(format(Float(2), '.2j'), '2.00')
        self.assertEqual(format(Float(2), '.2J'), '2.00')
        self.assertEqual(format(Float(2**10), '.2j'), '1.00Ki')
        self.assertEqual(format(Float(2**10), '.2J'), '1.00K')
        self.assertEqual(format(Float(2**20), '.2j'), '1.00Mi')
        self.assertEqual(format(Float(2**20), '.2J'), '1.00M')
        self.assertEqual(format(Float(2**30), '.2j'), '1.00Gi')
        self.assertEqual(format(Float(2**30), '.2J'), '1.00G')
        self.assertEqual(format(Float(2**40), '.2j'), '1.00Ti')
        self.assertEqual(format(Float(2**40), '.2J'), '1.00T')
        self.assertEqual(format(Float(2**50), '.2j'), '1.00Pi')
        self.assertEqual(format(Float(2**50), '.2J'), '1.00P')
        self.assertEqual(format(Float(2**60), '.2j'), '1.00Ei')
        self.assertEqual(format(Float(2**60), '.2J'), '1.00E')
        self.assertEqual(format(Float(2**70), '.2j'), '1.00Zi')
        self.assertEqual(format(Float(2**70), '.2J'), '1.00Z')
        self.assertEqual(format(Float(2**80), '.2j'), '1.00Yi')
        self.assertEqual(format(Float(2**80), '.2J'), '1.00Y')

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
            self.assertEqual(format(Float(num), '.2j'), num)
            self.assertEqual(format(Float(num), '.2J'), short_form)
            self.assertEqual(format(Float('-' + num), '.2j'), '-' + num)
            self.assertEqual(format(Float('-' + num), '.2J'), '-' + short_form)
            self.assertEqual(format(Float('+' + num), '.2j'), num)
            self.assertEqual(format(Float('+' + num), '.2J'), short_form)

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
            self.assertEqual(format(Float(num), '.2j'), num)
            self.assertEqual(format(Float(num), '.2J'), short_form)
            self.assertEqual(format(Float('-' + num), '.2j'), '-' + num)
            self.assertEqual(format(Float('-' + num), '.2J'), '-' + short_form)
            self.assertEqual(format(Float('+' + num), '.2j'), num)
            self.assertEqual(format(Float('+' + num), '.2J'), short_form)

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

    def test_extra_characters(self):
        """
        Units provided
        """

        self.assertEqual(format(Float('3kg'), '.2h'), '3.00k')

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
