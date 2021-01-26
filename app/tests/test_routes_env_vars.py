#!/usr/bin/env python3

from append_sys_path import append_sys_path; append_sys_path()
from env_vars import env_vars


def test_env_vars():
  '''Testing `/routes/test.py`'''
  assert type(env_vars(None)) is not None


if __name__ == '__main__':
  tests = [test_env_vars]
  for test in tests:
    test()
    print(f'{test.__name__}: Succesful')
