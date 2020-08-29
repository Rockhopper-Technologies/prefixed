# -*- coding: utf-8 -*-
# Copyright 2020 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Test file for prefixed format spec parsing
"""

import unittest

from prefixed import RE_FORMAT_SPEC

FIELDS = ('fill', 'align', 'sign', 'alt', 'zero', 'prefix_space',
          'width', 'grouping', 'margin', 'precision', 'type')


class FormatSpec(unittest.TestCase):
    """
    Tests for format spec regular expression
    """

    def test_fill_align(self):
        """
        Test fill
        """
        for align in '<>=^':
            spec = RE_FORMAT_SPEC.match('.%s' % align).groupdict()
            self.assertEqual(spec.pop('fill'), '.')
            self.assertEqual(spec.pop('align'), align)
            self.assertTrue(all(field is None for field in spec.values()))

    def test_align(self):
        """
        Test alignment
        """
        for align in '<>=^':
            spec = RE_FORMAT_SPEC.match(align).groupdict()
            self.assertEqual(spec.pop('align'), align)
            self.assertTrue(all(field is None for field in spec.values()))

    def test_sign(self):
        """
        Test sign
        """
        for sign in '+- ':
            spec = RE_FORMAT_SPEC.match(sign).groupdict()
            self.assertEqual(spec.pop('sign'), sign)
            self.assertTrue(all(field is None for field in spec.values()))

    def test_alt(self):
        """
        Test alternative form
        """
        spec = RE_FORMAT_SPEC.match('#').groupdict()
        self.assertEqual(spec.pop('alt'), '#')
        self.assertTrue(all(field is None for field in spec.values()))

    def test_zero(self):
        """
        Test zero alias
        """
        spec = RE_FORMAT_SPEC.match('0').groupdict()
        self.assertEqual(spec.pop('zero'), '0')
        self.assertTrue(all(field is None for field in spec.values()))

    def test_space_prefix(self):
        """
        Test space before prefix flag
        """
        spec = RE_FORMAT_SPEC.match('!').groupdict()
        self.assertEqual(spec.pop('prefix_space'), '!')
        self.assertTrue(all(field is None for field in spec.values()))

    def test_width(self):
        """
        Test width
        """
        spec = RE_FORMAT_SPEC.match('40').groupdict()
        self.assertEqual(spec.pop('width'), '40')
        self.assertTrue(all(field is None for field in spec.values()))

    def test_grouping(self):
        """
        Test grouping options
        """
        for opt in ',_':
            spec = RE_FORMAT_SPEC.match(opt).groupdict()
            self.assertEqual(spec.pop('grouping'), opt)
            self.assertTrue(all(field is None for field in spec.values()))

    def test_margin(self):
        """
        Test margin
        """
        spec = RE_FORMAT_SPEC.match('%4').groupdict()
        self.assertEqual(spec.pop('margin'), '4')
        self.assertTrue(all(field is None for field in spec.values()))

        spec = RE_FORMAT_SPEC.match('%-4').groupdict()
        self.assertEqual(spec.pop('margin'), '-4')
        self.assertTrue(all(field is None for field in spec.values()))

    def test_precision(self):
        """
        Test precision
        """
        spec = RE_FORMAT_SPEC.match('.4').groupdict()
        self.assertEqual(spec.pop('precision'), '4')
        self.assertTrue(all(field is None for field in spec.values()))

    def test_type(self):
        """
        Test format type
        """

        for item in ('f', 'h', 'k', '?', '%'):
            spec = RE_FORMAT_SPEC.match(item).groupdict()
            self.assertEqual(spec.pop('type'), item)
            self.assertTrue(all(field is None for field in spec.values()))
