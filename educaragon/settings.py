# -*- coding: utf-8 -*-

# Scrapy settings for educaragon project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'educaragon'

SPIDER_MODULES = ['educaragon.spiders']
NEWSPIDER_MODULE = 'educaragon.spiders'
DOWNLOAD_DELAY = 0.25


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'educaragon (+http://www.yourdomain.com)'
