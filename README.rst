.. start-badges

| |docs| |gh_actions| |codecov|
| |pypi| |supported-versions| |supported-implementations|

.. |docs| image:: https://img.shields.io/readthedocs/prefixed.svg?style=plastic&logo=read-the-docs
    :target: https://prefixed.readthedocs.org
    :alt: Documentation Status

.. |gh_actions| image:: https://img.shields.io/github/workflow/status/Rockhopper-Technologies/prefixed/Tests?event=push&logo=github-actions&style=plastic
    :target: https://github.com/Rockhopper-Technologies/prefixed/actions/workflows/tests.yml
    :alt: GitHub Actions Status

.. |travis| image:: https://img.shields.io/travis/com/Rockhopper-Technologies/prefixed.svg?style=plastic&logo=travis
    :target: https://travis-ci.com/Rockhopper-Technologies/prefixed
    :alt: Travis-CI Build Status

.. |codecov| image:: https://img.shields.io/codecov/c/github/Rockhopper-Technologies/prefixed.svg?style=plastic&logo=codecov
    :target: https://codecov.io/gh/Rockhopper-Technologies/prefixed
    :alt: Coverage Status

.. |pypi| image:: https://img.shields.io/pypi/v/prefixed.svg?style=plastic&logo=pypi
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/prefixed

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/prefixed.svg?style=plastic&logo=pypi
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/prefixed

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/prefixed.svg?style=plastic&logo=pypi
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/prefixed

.. end-badges


Overview
========

Prefixed provides an alternative implementation of the built-in float_ which supports
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

Because `prefixed.Float`_ inherits from the built-in float_, it behaves
exactly the same in most cases.

When a math operation is performed with another real number type
(float_, int_), the result will be a `prefixed.Float`_ instance.


Presentation Types
^^^^^^^^^^^^^^^^^^

Additional presentation types ``'h'``, ``'H'``, ``'k'``, ``'K'``,
``'m'``, and ``'M'`` are supported for f-strings and `format()`_.

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


String Initialization
^^^^^^^^^^^^^^^^^^^^^

When initializing from strings, SI and IEC prefixes are honored

.. code-block:: python

    >>> Float('2k')
    Float(2000.0)

    >>> Float('2Ki')
    Float(2048.0)


Additional Flags
^^^^^^^^^^^^^^^^

An additional format flag '!' is available which adds a space before the prefix

.. code-block:: python

  >>> f'{Float(3250):!.2h}'
  '3.25 k'


Significant Digits
^^^^^^^^^^^^^^^^^^

When the ``'H'``, ``'K``, or ``'M'`` presentation types are used, precision is treated as
the number of `significant digits`_ to include. Standard rounding will occur for the final digit.

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


Adjustable Thresholds
^^^^^^^^^^^^^^^^^^^^^

An additional field, margin, can be specified which lowers or raises the threshold for
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
.. _signifigant digits: https://en.wikipedia.org/wiki/Significant_figures


Supported Prefixes
==================

SI (Decimal) Prefixes
^^^^^^^^^^^^^^^^^^^^^

+--------+-------+----------+
| Prefix | Name  |   Base   |
+========+=======+==========+
|   Y    | Yotta | |10^24|  |
+--------+-------+----------+
|   Z    | Zetta | |10^21|  |
+--------+-------+----------+
|   E    | Exa   | |10^18|  |
+--------+-------+----------+
|   P    | Peta  | |10^15|  |
+--------+-------+----------+
|   T    | Tera  | |10^12|  |
+--------+-------+----------+
|   G    | Giga  | |10^9|   |
+--------+-------+----------+
|   M    | Mega  | |10^6|   |
+--------+-------+----------+
|   k    | Kilo  | |10^3|   |
+--------+-------+----------+
|   m    | Milli | |10^-3|  |
+--------+-------+----------+
|   μ    | Micro | |10^-6|  |
+--------+-------+----------+
|   n    | Nano  | |10^-9|  |
+--------+-------+----------+
|   p    | Pico  | |10^-12| |
+--------+-------+----------+
|   f    | Femto | |10^-15| |
+--------+-------+----------+
|   a    | Atto  | |10^-18| |
+--------+-------+----------+
|   z    | Zepto | |10^-21| |
+--------+-------+----------+
|   y    | Yocto | |10^-24| |
+--------+-------+----------+

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

.. _SI (decimal): https://en.wikipedia.org/wiki/Metric_prefix
.. _IEC (binary): https://en.wikipedia.org/wiki/Binary_prefix
.. _float: https://docs.python.org/3/library/functions.html#float
.. _int: https://docs.python.org/3/library/functions.html#int
.. _prefixed.Float: https://prefixed.readthedocs.io/en/stable/api.html#prefixed.Float
.. _format(): https://docs.python.org/3/library/functions.html#format

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

.. |2^80| replace:: 2\ :sup:`80`\
.. |2^70| replace:: 2\ :sup:`70`\
.. |2^60| replace:: 2\ :sup:`60`\
.. |2^50| replace:: 2\ :sup:`50`\
.. |2^40| replace:: 2\ :sup:`40`\
.. |2^30| replace:: 2\ :sup:`30`\
.. |2^20| replace:: 2\ :sup:`20`\
.. |2^10| replace:: 2\ :sup:`10`\
