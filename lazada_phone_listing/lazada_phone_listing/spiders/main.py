import scrapy
from scrapy import Request
import json

# Using proxy if unsuccessful and errors
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
from scrapy.utils.log import configure_logging
logging.getLogger('__main__').setLevel(logging.DEBUG)
configure_logging(install_root_handler = False) 
logging.basicConfig(
    filename="logfile.txt", 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filemode='w',
    level = logging.ERROR,
)

class MainSpider(scrapy.Spider):
    name = 'main'
    # allowed_domains = ['x']
    # start_urls = ['http://x/']
    # logging.getLogger().setLevel(logging.DEBUG)

    url = 'https://www.lazada.com.my/shop-mobiles/?ajax=true&isFirstRequest=true&page=1&spm=a2o4k.SearchListCategory.cate_2_1.1.632a2had2hadvE'

    headers = {
        "authority": "www.lazada.com.my",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "referer": "https://www.lazada.com.my/shop-mobiles/?page=1&spm=a2o4k.SearchListCategory.cate_2_1.1.632a2had2hadvE",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "x-csrf-token": "7f37648134eea",
        "x-requested-with": "XMLHttpRequest"
    }

    cookies = {
        "__wpkreporterwid_": "a96fbf16-a74e-4fed-a109-429f8029a231",
        "hng": "MY|en-MY|MYR|458",
        "hng.sig": "3PRPmcBmKLS4UwrxxIzxYKE2BjFcClNbRbYGSaUai_0",
        "lzd_cid": "dca32a84-0fb1-4d75-9b2f-d4253e500ed4",
        "t_uid": "dca32a84-0fb1-4d75-9b2f-d4253e500ed4",
        "lzd_sid": "18ceb197160db5065c2cbb1752e58126",
        "_tb_token_": "7f37648134eea",
        "_bl_uid": "hmljt9vpwXd5C6mhb04emO2hvmme",
        "t_fv": "1667182830196",
        "age_limit": "18Y",
        "t_sid": "uXzf5ga3aGc1SCMeaMDaQwuP0KaoVfYK",
        "utm_channel": "NA",
        "_m_h5_tk": "60caf12de55dd41acad4d04a7b6c7382_1668599271096",
        "_m_h5_tk_enc": "10b804667916d5e088fe7f0a95d30fc1",
        "x5sec": "7b22617365727665722d6c617a6164613b32223a223935616261623032316136663435636131393437353165363730356230303864434e625330707347454e4b6d793779456f4d614d417a43633463657941304143227d",
        "l": "eBa4qxxHLhCnq3mUBOfwourza77OSIRAguPzaNbMiOCPOBfp5gscW6zJKWY9C3GNh6vJR3PB699XBeYBYI2pH8i7DSSRMsHmn",
        "isg": "BHR0op6Sq9Mhoz68PpgU-xDdRTvmTZg36vRWxQ7VAP-CeRTDNl1oxyo_-bmhgdCP"
    }

    def start_requests(self):
        # Comment below if using proxy
        for i in range(1,103):
            request = Request(
            url=self.url.format(i),
            method='GET',
            dont_filter=True,
            headers=self.headers,
            cookies=self.cookies
            # callback=self.parse
            )
            yield request
        # Uncomment below if using proxy
        # for i in range(1,103):
        #     yield scrapy.Request(client.scrapyGet(url=self.url.format(i), headers=self.headers), dont_filter=True)

    def parse(self, response):
        # Load json
        raw_data = response.body
        data = json.loads(raw_data)['mods']['listItems']
        # data_phone = []
        # data_phone = data['mods']['listItems']
        # data = data_phone
        print('\n\n Has {} DATA\n\n'.format(len(data)))
        for count,phone in enumerate(data):                    
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