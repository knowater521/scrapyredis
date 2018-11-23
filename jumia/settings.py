# -*- coding: utf-8 -*-

# Scrapy settings for jumia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jumia'

SPIDER_MODULES = ['jumia.spiders']
NEWSPIDER_MODULE = 'jumia.spiders'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#redis配置

REDIS_URL = 'redis://:yang5224910@96.45.191.65:6379'
#REDIS_URL = 'redis://:yang5224910@127.0.0.1:6379'
#ITEM_PIPELINES = {
#    'scrapy_redis.pipelines.RedisPipeline': 300
#}

ITEM_PIPELINES = {
#    'jumia.pipelines.JumiaPipeline': 600,
    'jumia.pipelines.MysqlTwistedPipline': 500,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jumia (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
SCHEDULER_FLUSH_ON_START = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
MYSQL_HOST = '96.45.191.65'
MYSQL_DBNAME = 'louis'     # 数据库名
MYSQL_USER = 'root'         # 数据库用户
MYSQL_PASSWORD = '#Yang5224910$%'   # 数据库密码
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jumia.middlewares.JumiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'jumia.middlewares.JumiaDownloaderMiddleware': 543,
}

if IF_USE_PROXY:
    DOWNLOADER_MIDDLEWARES = {

        # 第二行的填写规则
        #  yourproject.myMiddlewares(文件名).middleware类

        # 设置 User-Agent
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'proxyPool.scrapy.RandomUserAgentMiddleware.RandomUserAgentMiddleware': 400,

        # 设置代理
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
        'proxyPool.scrapy.middlewares.ProxyMiddleware': 100,

        # 设置自定义捕获异常中间层
        'proxyPool.scrapy.middlewares.CatchExceptionMiddleware': 105,

        # 设置自定义重连中间件
        'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': None,
        'proxyPool.scrapy.middlewares.RetryMiddleware': 95,
    }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
DEPTH_LIMIT = 0
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jumia.pipelines.JumiaPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 50
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
