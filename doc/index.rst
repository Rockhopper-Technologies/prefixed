..
  Copyright 2020 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/prefixed

Welcome to Prefixed's documentation!
====================================

.. toctree::
   :hidden:

   self
   api.rst

Overview
========

Prefixed provides an alternative implementation of the built-in :py:class:`float`

Key differences:

- Format type 'h' will output with an SI prefix (ex: k for 1000)
- Format type 'j' will output with an IEC prefix (ex: Ki for 1024)
- Format type 'J' will output with an IEC prefix minus the i (ex: K for 1024)
- When initializing from strings, SI and IEC prefixes are honored

    - SI Example: Float('3k')
    - IEC Example: Float('3Ki')
