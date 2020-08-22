import scrapy
from scrapy.spiders import CrawlSpider, Rule


class PostsSpider(scrapy.Spider):
    name = "links"
    start_urls = [
        'https://www.defensenews.com/stories/air/1/',
        'https://www.defensenews.com/stories/air/21/',
        'https://www.defensenews.com/stories/air/41/',
        'https://www.defensenews.com/stories/air/61/',
        'https://www.defensenews.com/stories/air/81/',
        'https://www.defensenews.com/stories/air/101/',
        'https://www.defensenews.com/stories/air/121/',
        'https://www.defensenews.com/stories/air/141/',
        'https://www.defensenews.com/stories/air/161/',
        'https://www.defensenews.com/stories/air/181/',
        'https://www.defensenews.com/stories/air/201/',
        'https://www.defensenews.com/stories/air/221/',
        'https://www.defensenews.com/stories/air/241/',
        'https://www.defensenews.com/stories/air/261/',
        'https://www.defensenews.com/stories/air/281/',
        'https://www.defensenews.com/stories/air/301/',
        'https://www.defensenews.com/stories/air/321/',
        'https://www.defensenews.com/stories/air/341/',
        'https://www.defensenews.com/stories/air/361/',
        'https://www.defensenews.com/stories/air/381/',
        'https://www.defensenews.com/stories/air/401/'
    ]

    def parse(self, response):
        post = response.css('div.pb-container')
        test = post.css('div.result-listing')
        for i in test:
            yield {
                'link': i.css('a::attr(href)').getall()
            }

# test = post.css('div.result-listing')
# for i in test: i.css('a::attr(href)').getall()
# for i in test: i.css('h4::text').getall()
