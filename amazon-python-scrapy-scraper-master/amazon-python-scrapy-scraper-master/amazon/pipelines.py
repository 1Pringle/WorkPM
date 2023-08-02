# Define your item pipelines here
#.html

from itemadapter import ItemAdapter


class AmazonPipeline:
    def process_item(self, item, spider):
        return item
