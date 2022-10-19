from distutils.log import debug
import numpy as np
from flask import Flask,request,jsonify
from flask_restful import Api,Resource,reqparse
import pickle

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
    savedmodel=open('studentmodel.pickle', 'rb')
    newlinear=pickle.load(savedmodel)
    mine=[[5,401,4,2,16,2,16,8,2500]]
    mine=np.array(mine)
    #predict the outcome of your value(s)
    predictions=newlinear.predict(mine)

#loop through prediction to see if your data is corresponding well
    for x in range(len(predictions)):
        print(predictions[x])
        return jsonify(predictions[x])

#this enables the api endpoints
api.add_resource(ml,'/')


#this starts the server
if __name__ == "__main__":
     app.run(debug =True)