..
  Copyright 2020 - 2024 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/prefixed

Supported Prefixes
==================

SI (Decimal) Prefixes
^^^^^^^^^^^^^^^^^^^^^

+--------+--------+----------+
| Prefix | Name   |   Base   |
+========+========+==========+
|   Q    | Quetta | |10^30|  |
+--------+--------+----------+
|   R    | Ronna  | |10^27|  |
+--------+--------+----------+
|   Y    | Yotta  | |10^24|  |
+--------+--------+----------+
|   Z    | Zetta  | |10^21|  |
+--------+--------+----------+
|   E    | Exa    | |10^18|  |
+--------+--------+----------+
|   P    | Peta   | |10^15|  |
+--------+--------+----------+
|   T    | Tera   | |10^12|  |
+--------+--------+----------+
|   G    | Giga   | |10^9|   |
+--------+--------+----------+
|   M    | Mega   | |10^6|   |
+--------+--------+----------+
|   k    | Kilo   | |10^3|   |
+--------+--------+----------+
|   m    | Milli  | |10^-3|  |
+--------+--------+----------+
|   μ    | Micro  | |10^-6|  |
+--------+--------+----------+
|   n    | Nano   | |10^-9|  |
+--------+--------+----------+
|   p    | Pico   | |10^-12| |
+--------+--------+----------+
|   f    | Femto  | |10^-15| |
+--------+--------+----------+
|   a    | Atto   | |10^-18| |
+--------+--------+----------+
|   z    | Zepto  | |10^-21| |
+--------+--------+----------+
|   y    | Yocto  | |10^-24| |
+--------+--------+----------+
|   r    | Ronto  | |10^-27| |
+--------+--------+----------+
|   q    | Quecto | |10^-30| |
+--------+--------+----------+

.. note::
  Prefixed uses the lowercase Greek letter mu ('μ'), U+03BC, to represent the Micro
  prefix, but will accept input using the Micro sign ('µ'), U+00B5. This complies
  with the preference defined in `Unicode Technical Report #25`_ section 2.5.


IEC (Binary) Prefixes
^^^^^^^^^^^^^^^^^^^^^

+--------+------+--------+
| Prefix | Name |  Base  |
+========+======+========+
|   Y    | Yobi | |2^80| |
+--------+------+--------+
|   Z    | Zebi | |2^70| |
+--------+------+--------+
|   E    | Exbi | |2^60| |
+--------+------+--------+
|   P    | Pedi | |2^50| |
+--------+------+--------+
|   T    | Tebi | |2^40| |
+--------+------+--------+
|   G    | Gibi | |2^30| |
+--------+------+--------+
|   M    | Mebi | |2^20| |
+--------+------+--------+
|   K    | Kibi | |2^10| |
+--------+------+--------+

.. _Unicode Technical Report #25: https://www.unicode.org/reports/tr25

.. |10^30| replace:: 10\ :sup:`30`\
.. |10^27| replace:: 10\ :sup:`27`\
.. |10^24| replace:: 10\ :sup:`24`\
.. |10^21| replace:: 10\ :sup:`21`\
.. |10^18| replace:: 10\ :sup:`18`\
.. |10^15| replace:: 10\ :sup:`15`\
.. |10^12| replace:: 10\ :sup:`12`\
.. |10^9| replace:: 10\ :sup:`9`\
.. |10^6| replace:: 10\ :sup:`6`\
.. |10^3| replace:: 10\ :sup:`3`\
.. |10^-3| replace:: 10\ :sup:`-3`\
.. |10^-6| replace:: 10\ :sup:`-6`\
.. |10^-9| replace:: 10\ :sup:`-9`\
.. |10^-12| replace:: 10\ :sup:`-12`\
.. |10^-15| replace:: 10\ :sup:`-15`\
.. |10^-18| replace:: 10\ :sup:`-18`\
.. |10^-21| replace:: 10\ :sup:`-21`\
.. |10^-24| replace:: 10\ :sup:`-24`\
.. |10^-27| replace:: 10\ :sup:`-27`\
.. |10^-30| replace:: 10\ :sup:`-30`\

.. |2^80| replace:: 2\ :sup:`80`\
.. |2^70| replace:: 2\ :sup:`70`\
.. |2^60| replace:: 2\ :sup:`60`\
.. |2^50| replace:: 2\ :sup:`50`\
.. |2^40| replace:: 2\ :sup:`40`\
.. |2^30| replace:: 2\ :sup:`30`\
.. |2^20| replace:: 2\ :sup:`20`\
.. |2^10| replace:: 2\ :sup:`10`\