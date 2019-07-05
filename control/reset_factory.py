#!/usr/bin/env python
#
# Copyright (c) 2019, CESAR. All rights reserved.
#
# SPDX-License-Identifier: BSD 3-Clause

from mongo import MongoConn
from rabbitmq import RabbitMQConn
from reset import Reset
from settings_factory import SettingsFactory

class ResetFactory():
    """
    Factory to create a instance of Reset
    """
    @staticmethod
    def create(file):
        settings = SettingsFactory.create(file)
        mongodb_settings = settings.get('mongodb')
        mongo_conn = MongoConn(mongodb_settings.get('host'),
                               mongodb_settings.get('port'))
        rabbitmq_conn = RabbitMQConn()

        return Reset(mongo_conn, rabbitmq_conn)
