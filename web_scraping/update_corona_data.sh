#!/usr/bin/env bash

cd /home/shadhini/dev/repos/shadhini/python_helpers/web_scraping
echo "Inside `pwd`"
source venv/bin/activate
cd corona_data
scrapy crawl ifs
