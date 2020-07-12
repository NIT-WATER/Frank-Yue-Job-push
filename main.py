#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import time 
import argparse
from master import *
from datetime import datetime

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--config_file', default = './meta/config.json', help = 'Config file.')
  parser.add_argument('--company_file', default = './meta/company.json', help = 'Company file.')
  parser.add_argument('--user_file', default = './meta/user.json', help = 'User file.')
  parser.add_argument('--force', action='store_true', default=False,
                                  help='For force send')
  args = parser.parse_args()

  '''load config, user and company'''
  config_info = None
  user_info = None
  company_info = None
  with open(args.config_file) as f:
    config_info = json.load(f)
  with open(args.company_file) as f:
    company_info = json.load(f)
  with open(args.user_file) as f:
    user_info = json.load(f)
        
  last_time = config_info['data'] 
  last_time_list = last_time.split('/')
  last_time = datetime.date(last_time_list[0], last_time_list[1], last_time_list[2])
  send_days = config_info['send_days'] 
  is_force_send = args.force
  while True:
    time.sleep(1000)
    now_time = datetime.now()
    print(now_time)
    if is_force_send or (now_time - last_time).days >= send_days:
      print('Time to send e-mail')

      master_handle = Master(user_info, admin_info, company_info)
      master_handle.run()
      last_time = datetime.now()
      is_force_send = False


