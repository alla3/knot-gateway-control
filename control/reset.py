#!/usr/bin/env python
#
# Copyright (c) 2019, CESAR. All rights reserved.
#
# SPDX-License-Identifier: BSD 3-Clause

import logging
import os

class Reset():
    """
    Control KNoT Gateway state using a dbus implementation
    """
    def __init__(self, mongo_conn, rabbitmq_conn):
        self._rabbitmq_conn = rabbitmq_conn
        self._mongo_conn = mongo_conn

    def stop_process(self, process):
        logging.info('Stopping process: ' + process)
        stop = '/etc/knot/stop.sh '
        os.system(stop + process)

    def stop_processes(self):
        processes = ['knot-fog', 'knot-connector']
        for proc in processes:
            self.stop_process(proc)

    def factory_reset(self):
        # stop Daemons
        self.stop_processes()

        # clear RabbitMQ
        self._rabbitmq_conn.connect()
        self._rabbitmq_conn.remove_all_queues()
        self._rabbitmq_conn.close()

        # clear MongoDB
        self._mongo_conn.connect()
        self._mongo_conn.drop_all_db()
        self._mongo_conn.close()

        # reboot
        os.system('reboot')
