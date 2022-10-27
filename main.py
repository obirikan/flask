from distutils.log import debug
import json
import numpy as np
from flask_cors import CORS
from flask import Flask,request,jsonify
import pickle

app = Flask(__name__)
CORS(app)

@app.route('/get',methods =['POST'])
def post_details():
    data = request.json
    mine=[data['name']]
    mine=np.array(mine)
    savedmodel=open('heartprediction.pickle', 'rb')
    newmodel=pickle.load(savedmodel)


    myvalues=[[20, 0 ,3, 100 ,100,0,1,100]]
    
    #predict the outcome of your value(s)
    predicted=newmodel.predict(mine)
    names=['absense','presence']
    
#loop through prediction to see if your data is corresponding well
    for x in range(len(predicted)):
        return jsonify(names[predicted[x]])

#this starts the server
if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
