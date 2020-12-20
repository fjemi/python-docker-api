from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
  '''Ping the API'''
  return {'ping': 'pong'}