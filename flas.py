from distutils.log import debug
from flask import Flask
from flask_restful import Api,Resource,reqparse

#enables you to make put request with ease
args=reqparse.RequestParser()

#request arguements 
args.add_argument('name',type=str, help='err')

#insantiate varibles to enable create enpoits
app = Flask(__name__)
api= Api(app)

#this is where you instantiate the endpoints
class ml(Resource):
  def put(self):
      arr=args.parse_args()
      
      return text

#this enables the api endpoits
api.add_resource(ml,'/')


#this starts the server
if __name__ == "__main__":
     app.run(debug =True)