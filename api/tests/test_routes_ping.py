#!/usr/bin/env python3

from append_sys_path import append_sys_path; append_sys_path()
from ping import ping


def test_ping():
  assert ping(None)['response'] == 'pong'
  
  
if __name__ == '__main__':
  tests = [test_ping]
  for test in tests:
    test()
    print(f'{test.__name__}: Succesful')
