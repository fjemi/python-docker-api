#! /usr/bin/python3

from os import environ

# TODO  add login and token
def env_vars() -> dict:
  ''' Returns a JSON containg system enviroment variables
  '''
  return environ
  
if __name__ == '__main__':
  print(env_vars())
