#!/usr/bin/env python3

from append_sys_path import append_sys_path; append_sys_path()
from hello_world import hello_world


def test_hello_world():
  '''Testing route at `/routes/helloworld.py`'''
  assert hello_world(None) == {'hello': 'world'}


if __name__ == '__main__':
  tests = [test_hello_world]
  for test in tests:
    test()
    print(f'{test.__name__}: Succesful')
