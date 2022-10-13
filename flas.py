from distutils.log import debug
from flask import Flask,request,jsonify
from flask_restful import Api,Resource,reqparse

#enables you to make put request with ease
args=reqparse.RequestParser()

#request arguements 
# args.add_argument('name',type=str, help='err')

#insantiate varibles to enable create enpoits
app = Flask(__name__)
api= Api(app)

#this is where you instantiate the endpoints
class ml(Resource):
  def post(self):
    data = request.json
    return jsonify(data)

#this enables the api endpoints
api.add_resource(ml,'/')


#this starts the server
if __name__ == "__main__":
     app.run(debug =True)