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
InlineResults"""

import os
import unittest
import sys
sys.path.append('.')

import telegram
from tests.base import BaseTest


class InlineQueryResultArticleTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Telegram InlineQueryResultArticle."""

    def setUp(self):
        self.id = 'id'
        self.title = 'title'
        self.message_text = 'message text'
        self.parse_mode = 'HTML'
        self.disable_web_page_preview = True
        self.url = 'url'
        self.hide_url = True
        self.description = 'description'
        self.thumb_url = 'thumb url'
        self.thumb_height = 10
        self.thumb_width = 15

        self.json_dict = {
            'type': 'article',
            'id': self.id,
            'title': self.title,
            'message_text': self.message_text,
            'parse_mode': self.parse_mode,
            'disable_web_page_preview': self.disable_web_page_preview,
            'url': self.url,
            'hide_url': self.hide_url,
            'description': self.description,
            'thumb_url': self.thumb_url,
            'thumb_height': self.thumb_height,
            'thumb_width': self.thumb_width
        }

    def test_article_de_json(self):
        """Test InlineQueryResultArticle.de_json() method"""
        print('Testing InlineQueryResultArticle.de_json()')

        article = telegram.InlineQueryResultArticle.de_json(self.json_dict)

        self.assertEqual(article.type, 'article')
        self.assertEqual(article.id, self.id)
        self.assertEqual(article.title, self.title)
        self.assertEqual(article.message_text, self.message_text)
        self.assertEqual(article.parse_mode, self.parse_mode)
        self.assertEqual(article.disable_web_page_preview,
                         self.disable_web_page_preview)
        self.assertEqual(article.url, self.url)
        self.assertEqual(article.hide_url, self.hide_url)
        self.assertEqual(article.description, self.description)
        self.assertEqual(article.thumb_url, self.thumb_url)
        self.assertEqual(article.thumb_height, self.thumb_height)
        self.assertEqual(article.thumb_width, self.thumb_width)

    def test_article_to_json(self):
        """Test InlineQueryResultArticle.to_json() method"""
        print('Testing InlineQueryResultArticle.to_json()')

        article = telegram.InlineQueryResultArticle.de_json(self.json_dict)

        self.assertTrue(self.is_json(article.to_json()))

    def test_article_to_dict(self):
        """Test InlineQueryResultArticle.to_dict() method"""
        print('Testing InlineQueryResultArticle.to_dict()')

        article = telegram.InlineQueryResultArticle.de_json(self.json_dict)

        self.assertTrue(self.is_dict(article.to_dict()))
        self.assertEqual(article['type'], 'article')
        self.assertEqual(article['id'], self.id)
        self.assertEqual(article['title'], self.title)
        self.assertEqual(article['message_text'], self.message_text)
        self.assertEqual(article['parse_mode'], self.parse_mode)
        self.assertEqual(article['disable_web_page_preview'],
                         self.disable_web_page_preview)
        self.assertEqual(article['url'], self.url)
        self.assertEqual(article['hide_url'], self.hide_url)
        self.assertEqual(article['description'], self.description)
        self.assertEqual(article['thumb_url'], self.thumb_url)
        self.assertEqual(article['thumb_height'], self.thumb_height)
        self.assertEqual(article['thumb_width'], self.thumb_width)


class InlineQueryResultPhotoTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Telegram InlineQueryResultPhoto."""

    def setUp(self):
        self.id = 'id'
        self.photo_url = 'photo url'
        self.mime_type = 'mime type'
        self.photo_width = 10
        self.photo_height = 15
        self.thumb_url = 'thumb url'
        self.title = 'title'
        self.caption = 'caption'
        self.message_text = 'message text'
        self.parse_mode = 'parse mode'
        self.disable_web_page_preview = True

        self.json_dict = {
            'type': 'photo',
            'id': self.id,
            'photo_url': self.photo_url,
            'mime_type': self.mime_type,
            'photo_width': self.photo_width,
            'photo_height': self.photo_height,
            'thumb_url': self.thumb_url,
            'title': self.title,
            'caption': self.caption,
            'message_text': self.message_text,
            'parse_mode': self.parse_mode,
            'disable_web_page_preview': self.disable_web_page_preview
        }

    def test_photo_de_json(self):
        """Test InlineQueryResultPhoto.de_json() method"""
        print('Testing InlineQueryResultPhoto.de_json()')

        photo = telegram.InlineQueryResultPhoto.de_json(self.json_dict)

        self.assertEqual(photo.type, 'photo')
        self.assertEqual(photo.id, self.id)
        self.assertEqual(photo.photo_url, self.photo_url)
        self.assertEqual(photo.mime_type, self.mime_type)
        self.assertEqual(photo.photo_width, self.photo_width)
        self.assertEqual(photo.photo_height,
                         self.photo_height)
        self.assertEqual(photo.thumb_url, self.thumb_url)
        self.assertEqual(photo.title, self.title)
        self.assertEqual(photo.caption, self.caption)
        self.assertEqual(photo.message_text, self.message_text)
        self.assertEqual(photo.parse_mode, self.parse_mode)
        self.assertEqual(photo.disable_web_page_preview,
                         self.disable_web_page_preview)

    def test_photo_to_json(self):
        """Test InlineQueryResultPhoto.to_json() method"""
        print('Testing InlineQueryResultPhoto.to_json()')

        photo = telegram.InlineQueryResultPhoto.de_json(self.json_dict)

        self.assertTrue(self.is_json(photo.to_json()))

    def test_photo_to_dict(self):
        """Test InlineQueryResultPhoto.to_dict() method"""
        print('Testing InlineQueryResultPhoto.to_dict()')

        photo = telegram.InlineQueryResultPhoto.de_json(self.json_dict)

        self.assertTrue(self.is_dict(photo.to_dict()))
        self.assertEqual(photo['type'], 'photo')
        self.assertEqual(photo['id'], self.id)
        self.assertEqual(photo['photo_url'], self.photo_url)
        self.assertEqual(photo['mime_type'], self.mime_type)
        self.assertEqual(photo['photo_width'], self.photo_width)
        self.assertEqual(photo['photo_height'],
                         self.photo_height)
        self.assertEqual(photo['thumb_url'], self.thumb_url)
        self.assertEqual(photo['title'], self.title)
        self.assertEqual(photo['caption'], self.caption)
        self.assertEqual(photo['message_text'], self.message_text)
        self.assertEqual(photo['parse_mode'], self.parse_mode)
        self.assertEqual(photo['disable_web_page_preview'],
                         self.disable_web_page_preview)


if __name__ == '__main__':
    unittest.main()
