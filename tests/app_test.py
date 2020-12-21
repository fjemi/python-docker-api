#!/usr/bin/env python3

import sys
# add module directory to system path for importing
sys.path.insert(0,'../api/app')
from app import app
from fastapi.testclient import TestClient
from fastapi import HTTPException


client = TestClient(app)


def test_root():
  '''Test API Get request in `../api/app/app.py`
  '''
  response = client.get('/api')
  assert response.status_code == 200
  assert response.json() == {'ping': 'pong'}


def test_api():
  '''Test the API Post request in `../api/app/app.py`
  '''
  # no route passed
  response = client.post('/api', {})
  assert response.status_code == 422 or response.status_code == 405
  # data is not a valid json
  response = client.post('/api', json={'route': 'ping', 'data': {}})
  assert response.status_code == 200
