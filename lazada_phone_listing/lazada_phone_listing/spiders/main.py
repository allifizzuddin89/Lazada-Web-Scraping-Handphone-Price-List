import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json

# Using proxy if unsuccessful
# Register here at https://www.scraperapi.com/?fp_ref=allif-izzuddin-bin-abdullah73
# You might want to choose free account
# Scraperapi proxy API key details will be provided after the registration
# Follow the instruction in the scraperapi website to setup the proxy
# Paste the API key inside creds.py module

# Uncomment below if using proxy
# from creds import API
# from scraper_api import ScraperAPIClient
# client = ScraperAPIClient(API)

# Logging
import logging
logging.basicConfig(
    filename="logfile.txt", 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filemode='w',
    level = logging.DEBUG,
)

class MainSpider(scrapy.Spider):
    name = 'main'
    # allowed_domains = ['x']
    # start_urls = ['http://x/']

    headers = {
        "authority": "www.lazada.com.my",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "referer": "https://www.lazada.com.my/shop-mobiles/?spm=a2o4k.home.cate_2_1.1.75f8191bjdZqQG",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "x-csrf-token": "e557530334835",
        "x-requested-with": "XMLHttpRequest"
    }

    # Cookies are dynamic
    # Feel free to update for every scraping session
    cookies = {
        "__wpkreporterwid_": "8987d50d-7410-4452-0d4a-838a55cbf24b",
        "lzd_cid": "2b3f81a9-b3ac-4511-d563-88dc718bd43e",
        "t_uid": "2b3f81a9-b3ac-4511-d563-88dc718bd43e",
        "hng": "MY|en-MY|MYR|458",
        "userLanguageML": "en",
        "_m_h5_tk": "2ab15fa1ff4dd42259c8217ac2ad2449_1668508613562",
        "_m_h5_tk_enc": "65c3d44ac8a9784847f3c6c28596a59f",
        "_bl_uid": "Ujlg8aUzheqy1488ke9tys9ukwIX",
        "lzd_sid": "1b4b47eeee23df99f7504fd28cec55f7",
        "_tb_token_": "e557530334835",
        "t_fv": "1668500695130",
        "t_sid": "PgAFQBrejpUc1sEjEKcrkX8qen6g3t9j",
        "utm_channel": "NA",
        "l": "eBIVRAqnT1tJPFO6BOfwourza77OSIRAguPzaNbMiOCPOL5p5andW6zmR9T9C3GNh6vJR3PB699XBeYBYI2pH8i7DSSRMsHmn",
        "isg": "BAUFcQoByvc9Nu6rO_-Q8HJXFEg_wrlUM_PnFgdqwTxLniUQzxLJJJN4qMpo3tEM"
    }

    url = 'https://www.lazada.com.my/shop-mobiles/?ajax=true&isFirstRequest=true&page={}&spm=a2o4k.home.cate_2_1.1.75f8191bjdZqQG'

    def start_requests(self):
        # Comment below if using proxy
        for i in range(1,103):
            request = Request(
            url=self.url.format(i),
            method='GET',
            dont_filter=True,
            cookies=self.cookies,
            headers=self.headers,
            # callback=self.parse
            )
            yield request
        # Uncomment below if using proxy
        # for i in range(1,103):
        #     yield scrapy.Request(client.scrapyGet(url=self.url.format(i), headers=self.headers), dont_filter=True, callback=self.parse_api)

    def parse(self, response):
        # Load json 
        raw_data = response.text
        data = json.loads(raw_data)['mods']['listItems']
        print('\n\n Has {} DATA\n\n'.format(len(data)))
        for count, phone in enumerate(data):                    
            try:
                item = {
                    'name': data[count]['name'],
                    'brand': data[count]['brandName'],
                    'price (RM)': data[count]['price'],
                    'link': data[count]['itemUrl'],
                    'shop_rating': data[count]['ratingScore'],
                }
                yield item
            except:
                item = {
                    'name': data[count]['name'],
                    'brand': data[count]['brandName'],
                    'price (RM)': 'sold out',
                    'link': data[count]['itemUrl'],
                    'shop_rating': data[count]['ratingScore'],
                }
                yield item

process = CrawlerProcess(settings={
    "FEEDS": {
        'Lazada_phone_list.csv': {"format": "csv"},
    },
})

process.crawl(MainSpider)
process.start()