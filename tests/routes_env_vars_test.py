#! /usr/bin/python3

import sys
# add module directory to system path for importing
sys.path.insert(0,'../api/app/routes')
from env_vars import env_vars
import pytest


def env_vars_test():
  '''Testing `/routes/test.py`'''
  assert type(env_vars()) == dict
