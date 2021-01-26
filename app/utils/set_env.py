#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass 
class APIEnv:
  '''default env vars for the ap'''
  env: 'str' = 'dev'
  name: 'str' = 'api'
  tag: 'str' = 'dev'
  host: 'str' = '0.0.0.0'
  port: 'int' = 8000
  debug: 'bool' = True
  workers: 'int' = 1

@dataclass
class DBEnv:
  '''default env vars for db connected to the app'''
  db: 'str' = 'db'
  user: 'str' = 'user'
  host_address: 'str' = '0.0.0.0'
  password: 'str' = 'password'
  port: 'str' = 5432

#set db_env_variables(:'') -> 'dict':
  #print('test')

#db_env_variables('db': 'postgres')

def set_env() -> 'Env':
  ''''''
  from os import environ
  
  store = {}
  
  # get env vars to set
  env = vars(APIEnv())
  set_env_vars = vars(APIEnv())
  var_names = set_env_vars.keys()
  # default env vars
  default_env_vars = list(environ.keys())
  
  for var in var_names:
    var_name = f'{var.upper()}'
    try:
      # add var to store
      store[var] = environ[var_name]
    except:
      # add var to env and store
      environ[var_name] = store[var] = env[var]
      
  # return dict as dataclass object
  return APIEnv(**store)


if __name__ == '__main__':
  API_ENV = set_env()
  print(API_ENV)
