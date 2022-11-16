# Lazada-Web-Scraping-Handphone-Price-List
- Web scraping via API request using Scrapy web scraping framework
- Extracting mobile phones price and details from Lazada Malaysia
- Scraping framework : Scrapy
- Scraping through API, extracting data from JSON
- This is only meant for educational, research and proof of work purpose only. I will not responsible for any illegal activities.

## Requirement : 
- Scrapy 2.7.1
- Python 3.7 or above
- Any working environment to install the required packages such as conda or pyenv and run the script.

## Run
- The working directory is lazada_phone_listing/lazada_phone_listing/spiders
- Activate the installed working environment
- run <scrapy runspider main.py> in the terminal
- add --O lazada_list.csv in cli to produce the csv file e.g. 'scrapy runspider main.py --O lazada_list.csv'

## Troubleshoot
- Error [mod] due to the cookies already expired
- Any error occur highly due to link or cookies expired
- Solution: 1. Refresh the cookies OR
            2. Using proxy (refer main.py)
