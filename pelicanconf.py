#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'cnDenis'
SITENAME = u'cnDenis的笔记'
SITEURL = 'http://localhost:8000'

PATH = '_posts'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y年%m月%d日 星期%a'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# GITHUB_URL = 'https://github.com/cnDenis/cndenis.github.io'
MENUITEMS = [

]

# Blogroll
LINKS = (
    ('Erlang官网', 'http://www.erlang.org/'),
    ('Pelican官网', 'http://getpelican.com/')
)

# Social widget
# SOCIAL = (('GitHub: cndenis', 'https://github.com/cnDenis'),
#             ('Twitter: cndenis', 'https://twitter.com/cndenis'),)

DEFAULT_PAGINATION = 6

DISPLAY_CATEGORIES_ON_MENU = False

CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = '{slug}/index.html'

ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{slug}.html'  # 文章生成位置
ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{slug}.html'  # 文章生成位置
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'  # 按年显示文章列表
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'  # 按月份显示文章列表

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

STATIC_PATHS = [
  	'images',
  	'extra'
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    # 'extra/custom.js': {'path': 'static/js/custom.js'}
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = os.path.join(os.environ.get('HOME'), 'gits/pelican-themes/pelican-bootstrap3')
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = [os.path.join(os.environ.get('HOME'), 'gits/pelican-plugins')]
PLUGINS = [
	'i18n_subsites',
	'tag_cloud',
	'tipue_search'
]

# 以下是pelican-bootstrap3的设置

DIRECT_TEMPLATES = (
   'index',
   'categories',
   # 'authors',
   'archives',
   'search'
)  # 直接由模板生成的页面, 前四个是默认值

CUSTOM_CSS = 'static/custom.css'

PYGMENTS_STYLE = 'monokai'

DISPLAY_TAGS_ON_SIDEBAR = True  # 在侧边栏显示Tags, 仅启用tag_cloud时有效
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True  # 在侧边栏显示栏目
DISPLAY_ARCHIVE_ON_SIDEBAR = True  # 在侧边栏显示月份文章, 仅在MONTH_ARCHIVE_SAVE_AS正确时生效

ABOUT_ME = '<a href="/pages/about.html"><img class="center" src="http://gravatar.com/avatar/8373fc5c4d82aeba56db52f7317ab48d?s=160"></a>'
# AVATAR = "http://gravatar.com/avatar/8373fc5c4d82aeba56db52f7317ab48d?s=160" # 只能用相对路径, 可能是Bug

SHOW_DATE_MODIFIED = True  # 显示文章修改时间
SHOW_ARTICLE_CATEGORY = True  # 显示文章分类
SHOW_ARTICLE_AUTHOR = False  # 显示文章作者

CC_LICENSE = "CC-BY-NC-SA"  # CC协议
