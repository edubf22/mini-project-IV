# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

# Create an API 
app = Flask(__name__)
api = Api(app)

# Load model 
model = pickle.load(open("miniproject-model.p", "rb"))

# Create an endpoint where we can communicate with our ML model
class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(
            json_data.values(), index=json_data.keys()).transpose()
        
        # Get predictions
        res = model.predict_proba(df)
        return res.tolist()

# assign endpoint
api.add_resource(Scoring, '/scoring')

# Create an application run 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)