# -*- coding: utf-8 -*-

# 在这里定义你的数据处理管道
#
# 不要忘记将你的管道添加到ITEM_PIPELINES设置中
# 参考链接: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TextFilePipeline(object):
    def __init__(self, output_file):
        self.output_file = output_file

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            output_file="output.txt"
        )

    def open_spider(self, spider):
        # 在爬虫开始时执行的方法，用于创建并打开输出文件
        self.file = open(self.output_file, 'w', encoding='utf-8')

    def close_spider(self, spider):
        # 在爬虫结束时执行的方法，用于关闭输出文件
        self.file.close()

    def process_item(self, item, spider):
        # 处理每个爬取到的数据项，并将其写入输出文件
#        if isinstance(item, 'title'):  # 替换成您的数据项类
        self.write_item(item)
        return item

    def write_item(self, item):
        # 将数据项的字段写入文本文件
        self.file.write(f"Title: {item['title']}\n")
        self.file.write(f"Content: {item['content']}\n\n")
