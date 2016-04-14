#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2016
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

""" This module contains the base class for handlers as used by the
Dispatcher """

from .handler import Handler
from telegram import Update


class CommandHandler(Handler):

    def __init__(self, command, callback, pass_args=False,
                 pass_update_queue=False):
        super(Handler).__init__(callback, pass_update_queue)
        self.command = command
        self.pass_args = pass_args

    def checkUpdate(self, update):
        return (isinstance(update, Update) and
                update.message and
                update.message.text and
                update.message.text.startswith('/') and
                update.message.text[1:].split(' ')[0].split('@')[0] ==
                self.command)

    def handleUpdate(self, update, dispatcher):
        optional_args = self.collectOptionalArgs(dispatcher)

        if self.pass_args:
            optional_args['args'] = update.message.text.split(' ')[1:]

        self.callback(dispatcher.bot, update, **optional_args)
