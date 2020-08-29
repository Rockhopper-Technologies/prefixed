..
  Copyright 2017 - 2020 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/prefixed

Format Specification
====================

.. code-block:: abnf

    format_spec     ::=  [[fill]align][sign][#][0][!][width][grouping_option][.precision][type]
    fill            ::=  <any character>
    align           ::=  "<" | ">" | "=" | "^"
    sign            ::=  "+" | "-" | " "
    width           ::=  digit+
    grouping_option ::=  "_" | ","
    precision       ::=  digit+
    type            ::=  "e" | "E" | "f" | "F" | "g" | "G" | "h" | "j" | "J" | "n" | "%"


Prefixed-specific fields are defined below. Descriptions of standard fields can be found in
the `Format Specification Mini-Language`_ documentation.

Prefixed-specific fields:

  +---------+----------------------------------------------------------+
  | Type    | Meaning                                                  |
  +=========+==========================================================+
  | ``'h'`` | SI format. Outputs the number with closest divisible     |
  |         | SI prefix. (k, M, G, ...)                                |
  +---------+----------------------------------------------------------+
  | ``'j'`` | IEC Format. Outputs the number with closest divisible    |
  |         | IEC prefix. (Ki, Mi, Gi, ...)                            |
  +---------+----------------------------------------------------------+
  | ``'J'`` | Short IEC Format. Same as ``'j'`` but only a single      |
  |         | character.   (K, M, G, ...)                              |
  +---------+----------------------------------------------------------+

  +---------+----------------------------------------------------------+
  | Flag    | Meaning                                                  |
  +=========+==========================================================+
  | ``'!'`` | Add a single space between number and prefix             |
  +---------+----------------------------------------------------------+

  .. _Format Specification Mini-Language: https://docs.python.org/3/library/string.html#formatspec