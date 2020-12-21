#! /usr/bin/python3

import sys
# add module directory to system path for importing
sys.path.insert(0,'../api/app/routes')
from hello_world import hello_world
import pytest


def helloworld_test():
  '''Testing route at `/routes/helloworld.py`'''
  assert helloworld() == {'response': 'hello world'}
