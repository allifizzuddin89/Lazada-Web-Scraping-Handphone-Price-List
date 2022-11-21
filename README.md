# Lazada-Web-Scraping-Handphone-Price-List
- Web scraping via API request using Scrapy web scraping framework
- Extracting mobile phones price and details from Lazada Malaysia
- Scraping framework : Scrapy
- Scraping through API, extracting data from JSON

## Requirement : 
- Scrapy 2.7.1
- Python 3.7 or above
- Any working environment to install the required packages such as conda or pyenv.

## Run
- The working directory is Lazada-Web-Scraping-Handphone-Price-List/lazada_phone_listing/lazada_phone_listing/spiders
- Activate the installed working environment
- Run the main.py in the working directory.
- Run <scrapy runspider main.py> in the terminal in the working directory
  OR simply run <scrapy crawl main.py>
- Add --O lazada_mobilephone_list.csv in cli to produce the csv file e.g. 'scrapy runspider main.py --O lazada_mobilephone_list.csv'

### Install environment
- refer [CONDA Environment Installation](https://docs.anaconda.com/anaconda/install/)
 
### Example How To Run The Script
"""bash
  git clone https://github.com/allifizzuddin89/Lazada-Web-Scraping-Handphone-Price-List.git
"""
 - conda create --name scraping_env -c conda-forge python=3.10.8 scrapy=2.7.1
 - conda activate scraping_env
 - scrapy runspider Lazada-Web-Scraping-Handphone-Price-List.lazada_phone_listing.lazada_phone_listing.spiders.main.py --O lazada_mobilephone_list.csv

## Troubleshoot
- Error might happened due to the cookies already expired or request being rejected by the server.
- Solution: 1. Refresh the cookies OR
            2. Using proxy (refer main.py)
  
## DISCLAIMER
- This work only meant for educational, research and proof of work purpose only. 
- I will not responsible for any illegal activities.
- Every action is on your own responsibilities.
