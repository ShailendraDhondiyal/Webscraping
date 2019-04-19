https://finance.yahoo.com/sector/ms_technology

Looking at the day-end performance of technology stocks, including -- how many had +ve and -ve changes, top 5 %gainers, top 5 % losers.
Exploring if %change was linked to factors like stock_price and market_cap.
Finding out the beta for the stocks, and correlating % change with beta.
Finding out the 1-year_estimate for the stocks, and correlating it with % change for the day.


rows[1].xpath('./td[2]/text()').extract_first()
rows[2].xpath('./td[2]/text()').extract_first()
rows[4].xpath('./td[2]/text()').extract_first()

response.xpath('')
response.xpath('')
response.xpath('')
response.xpath('')
================================================================================
symbol = rows[1].xpath('./td[1]/a/text()').extract_first()
name = rows[1].xpath('./td[2]/text()').extract_first()
price = rows[1].xpath('./td[3]/span/text()').extract_first()
change = rows[1].xpath('./td[4]/span/text()').extract_first()
perc_change = rows[1].xpath('./td[5]/span/text()').extract_first()
volume = rows[1].xpath('./td[6]/span/text()').extract_first()
volume_3_mth_avg = rows[1].xpath('./td[7]/text()').extract_first()
market_cap = rows[1].xpath('./td[8]/span/text()').extract_first()
pe_ratio = rows[1].xpath('./td[9]/text()').extract_first()


================================================================================
stock_link = row.xpath('./td[1]/a/@href').extract_first()
symbol = row.xpath('./td[1]/a/text()').extract_first()
name = rows.xpath('./td[2]/text()').extract_first()
price = rows.xpath('./td[3]/span/text()').extract_first()
change = rows.xpath('./td[4]/span/text()').extract_first()
perc_change = rows.xpath('./td[5]/span/text()').extract_first()
volume = rows.xpath('./td[6]/span/text()').extract_first()
volume_3_mth_avg = rows.xpath('./td[7]/text()').extract_first()
market_cap = rows.xpath('./td[8]/span/text()').extract_first()
pe_ratio = rows.xpath('./td[9]/text()').extract_first()

beta_3y_mthly = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[2]/span/text()').extract_first()
one_yr_target_est = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]/span/text()').extract_first()

meta = {'symbol': symbol, 'name': name, 'price': price, 'change': change,  , 'perc_change': perc_change, 'volume': volume, 'volume_3_mth_avg': volume_3_mth_avg, 'market_cap': market_cap, 'pe_ratio': pe_ratio}


rows = response.xpath('//div[@id="fin-scr-res-table"]//table//tr')
# len(rows): 101

pages = response.xpath('//div[@id="fin-scr-res-table"]/div[1]/div[1]/span[2]/span/text()').extract_first()
# 1-100 of 465 results

_, per_page, total = re.findall('\d+', pages)
num_pages = int(total)//int(per_page) + 1
# 5
