#!/usr/bin/python
# -*- coding: UTF-8 -*-

class UserInfo:
    def __init__(self, json_data):
        self.email = json_data['email']
        self.key_words = json_data['key_word']
        pass

class AdminInfo:
    def __init__(self, json_data):
        self.email = json_data['email']
        self.passwd = json_data['passwd']

class CompanyInfo:
    def __init__(self, json_data):
        self.url = json_data['url']
        self.name = json_data['name']
