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
InlineQueryResultMpeg4Gif"""

import sys
import unittest

sys.path.append('.')

import telegram
from tests.base import BaseTest


class InlineQueryResultMpeg4GifTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Telegram InlineQueryResultMpeg4Gif."""

    def setUp(self):
        self.id = 'id'
        self.type = 'mpeg4_gif'
        self.mpeg4_url = 'mpeg4 url'
        self.mpeg4_width = 10
        self.mpeg4_height = 15
        self.thumb_url = 'thumb url'
        self.title = 'title'
        self.caption = 'caption'
        self.input_message_content = telegram.InputTextMessageContent('input_message_content')
        self.reply_markup = telegram.InlineKeyboardMarkup([[
            telegram.InlineKeyboardButton('reply_markup')
        ]])

        self.json_dict = {
            'type': self.type,
            'id': self.id,
            'mpeg4_url': self.mpeg4_url,
            'mpeg4_width': self.mpeg4_width,
            'mpeg4_height': self.mpeg4_height,
            'thumb_url': self.thumb_url,
            'title': self.title,
            'caption': self.caption,
            'input_message_content': self.input_message_content.to_dict(),
            'reply_markup': self.reply_markup.to_dict(),
        }

    def test_mpeg4_de_json(self):
        mpeg4 = telegram.InlineQueryResultMpeg4Gif.de_json(self.json_dict)

        self.assertEqual(mpeg4.type, self.type)
        self.assertEqual(mpeg4.id, self.id)
        self.assertEqual(mpeg4.mpeg4_url, self.mpeg4_url)
        self.assertEqual(mpeg4.mpeg4_width, self.mpeg4_width)
        self.assertEqual(mpeg4.mpeg4_height, self.mpeg4_height)
        self.assertEqual(mpeg4.thumb_url, self.thumb_url)
        self.assertEqual(mpeg4.title, self.title)
        self.assertEqual(mpeg4.caption, self.caption)
        self.assertDictEqual(mpeg4.input_message_content.to_dict(),
                             self.input_message_content.to_dict())
        self.assertDictEqual(mpeg4.reply_markup.to_dict(), self.reply_markup.to_dict())

    def test_mpeg4_to_json(self):
        mpeg4 = telegram.InlineQueryResultMpeg4Gif.de_json(self.json_dict)

        self.assertTrue(self.is_json(mpeg4.to_json()))

    def test_mpeg4_to_dict(self):
        mpeg4 = telegram.InlineQueryResultMpeg4Gif.de_json(self.json_dict).to_dict()

        self.assertTrue(self.is_dict(mpeg4))
        self.assertDictEqual(self.json_dict, mpeg4)


if __name__ == '__main__':
    unittest.main()
