#!/usr/bin/env python3
import requests
import sys
import json
import os
import socket
import random
import string
import hashlib
import numpy as np

def basename(file_path):
    pos = file_path.rfind('/')
    return file_path[pos+1 : ]

# run os.system()
def set_os_system(command_str):
    #print(command_str)
    if os.system(command_str) != 0:
      raise Exception('Failed to execute this command: "%s"' % command_str)

def readlines(file_path):
  with open(file_path) as f:
    contents = f.readlines()
    contents = [x.strip() for x in contents]
    ret = []
    for line in contents:
      if line != '':
        ret.append(line)
    return ret

def read_file_lines_count(file_path):
  lines = readlines(file_path)
  return len(lines)

def readline(file_path):
  with open(file_path) as f:
    contents = f.readlines()
    ret = ''
    for content in contents:
      ret += content
    return ret

def read(json_data, key, is_require = True, default_value = ''):
  if json_data.__contains__(key):
    return json_data[key]
  else:
    if is_require:
      raise Exception('value of' + key + ' no found in config ' + json_data)
    else:
      return default_value

def file_exist(file_path):
  if os.path.isfile(file_path):
    return True
  else:
    return False

def download_file(url, user, token, target_file, payload = None):
  with open(target_file, "wb") as f:
    r = requests_get(url, auth_data=(user, token), payload=payload, stream_data=True)
    r.raise_for_status()
    for chunk in r.iter_content(chunk_size=8192):
      if chunk:
        f.write(chunk)
  return target_file

def parse_json_file(file_path):
  with open(file_path, "r") as file_py:
    json_data = json.load(file_py)
    return json_data

def write_string_to_file(content, file_path, param = "w"):
  with open(file_path, param) as f:
    f.write(content + '\n')

def requests_post(url, auth_data = None, json_data = None):
  requests.post(url, auth=auth_data, data=json_data)

def requests_get(url, auth_data = None, payload = None, verify_data = False, stream_data = True):
  return requests.get(url, auth=auth_data, params=payload, verify=verify_data, stream=stream_data)

def jenkins_start_post(url, auth_data, payload):
  requests_post(url, auth_data = auth_data, json_data = payload)

def send_status(url, status):
  requests_post(url, json_data = {'status': status})

def handle_status(url, status, message = ''):
  if status == 'FAILURE':
    send_status(url, status)
    raise Exception(message)

def random_string(string_length=10):
  """Generate a random string of fixed length """
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(string_length))

def write_json_list_file(file_path, json_list, param = "w"):
  with open(file_path, param) as file_py:
    for data in json_list:
      string_data = json.dumps(data)
      file_py.write(string_data +"\n")

def write_json_file(file_path, json_data, param = "w"):
  with open(file_path, param) as file_py:
    string_data = json.dumps(json_data)
    file_py.write(string_data +"\n")

def read_json_list_file(file_path):
  data = []
  with open(file_path, 'r') as file_py:
    for line in file_py:
      data.append(json.loads(line))
  return data

def clear_file(file_path):
  open(file_path, 'w').close()

def created_file(filepath):
  if not os.path.exists(filepath):
    with open(filepath, 'w') as f:
      pass

def get_file_md5(filepath):
  if not os.path.isfile(filepath):
    return None
  hash_md5 = hashlib.md5()
  with open(filepath, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
       hash_md5.update(chunk)
  return hash_md5.hexdigest()

def get_str_md5(string):
  hash_md5 = hashlib.md5()
  hash_md5.update(string.encode("utf-8"))
  return hash_md5.hexdigest()

def send_json_to_url(url, json_data):
  r = requests.post(url, json = json_data)
  return r.json()
