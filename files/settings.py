# -*- coding: utf-8 -*-

    # Scrapy settings for GetCaiWuInfo project
    #
    # For simplicity, this file contains only settings considered important or
    # commonly used. You can find more settings consulting the documentation:
    #
    #     https://doc.scrapy.org/en/latest/topics/settings.html
    #     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
    #     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
    import os
    import platform
    import uuid
    
    
    BOT_NAME = 'GetCaiWuInfo'
    
    SPIDER_MODULES = ['GetCaiWuInfo.spiders']
    NEWSPIDER_MODULE = 'GetCaiWuInfo.spiders'
    
    # 本文件所在绝对父路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 日志路径
    LOG_DIR = os.path.join(BASE_DIR, '..', 'log')
    # 股票代码json文件路径
    STOCK_CODE_DIR = os.path.join(BASE_DIR, '..', 'temp', 'stock_code.json')
    # 爬虫缓存文件存放路径
    CACHE_FILE_DIR = os.path.join(BASE_DIR, '..', 'cache')
    # 无图形化浏览器存放路径
    if 'Windows' in platform.system():
        DRIVER_PATH = os.path.join(BASE_DIR, '..', 'temp', 'chromedriver.exe')
    elif 'Linux' in platform.system():
        DRIVER_PATH = os.path.join(BASE_DIR, '..', 'temp', 'geckodriver')
    else:
        DRIVER_PATH = ''
    
    # redis 配置
    # 使用scrapy-redis里的去重组件，不使用scrapy默认的去重方式
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
    # 使用scrapy-redis里的调度器组件，不使用默认的调度器
    SCHEDULER = "scrapy_redis.scheduler.Scheduler"
    # 允许暂停，redis请求记录不丢失
    SCHEDULER_PERSIST = True
    # redis采用set集合方式
    REDIS_START_URLS_AS_SET = True
    
    # 版本号
    VERSION = "v1.0"
    
    # 日志配置
    # 是否启用logging, 默认: True
    LOG_ENABLED = False
    # logging使用的编码。默认: 'utf-8'
    LOG_ENCODING = 'utf-8'
    # log的最低级别。可选的级别有: CRITICAL、ERROR、WARNING、INFO、DEBUG。
    LOG_LEVEL = 'INFO'
    # 如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中。例如， 执行 print 'hello' ，其将会在Scrapy log中显示。默认: False
    LOG_STDOUT = True
    
    USER_AGENT_LIST = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FDM) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FTDv3 Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts; .NET CLR 1.1.4322; .NET CLR 2.0.40607) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts; AtHome033) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; HCI0449; .NET CLR 1.0.3705) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; i-NavFourF; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon; ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2; Maxthon; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312461; FunWebProducts; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Woningstichting Den Helder; .NET CLR 1.0.3705) ",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1) ",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 2.0.50727; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322) ",
    ]
    
    PH_USER_AGENT_LIST = [
        "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ZUK Z2121 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Letv X501 Build/DBXCNOP5501304131S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.7 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 baiduboxapp/7.3.1 (Baidu; P1 5.1.1)",
        "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; N5117 Build/JLS36C) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/7.0 (Baidu; P1 4.3)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/13D15 UCBrowser/10.9.15.793 Mobile",
        "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.7 Mobile/13D15 Safari/8536.25 MttCustomUA/2",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13D15 Safari/601.1",
        "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-S7572 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.7 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; SM-J3109 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; Coolpad 8297-T01 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MX4 Pro Build/LMY48W) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.800 U3/0.8.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; Android 5.1; m2 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.114 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m2 note Build/LMY47D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.10.788 U3/0.8.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; m2 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 MxBrowser/4.5.9.3000",
        "Mozilla/5.0 (Linux; Android 4.3; R7007 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 baiduboxapp/7.3.1 (Baidu; P1 4.3)",
    ]
    
    # Crawl responsibly by identifying yourself (and your website) on the user-agent
    #USER_AGENT = 'GetCaiWuInfo (+http://www.yourdomain.com)'
    
    # Obey robots.txt rules
    ROBOTSTXT_OBEY = False
    
    # Configure maximum concurrent requests performed by Scrapy (default: 16)
    #CONCURRENT_REQUESTS = 32
    
    # Configure a delay for requests for the same website (default: 0)
    # See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
    # See also autothrottle settings and docs
    
    # 设置下载延迟
    DOWNLOAD_DELAY = 0.5
    RANDOMIZE_DOWNLOAD_DELAY = True
    
    DOWNLOAD_TIMEOUT = 15
    RETRY_TIMES = 5
    
    # The download delay setting will honor only one of:
    #CONCURRENT_REQUESTS_PER_DOMAIN = 16
    #CONCURRENT_REQUESTS_PER_IP = 16
    CONCURRENT_REQUESTS = 16
    
    # Disable cookies (enabled by default)
    COOKIES_ENABLED = False
    
    # Disable Telnet Console (enabled by default)
    #TELNETCONSOLE_ENABLED = False
    
    # Override the default request headers:
    #DEFAULT_REQUEST_HEADERS = {
    #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #   'Accept-Language': 'en',
    #}
    
    # Enable or disable spider middlewares
    # See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
    #SPIDER_MIDDLEWARES = {
    #    'GetCaiWuInfo.middlewares.GetcaiwuinfoSpiderMiddleware': 543,
    #}
    
    # Enable or disable downloader middlewares
    # See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
    DOWNLOADER_MIDDLEWARES = {
        # 'GetCaiWuInfo.middlewares.GetcaiwuinfoDownloaderMiddleware': 543,
        'GetCaiWuInfo.middlewares.RandomUserAgentMiddelware': 544,
    }
    
    # Enable or disable extensions
    # See https://doc.scrapy.org/en/latest/topics/extensions.html
    #EXTENSIONS = {
    #    'scrapy.extensions.telnet.TelnetConsole': None,
    #}
    
    # Configure item pipelines
    # See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
    ITEM_PIPELINES = {
        # 'GetCaiWuInfo.pipelines.GetcaiwuinfoPipeline': 300,
        'GetCaiWuInfo.pipelines.GetUrlPipeline': 1,
        'GetCaiWuInfo.pipelines.ErrorReminderPipeline': 500,
        'GetCaiWuInfo.pipelines.MysqlDBPipeline': 300,
    }
    
    # Enable and configure the AutoThrottle extension (disabled by default)
    # See https://doc.scrapy.org/en/latest/topics/autothrottle.html
    AUTOTHROTTLE_ENABLED = True
    # The initial download delay
    AUTOTHROTTLE_START_DELAY = 0.25
    # The maximum download delay to be set in case of high latencies
    AUTOTHROTTLE_MAX_DELAY = 5
    # The average number of requests Scrapy should be sending in parallel to
    # each remote server
    AUTOTHROTTLE_TARGET_CONCURRENCY = 0.5
    # Enable showing throttling stats for every response received:
    AUTOTHROTTLE_DEBUG = False
    
    # Enable and configure HTTP caching (disabled by default)
    # See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
    #HTTPCACHE_ENABLED = True
    #HTTPCACHE_EXPIRATION_SECS = 0
    #HTTPCACHE_DIR = 'httpcache'
    #HTTPCACHE_IGNORE_HTTP_CODES = []
    #HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
    
    MYEXT_ENABLED = True   # 是否启用扩展，启用扩展为 True， 不启用为 False
    IDLE_NUMBER = 12  # 关闭爬虫的持续空闲次数，持续空闲次数超过IDLE_NUMBER，爬虫会被关闭。默认为 360 ，也就是30分钟，一分钟12个时间单位
    
    # 在 EXTENSIONS 配置，激活扩展
    EXTENSIONS = {
        'GetCaiWuInfo.extensions.RedisSpiderSmartIdleClosedExensions': 500,
    }
    # 捕获404状态码    默认为空
    HTTPERROR_ALLOWED_CODES = [400, 404, 403]
    
    
    # def get_mac_address():
    #     # mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    #     # return ":".join([mac[e:e+2] for e in range(0,11,2)])
    #     return uuid.UUID(int = uuid.getnode()).hex[-12:]
    #
    # u_id = get_mac_address()
    
    # --------------------预生产-----------------------------
    # 数据库配置
    # 行情mysql数据库
    MYSQL_SERVER = '10.3.4.5'
    MYSQL_DB = 'xuangu'
    MYSQL_USER = 'hq'
    MYSQL_PWD = '1234560.'
    MYSQL_PORT = 3306
    
    # 爬虫mysql数据库
    PMYSQL_SERVER = '10.2.34.5'
    PMYSQL_DB = 'ap'
    PMYSQL_USER = 'root'
    PMYSQL_PWD = 'imLG29gyL5WuyJpXplplp'
    PMYSQL_PORT = 3306
    
    # 爬虫服务redis
    REDIS_SERVER = '10.216.251.84'
    REDIS_PORT = 6379
    REDIS_PWD = '1234560.'
    REDIS_DB = 11
    # 指定使用redis库
    REDIS_PARAMS = {
        'db': REDIS_DB
    }
    REDIS_URL = 'redis://root:1234560.@10.216.251.84:6379'
    
    # 行情redis
    HREDIS_SERVER = ['19.216.251.20@root@T1WrrHTZIlcxR9e7lpPy@6379']
    HREDIS_KEY = 'exchange_rate'
    
    ALERT_URL = 'https://oapi.dingtalk.com/robot/send?' \
                'access_token=06c85d1c64d89b09b1feb506dac20716d0548b549fce5cae04a2cb8311a0090d'
