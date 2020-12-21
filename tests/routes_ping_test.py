#! /usr/bin/python3

import sys
# add module directory to system path for importing
sys.path.insert(0,'../api/app/routes')
from ping import ping
import pytest

def ping_test():
  '''Testing `/routes/ping.py`'''
  assert ping()['response'] == 'pong'
