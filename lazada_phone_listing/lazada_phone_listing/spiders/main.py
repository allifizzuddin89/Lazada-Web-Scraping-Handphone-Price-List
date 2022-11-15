import scrapy
from scrapy import Request
import json

# Using proxy
# Get here at https://www.scraperapi.com/?fp_ref=allif-izzuddin-bin-abdullah73
# You might want to choose free account
# Scraperapi proxy API key details will be provided after the registration
# Follow the instruction in the scraperapi website to setup the proxy
from creds import API
from scraper_api import ScraperAPIClient
client = ScraperAPIClient(API)

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
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
