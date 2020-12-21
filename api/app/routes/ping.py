#! /usr/bin/python3

from typing import Any, Dict
from datetime import datetime, timedelta

def ping(data: None) -> dict:
  ''' Returns request response time
  '''
  # function's start time
  start_time = datetime.now()
  # function's end time in milliseconds
  end_time = (datetime.now() - start_time).total_seconds() * 100000
  return {
    'response': 'pong',
    'response_time': f'{end_time:.1f} μs'
  }

if __name__ == '__main__':
  print(ping())
