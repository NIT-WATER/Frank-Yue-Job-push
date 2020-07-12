#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import time
import sys
import os
sys.path.append("..")
from common.test_tool import *

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--company_name', default = '', help = 'Company name.')
  parser.add_argument('--company_url', default = 'xxx', help = 'Company url.')
  parser.add_argument('--is_have_crawl_code', action='store_true', default=True,
                                  help='If has crawl code')
  parser.add_argument('--crawl_code_path', default=False, help='Crawl code file path')
  args = parser.parse_args()
  json_date = None
  with open('../meta/company.json') as f:
    json_date = json.load(f)

  is_have_company = False
  for company in json_date:
    if company['name'] == args.company_name:
      if args.company_url == 'xxx':
        company['url'] = args.company_url
      company['is_have_crawl_code'] = args.is_have_crawl_code
      is_have_company = True

  if is_have_company is False:
    company_obj = {}
    company_obj['name'] = args.company_name
    company_obj['url'] = args.company_url
    company_obj['is_have_crawl_code'] = args.is_have_crawl_code
    json_date.append(company_obj)

  with open('./company.json', 'w') as f:
    json.dump(json_date, f)

  os.system(f'mkdir -p ../src/{args.company_name}')
  os.system(f'cp {args.crawl_code_path} ../src/{args.company_name}/crawl.py')
