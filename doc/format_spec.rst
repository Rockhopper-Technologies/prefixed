..
  Copyright 2017 - 2023 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/prefixed

Format Specification
====================

.. code-block:: abnf

    format_spec     ::=  [[fill]align][sign][#][0][![!]][width][grouping_option][%[-]margin][.precision][type]
    fill            ::=  <any character>
    align           ::=  "<" | ">" | "=" | "^"
    sign            ::=  "+" | "-" | " "
    width           ::=  digit+
    grouping_option ::=  "_" | ","
    precision       ::=  digit+
    type            ::=  "e" | "E" | "f" | "F" | "g" | "G" | "h" | "H" | "k" | "K" | "m" | "M" | "n" | "%"


Prefixed-specific fields are defined below. Descriptions of standard fields can be found in
the `Format Specification Mini-Language`_ documentation.

Prefixed-specific fields
^^^^^^^^^^^^^^^^^^^^^^^^

Flags
-----

+----------+----------------------------------------------------------+
| Flag     | Meaning                                                  |
+==========+==========================================================+
| ``'!'``  | Add a single space between number and prefix             |
+----------+----------------------------------------------------------+
| ``'!!'`` | Same as ``'!'``, but drop space if there is no prefix    |
+---------+----------------------------------------------------------+

Margin
------

By default, a prefix will be used when the magnitude of that prefix is reached.
For example, ``format(Float(999), '.1h')`` will result in ``'999.0'`` and
``format(Float(1000), '.1h')`` will result in ``'1.0k'``.

Margin specifies the percentage to raise or lower these thresholds.

.. code-block:: python

  >>> f'{Float(950):%-5.2h}'
  '0.95k'

  >>> f'{Float(1000):%5.2h}'
  '1000.00'


Presentation Types
------------------

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


  .. _Format Specification Mini-Language: https://docs.python.org/3/library/string.html#formatspec