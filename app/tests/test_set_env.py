#!/usr/bin/env python3

from append_sys_path import append_sys_path; append_sys_path()
from set_env import set_env


def test_set_env():
  '''pytest'''
  ENV = set_env()
  assert ENV is not None
