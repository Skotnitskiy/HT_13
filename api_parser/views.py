import logging.config

import psycopg2
import requests
import sys
from datetime import datetime
from pprint import pprint

from django.http import HttpResponse
from psycopg2.extras import RealDictCursor
from psycopg2.sql import SQL, Identifier

from api_parser import config as conf

conn = psycopg2.connect(database=conf.db_name, user=conf.db_user, host=conf.db_host)
cursor = conn.cursor()
dict_cur = conn.cursor(cursor_factory=RealDictCursor)


def get_table_name(category):
    return "{}_{}".format(category, category)


class Parser(object):

    @staticmethod
    def write_record(table, record, old_ids):
        table = get_table_name(table)
        id = record.get('id')
        get_category_id_query = SQL("SELECT category_id FROM {}").format(Identifier(table))
        cursor.execute(get_category_id_query)
        category_id = cursor.fetchone()[0]
        if id not in old_ids:
            cursor.execute(SQL("INSERT INTO {}(id, category_id) VALUES (%s, %s)")
                           .format(Identifier(table)), (id, category_id))
            conn.commit()
            print("===================Inserted new record!===================")
        for column, value in record.items():
            cursor.execute(SQL("UPDATE {} SET {} = %s WHERE id = %s;").
                           format(Identifier(table), Identifier(column)), (value, str(id)))
        conn.commit()

    @staticmethod
    def get_old_ids(table):
        table = get_table_name(table)
        get_ids_query = SQL("SELECT id FROM {}").format(Identifier(table))
        cursor.execute(get_ids_query)
        ids = cursor.fetchall()
        ids_int = []
        for id in ids:
            ids_int += [int(id[0])]
        return ids_int

    def __init__(self):
        logging.config.dictConfig(conf.dictLogConfig)
        self.rep_empty = False
        self.logger = logging.getLogger("DataParserApp")
        self.logger.info("Program started")

    def get_records_id(self, category):
        ids_records = {}
        if category:
            categories = category
        else:
            categories = conf.categories_list
        for catg in categories:
            self.logger.info("request was sent to obtain the list of IDs by category {}".format(catg))
            request = requests.get(conf.categorie_url.format(catg))
            self.logger.info("list is received")
            try:
                ids_records.update({catg: request.json()})
            except requests.exceptions.RequestException as e:
                self.logger.error(e)
                print(e)
                sys.exit(1)
            print('category', catg, "ids received")
        return ids_records

    def record(self, *category):
        ids_records = self.get_records_id(category)
        self.logger.info("report generation started...")
        record_line = {}
        for key, val in ids_records.items():
            old_ids = self.get_old_ids(key)
            for id_rec in val:
                try:
                    record_line = requests.get(conf.item_url.format(id_rec)).json()
                except requests.exceptions.RequestException as e:
                    self.logger.error(e)
                    print(e)
                if record_line and record_line.get("score"):
                    if record_line.get("score") >= conf.score:
                        date = datetime.date(datetime.fromtimestamp((record_line.get('time'))))
                        if date >= conf.from_date:
                            self.write_record(key, record_line, old_ids)
                            self.logger.info("record {} added to result list".format(id_rec))
                            pprint(record_line)


def parse(request):
    parser = Parser()
    parser.record()
    return HttpResponse("Parsing completed")


def parse_category(request, category):
    if category in conf.categories_list:
        parser = Parser()
        parser.record(category)
        return HttpResponse("Parsing completed")
    else:
        return HttpResponse("Category '{}' is not exist".format(category))