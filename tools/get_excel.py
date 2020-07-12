#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import time 
import argparse
from datetime import datetime
import xlrd

if __name__ == "__main__":
  data = xlrd.open_workbook('Job Search.xlsx')
  table = data.sheets()[0]
  json_date = []
  for i in range(table.nrows):
    company_obj = {}
    company_obj['name'] = table.row_values(i)[1]
    company_obj['url'] = table.row_values(i)[2]
    json_date.append(company_obj)
    print(table.row_values(i))
    
   
  with open('./company.json', 'w') as f:
    json.dump(json_date, f)
