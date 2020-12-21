#! /usr/bin/python3

from os.path import split, realpath
from importlib.machinery import SourceFileLoader
from typing import Dict, Any
from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException

# set app root directory
API_DIR = split(realpath(__file__))[0]


class Payload(BaseModel):
  '''
  # Request Payload Model
  - **route**: route in `/routes` 
  - **data**: data passed to function loaded 
  '''
  route: str = 'ping'
  data: Any = {}
  


app = FastAPI()


@app.get('/api')
async def root() -> dict:
  '''Ping the API'''
  return {'ping': 'pong'}

@app.post('/api')
async def api(payload: Payload) -> dict:
  '''
  # API
  - **route**: each request must have a route
  - **data**: optional
  '''
  # check if the payload contains a route
  if 'route' not in payload.dict().keys():
    return HTTPException

  try:
    # load routes defined in `/routes` folder
    route = SourceFileLoader(payload.route,
      f'{API_DIR}/routes/{payload.route}.py'
    ).load_module()
    # load function from route
    func = getattr(route, payload.route)
    return func(payload.data)
  except Exception as error:
    return {'error': repr(error)}
  
