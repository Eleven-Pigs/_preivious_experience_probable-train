#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2017
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains the classes that represent Telegram
InputVenueMessageContent"""

from telegram import InputMessageContent


class InputVenueMessageContent(InputMessageContent):
    """Base class for Telegram InputVenueMessageContent Objects"""

    def __init__(self, latitude, longitude, title, address, foursquare_id=None, **kwargs):
        # Required
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        # Optionals
        self.foursquare_id = foursquare_id

    @classmethod
    def de_json(cls, data, bot):
        return cls(**data)
