#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Scovetta'
SITENAME = u'Negative Foo'
SITEURL = ''

TIMEZONE = 'America/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATH = "plugins"
PLUGINS = ['html_rst_directive']

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/scovetta'),
          ('LinkedIn', 'http://linkedin.com/in/scovetta'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/Users/scovetta/Projects/negativefoo/pelican-bootstrap3/'
TYPOGRIFY = True

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

DISQUS_SITENAME = 'negativefoo'
GITHUB_URL = 'http://github.com/scovetta'
TWITTER_USERNAME = 'scovetta'

# tags
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 20

SUMMARY_MAX_LENGTH = None
