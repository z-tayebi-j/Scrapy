import scrapy
import os
import csv


class backpacksSpider(scrapy.Spider):
    name = 'backpacks'

    def start_requests(self):
        self.i = 1
        url = f'https://quera.org/problemset?tag=78&tag=88&page={self.i}'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        questions = response.xpath('/html/body/div[5]/div[2]/main/section/div[2]/div/table/tbody/tr')
        next_page_disabled = response.xpath('/html/body/div[5]/div[2]/main/section/div[3]/button[3]/@disabled').get()

        with open(os.path.join(os.getcwd(), 'data.csv'), 'a') as file:
            for question in questions:
                name = question.xpath('td[2]/a/text()').get()
                link = question.xpath('td[2]/a/@href').get()
                level = question.xpath('td[5]/p/text()').get()
                question_object = {'name': name, 'link': link, 'level': level}
                writer = csv.DictWriter(file, fieldnames=['name', 'link', 'level'])
                writer.writerow(question_object)
        if len(questions) == 25:
            self.i += 1
            url = f'https://quera.org/problemset?tag=78&tag=88&page={self.i}'
            yield scrapy.Request(url=url, callback=self.parse)
