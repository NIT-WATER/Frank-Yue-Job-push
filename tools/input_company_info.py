#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import time 
import sys
sys.path.append("..") 
from common.test_tool import *

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--company_name', default = '', help = 'Company name.')
  parser.add_argument('--company_url', default = '', help = 'Company url.')
  parser.add_argument('--is_have_crawl_code', action='store_true', default=False,
                                  help='If has crawl code')
  parser.add_argument('--crawl_code_path', default=False, help='Crawl code file path')
  args = parser.parse_args()
  json_date = None
  with open('./company.json') as f:
    json_date = json.load(f)
  json_date.append(company_obj)
  with open('./company.json', 'w') as f:
    json.dump(json_date, f)
