#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass 
class Env:
  '''class containing default env vars for the app'''
  env: 'str' = 'dev'
  name: 'str' = 'api'
  tag: 'str' = 'dev'
  host: 'str' = '0.0.0.0'
  port: 'int' = 8000
  debug: 'bool' = True
  workers: 'int' = 1

def set_env() -> 'int':
  ''''''
  from os import environ
  
  # get default or env vars
  env = Env()
  env = vars(env)
  variables = env.keys()
  existing_variables = list(environ.keys())
  
  
  for var in variables:
    # reset the value for key in `env` if var in env
    if var.upper() in existing_variables:
      env[var] = environ[var.upper()]
    # add the var to env if it doesn't exist
    else:
      environ[var.upper()] = str(env[var])

  env = Env(**env)
  return env

if __name__ == '__main__':
  ENV = set_env()
  print(ENV)