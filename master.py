#!/usr/bin/python
# -*- coding: UTF-8 -*-

from common.Struct import *
from send import *
from crawl import *

class Master:
    def __init__(self, user_info, admin_info, company_info):
        self.user_info = user_info
        self.admin_info = admin_info
        self.company_info = company_info

    def run(self):
        for company in self.company_info:
            crawl_information = self.get_crawl_func(company)
            msg = crawl_information(user, company)
            for user in self.user_info:
                send_email(self.admin_info, user, msg)

    def get_crawl_func(self, company):
        file, pathname, description = imp.find_module("f'./src/{company.name}/crawl.py'", path=['./'])
        mod = imp.load_module('', file, pathname, description)
        mod.crawl_information()
