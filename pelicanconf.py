#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrii Soldatenko'
SITENAME = u'Python Geek blog'
SITEDESCRIPTION = u'(Graphs)-[:ARE]->(Everywhere)'
SITEURL = 'https://asoldatenko.com/'
ARTICLE_PATHS = ['blog']
PATH = 'content'
GITHUB_URL = 'http://github.com/andriisoldatenko/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True
# Blogroll
LINKS = (("Home", SITEURL),)

# Social widget
SOCIAL = (('@a_soldatenko', 'http://twitter.com/a_soldatenko'),
                  ('andriisoldatenko', 'http://github.com/andriisoldatenko'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = 'pelicanyan'
GA_ACCOUNT = "UA-76003429-1"
GOOGLE_ANALYTICS = "UA-76003429-1"
TWITTER_ACCOUNT = 'a_soldatenko'
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'sitemap', 'robots', 'humans')
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'
DEFAULT_LANG = 'en'
DATE_FORMATS = { 'en': '%B %d, %Y', }
STATIC_PATHS = ['static', 'images', 'pdfs', 'favicon.ico']
TYPOGRIFY = True

PLUGIN_PATHS = ['plugins']

PLUGINS = [
    'slideshare',
    'pelican_youtube'
]

DISQUS_SITENAME = 'asoldatenko2'

DISPLAY_CATEGORIES_ON_MENU = True

# Social widget
SOCIAL = (
    ('gitorious', 'https://gitorious.org/~hook'),
    ('github', 'https://github.com/silverhook'),
    ('friendica', 'https://friendica.free-beer.ch/profile/hook'),
)
