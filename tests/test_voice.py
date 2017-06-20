#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2017
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
"""This module contains an object that represents Tests for Telegram Voice"""

import os
import sys
import unittest

from flaky import flaky

import telegram
from tests.base import BaseTest, timeout
from tests.bots import get_bot


class VoiceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Telegram Voice."""

    @classmethod
    def setUpClass(cls):
        bot_info = get_bot()
        cls._chat_id = bot_info['chat_id']
        cls._bot = telegram.Bot(bot_info['token'])
        voice_file = open('tests/data/telegram.ogg', 'rb')
        voice = cls._bot.send_voice(cls._chat_id, voice=voice_file).voice
        cls.voice_file_id = voice.file_id
        cls.duration = voice.duration
        cls.mime_type = voice.mime_type
        cls.file_size = voice.file_size


    def setUp(self):
        self.voice_file = open('tests/data/telegram.ogg', 'rb')
        self.voice_file_url = 'https://raw.githubusercontent.com/python-telegram-bot/python-telegram-bot/master/tests/data/telegram.ogg'
        self.caption = "Test voice"
        self.json_dict = {
            'file_id': self.voice_file_id,
            'duration': self.duration,
            'caption': self.caption,
            'mime_type': self.mime_type,
            'file_size': self.file_size
        }

    @flaky(3, 1)
    @timeout(10)
    def test_send_voice_required_args_only(self):
        # Obsolete, tested in setUpClass
        self.assertEqual(True, True)

    @flaky(3, 1)
    @timeout(10)
    def test_send_voice_all_args(self):
        message = self._bot.sendVoice(
            self._chat_id,
            self.voice_file,
            duration=self.duration,
            caption=self.caption,
            mime_type=self.mime_type,
            file_size=self.file_size,
            disable_notification=False)

        self.assertEqual(message.caption, self.caption)

        voice = message.voice

        self.assertTrue(isinstance(voice.file_id, str))
        self.assertNotEqual(voice.file_id, '')
        self.assertEqual(voice.duration, self.duration)
        self.assertEqual(voice.mime_type, self.mime_type)
        self.assertEqual(voice.file_size, self.file_size)

    @flaky(3, 1)
    @timeout(10)
    def test_send_voice_ogg_file(self):
        # obsolete: Same as all_args
        self.assertEqual(True, True)

    @flaky(3, 1)
    @timeout(10)
    def test_send_voice_ogg_file_with_custom_filename(self):
        message = self._bot.sendVoice(
            chat_id=self._chat_id,
            voice=self.voice_file,
            duration=self.duration,
            caption=self.caption,
            filename='telegram_custom.ogg')

        self.assertEqual(message.caption, self.caption)

        voice = message.voice

        self.assertTrue(isinstance(voice.file_id, str))
        self.assertNotEqual(voice.file_id, '')
        self.assertEqual(voice.duration, self.duration)
        self.assertEqual(voice.mime_type, self.mime_type)
        self.assertEqual(voice.file_size, self.file_size)

    @flaky(3, 1)
    @timeout(10)
    def test_send_voice_ogg_url_file(self):
        message = self._bot.sendVoice(
            chat_id=self._chat_id, voice=self.voice_file_url, duration=self.duration)

        voice = message.voice

        self.assertTrue(isinstance(voice.file_id, str))
        self.assertNotEqual(voice.file_id, '')
        self.assertEqual(voice.duration, self.duration)
        self.assertEqual(voice.mime_type, self.mime_type)
        self.assertEqual(voice.file_size, self.file_size)

    @flaky(3, 1)
    @timeout(10)
    def test_send_voice_ogg_url_file_with_caption(self):
        message = self._bot.sendVoice(
            chat_id=self._chat_id,
            voice=self.voice_file_url,
            duration=self.duration,
            caption=self.caption)

        self.assertEqual(message.caption, self.caption)

        voice = message.voice

        self.assertTrue(isinstance(voice.file_id, str))
        self.assertNotEqual(voice.file_id, '')
        self.assertEqual(voice.duration, self.duration)
        self.assertEqual(voice.mime_type, self.mime_type)
        self.assertEqual(voice.file_size, self.file_size)

    @flaky(3, 1)
    @timeout(10)
    def test_send_voice_resend(self):
        message = self._bot.sendVoice(
            chat_id=self._chat_id,
            voice=self.voice_file_id)

        voice = message.voice

        self.assertEqual(voice.file_id, self.voice_file_id)
        self.assertEqual(voice.duration, self.duration)
        self.assertEqual(voice.mime_type, self.mime_type)

    def test_voice_de_json(self):
        voice = telegram.Voice.de_json(self.json_dict, self._bot)

        self.assertEqual(voice.file_id, self.voice_file_id)
        self.assertEqual(voice.duration, self.duration)
        self.assertEqual(voice.mime_type, self.mime_type)
        self.assertEqual(voice.file_size, self.file_size)

    def test_voice_to_json(self):
        voice = telegram.Voice.de_json(self.json_dict, self._bot)

        self.assertTrue(self.is_json(voice.to_json()))

    def test_voice_to_dict(self):
        voice = telegram.Voice.de_json(self.json_dict, self._bot)

        self.assertTrue(self.is_dict(voice.to_dict()))
        self.assertEqual(voice['file_id'], self.voice_file_id)
        self.assertEqual(voice['duration'], self.duration)
        self.assertEqual(voice['mime_type'], self.mime_type)
        self.assertEqual(voice['file_size'], self.file_size)

    @flaky(3, 1)
    @timeout(10)
    def test_error_send_voice_empty_file(self):
        json_dict = self.json_dict

        del (json_dict['file_id'])
        json_dict['voice'] = open(os.devnull, 'rb')

        with self.assertRaises(telegram.TelegramError):
            self._bot.sendVoice(chat_id=self._chat_id, **json_dict)

    @flaky(3, 1)
    @timeout(10)
    def test_error_send_voice_empty_file_id(self):
        json_dict = self.json_dict

        del (json_dict['file_id'])
        json_dict['voice'] = ''

        with self.assertRaises(telegram.TelegramError):
            self._bot.sendVoice(chat_id=self._chat_id, **json_dict)

    @flaky(3, 1)
    @timeout(10)
    def test_error_voice_without_required_args(self):
        json_dict = self.json_dict

        del (json_dict['file_id'])

        with self.assertRaises(TypeError):
            self._bot.sendVoice(chat_id=self._chat_id, **json_dict)

    @flaky(3, 1)
    @timeout(10)
    def test_reply_voice(self):
        """Test for Message.reply_voice"""
        message = self._bot.sendMessage(self._chat_id, '.')
        message = message.reply_voice(self.voice_file)

        self.assertNotEqual(message.voice.file_id, '')

    def test_equality(self):
        a = telegram.Voice(self.voice_file_id, self.duration)
        b = telegram.Voice(self.voice_file_id, self.duration)
        c = telegram.Voice(self.voice_file_id, 0)
        d = telegram.Voice("", self.duration)
        e = telegram.Audio(self.voice_file_id, self.duration)

        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertIsNot(a, b)

        self.assertEqual(a, c)
        self.assertEqual(hash(a), hash(c))

        self.assertNotEqual(a, d)
        self.assertNotEqual(hash(a), hash(d))

        self.assertNotEqual(a, e)
        self.assertNotEqual(hash(a), hash(e))


if __name__ == '__main__':
    unittest.main()
