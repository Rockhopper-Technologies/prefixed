..
  Copyright 2020 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/prefixed

.. toctree::
   :hidden:

   self
   prefixes.rst
   api.rst

Overview
========

Prefixed provides an alternative implementation of the built-in :py:class:`float` which supports
formatted output with `SI (decimal)`_ and `IEC (binary)`_ prefixes.

.. code-block:: python

  >>> f'{Float(3250):.2h}'
  '3.25k'

  >>> '{:.2h}s'.format(Float(.00001534))
  '15.34μs'

  >>> '{:.2j}B'.format(Float(42467328))
  '40.50MiB'

  >>> f'{Float(2048):.2J}B'
  '2.00KB'

Because :py:class:`prefixed.Float` inherits from the built-in :py:class:`float`, it behaves
exactly the same in most cases.

Key differences:

- When a math operation is performed with another real number type
  (:py:class:`float`, :py:class:`int`), the result will be a :py:class:`prefixed.Float` instance.

- Additional format types ``'h'``, ``'j'``, and ``'J'`` are supported for
  f-strings and :py:func:`format`.

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

- When initializing from strings, SI and IEC prefixes are honored

  .. code-block:: python

      >>> Float('2k')
      Float(2000.0)

      >>> Float('2Ki')
      Float(2048.0)

.. _SI (decimal): https://en.wikipedia.org/wiki/Metric_prefix
.. _IEC (binary): https://en.wikipedia.org/wiki/Binary_prefix
