# Scrape Main Result page - find the pattern of urls
# First Middle Way Checkpoint - print number of products

# Scrape Product Detail Page - find the url of review page
# Second Middle Way Checkpoint - print meta data from response

# Scrape Review Pages

from scrapy import Spider
from yahoofin.items import YahoofinItem
import re
from scrapy import Request

class YahoofinSpider(Spider):
    name = 'yahoofin_spider'
    allowed_urls = ['https://finance.yahoo.com/']
    start_urls = ['https://finance.yahoo.com/sector/ms_technology']

# number of pages:
    def parse(self, response):
        pages = response.xpath('//div[@id="fin-scr-res-table"]/div[1]/div[1]/span[2]/span/text()').extract_first()
        _, per_page, total = re.findall('\d+', pages)
        num_pages = (int(total) - 1)//int(per_page)
        result_page_urls = ['https://finance.yahoo.com/screener/predefined/ms_technology?offset={}&count=100' .format(x) for x in range(0, (num_pages*100)+1, 100)]

        for result_page_url in result_page_urls:
            yield Request(url = result_page_url, callback = self.parse_result_page)

    def parse_result_page(self, response):
        rows = response.xpath('//div[@id="fin-scr-res-table"]//table//tr')[1:]

        for row in rows:
            stock_link = row.xpath('./td[1]/a/@href').extract_first()
            symbol = row.xpath('./td[1]/a/text()').extract_first()
            name = row.xpath('./td[2]/text()').extract_first()
            price = row.xpath('./td[3]/span/text()').extract_first()
            change = row.xpath('./td[4]/span/text()').extract_first()
            perc_change = row.xpath('./td[5]/span/text()').extract_first()
            volume = row.xpath('./td[6]/span/text()').extract_first()
            volume_3_mth_avg = row.xpath('./td[7]/text()').extract_first()
            market_cap = row.xpath('./td[8]/span/text()').extract_first()
            pe_ratio = row.xpath('./td[9]/text()').extract_first()

            meta = {'symbol': symbol, 'name': name, 'price': price, 'change': change, 'perc_change': perc_change, 'volume': volume, 'volume_3_mth_avg': volume_3_mth_avg, 'market_cap': market_cap, 'pe_ratio': pe_ratio}

            yield Request(url = 'https://finance.yahoo.com/' + stock_link, meta = meta, callback = self.parse_stock_link)


    def parse_stock_link(self, response):
        symbol = response.meta['symbol']
        name = response.meta['name']
        price = response.meta['price']
        change = response.meta['change']
        perc_change = response.meta['perc_change']
        volume = response.meta['volume']
        volume_3_mth_avg = response.meta['volume_3_mth_avg']
        market_cap = response.meta['market_cap']
        pe_ratio = response.meta['pe_ratio']

        beta_3y_mthly = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[2]/span/text()').extract_first()
        one_yr_target_est = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]/span/text()').extract_first()

        item = YahoofinItem()
        item['symbol'] = symbol
        item['name'] = name
        item['price'] = price
        item['change'] = change
        item['perc_change'] = perc_change
        item['volume'] = volume
        item['volume_3_mth_avg'] = volume_3_mth_avg
        item['market_cap'] = market_cap
        item['pe_ratio'] = pe_ratio
        item['beta_3y_mthly'] = beta_3y_mthly
        item['one_yr_target_est'] = one_yr_target_est

        yield item
