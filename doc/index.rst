..
  Copyright 2020 - 2022 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/prefixed

.. toctree::
   :hidden:

   self
   prefixes.rst
   format_spec.rst
   api.rst

Overview
========

Prefixed provides an alternative implementation of the built-in :py:class:`float` which supports
formatted output with `SI (decimal)`_ and `IEC (binary)`_ prefixes.

.. code-block:: python

  >>> from prefixed import Float

  >>> f'{Float(3250):.2h}'
  '3.25k'

  >>> '{:.2h}s'.format(Float(.00001534))
  '15.34μs'

  >>> '{:.2k}B'.format(Float(42467328))
  '40.50MiB'

  >>> f'{Float(2048):.2m}B'
  '2.00KB'

Because :py:class:`prefixed.Float` inherits from the built-in :py:class:`float`, it behaves
exactly the same in most cases.

Key differences:

- When a math operation is performed with another real number type
  (:py:class:`float`, :py:class:`int`), the result will be a :py:class:`prefixed.Float` instance.

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

.. _SI (decimal): https://en.wikipedia.org/wiki/Metric_prefix
.. _IEC (binary): https://en.wikipedia.org/wiki/Binary_prefix
