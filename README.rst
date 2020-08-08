Overview
========

Prefixed provides an alternative implementation of the built-in `float`_

Key differences:

- Format type 'h' will output with an SI prefix (ex: k for 1000)
- Format type 'j' will output with an IEC prefix (ex: Ki for 1024)
- Format type 'J' will output with an IEC prefix minus the i (ex: K for 1024)
- When initializing from strings, SI and IEC prefixes are honored
    - SI Example: Float('3k')
    - IEC Example: Float('3Ki')


.. _float: https://docs.python.org/3/library/functions.html#float
