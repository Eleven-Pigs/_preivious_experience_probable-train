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
InlineQueryResultVideo"""

import sys

if sys.version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest

sys.path.append('.')

import telegram
from tests.base import BaseTest


class InlineQueryResultVideoTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Telegram InlineQueryResultVideo."""

    def setUp(self):
        self.id = 'id'
        self.type = 'video'
        self.video_url = 'video url'
        self.mime_type = 'mime type'
        self.video_width = 10
        self.video_height = 15
        self.video_duration = 15
        self.thumb_url = 'thumb url'
        self.title = 'title'
        self.caption = 'caption'
        self.description = 'description'

        self.json_dict = {
            'type': self.type,
            'id': self.id,
            'video_url': self.video_url,
            'mime_type': self.mime_type,
            'video_width': self.video_width,
            'video_height': self.video_height,
            'video_duration': self.video_duration,
            'thumb_url': self.thumb_url,
            'title': self.title,
            'caption': self.caption,
            'description': self.description,
        }

    def test_video_de_json(self):
        video = telegram.InlineQueryResultVideo.de_json(self.json_dict)

        self.assertEqual(video.type, self.type)
        self.assertEqual(video.id, self.id)
        self.assertEqual(video.video_url, self.video_url)
        self.assertEqual(video.mime_type, self.mime_type)
        self.assertEqual(video.video_width, self.video_width)
        self.assertEqual(video.video_height, self.video_height)
        self.assertEqual(video.video_duration, self.video_duration)
        self.assertEqual(video.thumb_url, self.thumb_url)
        self.assertEqual(video.title, self.title)
        self.assertEqual(video.description, self.description)
        self.assertEqual(video.caption, self.caption)

    def test_video_to_json(self):
        video = telegram.InlineQueryResultVideo.de_json(self.json_dict)

        self.assertTrue(self.is_json(video.to_json()))

    def test_video_to_dict(self):
        video = \
            telegram.InlineQueryResultVideo.de_json(self.json_dict).to_dict()

        self.assertTrue(self.is_dict(video))
        self.assertDictEqual(self.json_dict, video)


if __name__ == '__main__':
    unittest.main()
