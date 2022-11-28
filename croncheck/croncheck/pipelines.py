# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class CroncheckPipeline:
    def __init__(self):
        self.create_conn()
        # self.create_table()

    def create_conn(self):
        self.conn = sqlite3.connect('C:\\Users\\M. Abu Hurairah\\Desktop\\cron_check\\cron_check\\db.sqlite3')
        self.curr =self.conn.cursor()

    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS weather_weather""")
    #     self.curr.execute("""create table weather_weather(
    #                          city text,
    #                         curr_temp text,
    #                          )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
            self.curr.execute(""" INSERT INTO weather_weather(city,curr_temp) VALUES(?,?)""", (
               item['city'],
               item['curr_temp'] 
            ))
            self.conn.commit()