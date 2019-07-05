#!/usr/bin/env python
#
# Copyright (c) 2019, CESAR. All rights reserved.
#
# SPDX-License-Identifier: BSD 3-Clause

from pkg_resources import resource_string

import json

class SettingsFactory():
    """
    Factory to create settings with Reset parameters
    """
    @staticmethod
    def create(filename):
        json_file = resource_string(__name__, filename)
        settings = json.loads(json_file)

        return settings
