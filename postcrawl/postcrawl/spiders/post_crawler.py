import scrapy
import json
from scrapy.spiders import CrawlSpider, Rule


class PostsSpider(scrapy.Spider):
    name = "posts"
    json_data = []
    try:
        json_file = open('links.json')
        for line in json_file:
            json_data.append(line)
    except OSError:
        print('file not found')

    counter = 1
    links_list = []
    while counter < len(json_data) - 1:
        if json_data[counter][-2] == ',':
            json_data[counter] = json_data[counter][:-2]
        temp_json = json.loads(json_data[counter])
        #del temp_json['link'][-1]
        for i, k in enumerate(temp_json['link']):
            if k[:5] == 'https':
                links_list.append(temp_json['link'][i])
        counter += 1
    start_urls = list(dict.fromkeys(links_list))

    def parse(self, response):
        post = response.css('div.pb-container')
        yield {
            'title': post.css('h1::text').get(),
            'content': post.css('p::text').getall()
        }


