# microframework
from flask import Flask
from flask_restful import Resource, Api
# dates/time
from datetime import datetime
# operating system
import os

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Message(Resource):
    def get(self, message):
        if message == 'hello':
            return {'greetings': 'hello world'}
        elif message == 'bye':
            return {'farewell': 'goodbye world'}
 
class Name(Resource):
    def get(self, name):
        if name.strip() == '':
            abort(404, message="No name was given")
        else:
            return {'hello': name.strip()}
        
class FullName(Resource):
    def get(self, first, last):
        return { 'name': {'first': first, 'last': last}}
 
class Date(Resource):
    def get(self):
        date = datetime.now().strftime('%y-%m-%d')
        time = datetime.now().strftime('%H:%M:%S')
        return {'Date': date,
                'Time': time
                }
    
class OS(Resource):
    def get(self):
        return {'System-Dependent Version Information': os.uname()}

api.add_resource(HelloWorld, '/')    
api.add_resource(Message, '/message=<message>')
api.add_resource(Date, '/date')
api.add_resource(Name, '/name=<name>', '/')
api.add_resource(FullName, '/last=<last>&first=<first>')
api.add_resource(OS, '/os')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
