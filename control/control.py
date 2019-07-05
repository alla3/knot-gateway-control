#!/usr/bin/env python
#
# Copyright (c) 2019, CESAR. All rights reserved.
#
# SPDX-License-Identifier: BSD 3-Clause

import dbus
import dbus.service
import dbus.mainloop.glib
import os

from reset_factory import ResetFactory
from dbus.exceptions import DBusException

class Control(dbus.service.Object):
    """
    Control KNoT Gateway state using a dbus implementation
    """

    def __init__(self):
        self.reset = ResetFactory.create('settings.json')

    def start(self):
        self._bus_name = dbus.service.BusName(
            'br.org.cesar.knot.control', dbus.SystemBus())
        dbus.service.Object.__init__(
            self, self._bus_name, '/br/org/cesar/knot/control')

    @dbus.service.method('br.org.cesar.knot.control.Reset')
    def FactoryReset(self):
        try:
            self.reset.factory_reset()
        except Exception as error:
            raise DBusException(str(error))

