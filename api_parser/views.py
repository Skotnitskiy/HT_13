import logging.config
import time
import smtplib
from email.message import EmailMessage

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
news_counter = {key: 0 for key in conf.categories_list}
news_time = {key: 0.0 for key in conf.categories_list}


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
        start_time = 0.0
        for key, val in ids_records.items():
            old_ids = self.get_old_ids(key)
            for id_rec in val:
                try:
                    start_time = time.time()
                    record_line = requests.get(conf.item_url.format(id_rec)).json()
                except requests.exceptions.RequestException as e:
                    self.logger.error(e)
                    print(e)
                if record_line and record_line.get("score"):
                    if record_line.get("score") >= conf.score:
                        date = datetime.date(datetime.fromtimestamp((record_line.get('time'))))
                        if date >= conf.from_date:
                            self.write_record(key, record_line, old_ids)
                            end_time = time.time()
                            cnt = news_counter.get(key)
                            cnt += 1
                            result_time = (end_time - start_time)/60
                            time_cnt = news_time.get(key)
                            time_cnt += result_time
                            news_time.update({key: time_cnt})
                            news_counter.update({key: cnt})
                            self.logger.info("record {} added to result list".format(id_rec))
                            pprint(record_line)


def report():
    html = '<table border=1>' \
           '<th>Category</th>' \
           '<th>Count</th>' \
           '<th>Minutes</th>' \
           '{} </table>'
    rows = ''
    for category, value in news_counter.items():
        if value > 0:
            rows += '<tr><td>{}</td>'.format(category)
            rows += '<td>{}</td>'.format(value)
            rows += '<td>{}</td></tr>'.format(news_time.get(category))
    return html.format(rows)


def send_report(rep):
    gmail_user = 'geekpy.test@gmail.com'
    gmail_password = 'qwerty123Ss'

    msg = EmailMessage()
    you = 'one2011@yandex.ua'
    msg['Subject'] = 'Report Sergey Skotnitskiy'
    msg['From'] = gmail_user
    msg['To'] = you
    msg.set_content(rep)
    msg.set_type('text/html')

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(gmail_user, gmail_password)
    s.sendmail(gmail_user, [you], msg.as_string())
    s.close()


def parse(request):
    parser = Parser()
    parser.record()
    rep = report()
    send_report(rep)
    return HttpResponse(rep)


def parse_category(request, category):
    if category in conf.categories_list:
        parser = Parser()
        parser.record(category)
        rep = report()
        send_report(rep)
        return HttpResponse(rep)
    else:
        return HttpResponse("Category '{}' is not exist".format(category))
