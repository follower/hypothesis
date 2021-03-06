# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

import random

import pytest
from hypothesis.extra.datetime import draw_day_for_month


def test_draw_day_for_month_errors_on_bad_month():
    with pytest.raises(ValueError):
        draw_day_for_month(random, 2001, 13)
