from dataclasses import dataclass

@dataclass
class Data:
  test: 'str' = None

@dataclass
class ConnectParams:
  db: 'str' = 'db'
  user: 'str' = 'user'
  host_address: 'str' = '0.0.0.0'
  password: 'str' = 'password'
  port: 'str' = 5432


def set_connection(data: 'dict') -> 'dict':
  ''''''

  #data = ConnectParams(**data)
  connect_params = ConnectParams()

  

  return ()




'''
import psycopg2
from os import environ

connection = psycopg2.connect(
    environ['DB_URL']
  )
connection.autocommit = True
'''


def execute_sql(data: 'dict'):
  ''''''
  
  data = Data(**data)
  
  print(vars(data))
  return vars(data)

if __name__ == '__main__':
  execute_sql({})
