import scrapy
from scrapy.spiders import CrawlSpider, Rule


class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://www.defensenews.com/global/europe/2020/08/21/rolls-royce-backs-hypersonic-power-specialist-reaction-engines-with-new-investment/'
    ]

    def parse(self, response):
        post = response.css('div.pb-container')
        yield {
            'title': post.css('h1::text').get(),
            'content': post.css('p::text').getall()
        }


