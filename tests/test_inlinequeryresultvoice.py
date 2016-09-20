#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2016
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains a object that represents Tests for Telegram
InlineQueryResultVoice"""

import sys
import unittest

sys.path.append('.')

import telegram
from tests.base import BaseTest


class InlineQueryResultVoiceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Telegram InlineQueryResultVoice."""

    def setUp(self):
        self.id = 'id'
        self.type = 'voice'
        self.voice_url = 'voice url'
        self.title = 'title'
        self.voice_duration = 'voice_duration'
        self.input_message_content = telegram.InputTextMessageContent('input_message_content')
        self.reply_markup = telegram.InlineKeyboardMarkup([[
            telegram.InlineKeyboardButton('reply_markup')
        ]])

        self.json_dict = {
            'type': self.type,
            'id': self.id,
            'voice_url': self.voice_url,
            'title': self.title,
            'voice_duration': self.voice_duration,
            'input_message_content': self.input_message_content.to_dict(),
            'reply_markup': self.reply_markup.to_dict(),
        }

    def test_voice_de_json(self):
        voice = telegram.InlineQueryResultVoice.de_json(self.json_dict, self._bot)

        self.assertEqual(voice.type, self.type)
        self.assertEqual(voice.id, self.id)
        self.assertEqual(voice.voice_url, self.voice_url)
        self.assertEqual(voice.title, self.title)
        self.assertEqual(voice.voice_duration, self.voice_duration)
        self.assertDictEqual(voice.input_message_content.to_dict(),
                             self.input_message_content.to_dict())
        self.assertDictEqual(voice.reply_markup.to_dict(), self.reply_markup.to_dict())

    def test_voice_to_json(self):
        voice = telegram.InlineQueryResultVoice.de_json(self.json_dict, self._bot)

        self.assertTrue(self.is_json(voice.to_json()))

    def test_voice_to_dict(self):
        voice = telegram.InlineQueryResultVoice.de_json(self.json_dict, self._bot).to_dict()

        self.assertTrue(self.is_dict(voice))
        self.assertDictEqual(self.json_dict, voice)


if __name__ == '__main__':
    unittest.main()
