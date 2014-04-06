###########
DeputyScraper
###########

diputados.gob.mx scraper



After having these requirements, run with the following command line: 

...


Getting started
===============

In order to run this scraper, you should first need to satisfy following requirements:
------------------------------

- Python 2.7 or greater
- Scrapy 0.22 or greater
- MongoDB 2.02 or greater
- PyMongo 2.2 or greater

- Then run::

    scrapy crawl deputies
    
This will scrap `<diputados.gob.mx>` site :) and store basic info for each diputy in a MongoDB collection
