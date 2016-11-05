import scrapy
from time import strftime, strptime, localtime, mktime, time as currentTime

class NewYorkSpider(scrapy.Spider):
	
	name = "fatalities"
	# A query we will use for later when there is more reliable results
	# str(list_of_columns[0].css("::text").extract_first()) != strftime("%B %d, %Y", gmtime())
	# if str(list_of_columns[1].css("::text").extract_first()) != "Texas" 

	start_urls = ["http://www.gunviolencearchive.org/last-72-hours", ]
	
	def parse(self, response):
		four_days_ago = currentTime() - 345600


		for row in response.css("table.responsive tbody tr"):
			list_of_columns = row.css("td")
			cell_date = list_of_columns[0].css("::text").extract_first()
			epoch_date = strptime(cell_date, "%B %d, %Y")
			
			
			#Unique Identifier of the casuality that was created
			#will collect a snippet of the uid
			
			incident = list_of_columns[6].css("ul li a::attr('href')").extract_first()
			
		
			if int(list_of_columns[5].css("::text").extract_first()) == 0 or \
			mktime(epoch_date) <= four_days_ago:
				pass
			
			else:
				yield {
					"losses": list_of_columns[5].css("::text").extract_first(),
					"incident": list_of_columns[6].css(" ul li a::attr('href')").extract_first(),
					"source": list_of_columns[6].css("ul li.last a::attr('href')").extract_first(),
					"date": list_of_columns[0].css("::text").extract_first(),
					"state": list_of_columns[1].css("::text").extract_first(),
					"uid": incident[10:len(incident)]
				}

			
			#Create a field that checks the to see if there's another page with records 
			# greater than 4 days ago

		next_page = response.css('li.pager-next a::attr(href)').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse) 	
