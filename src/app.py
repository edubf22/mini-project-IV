# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle

# Create an API 
app = Flask(__name__)
api = Api(app)

# Function for feature engineering 
def transform_features(df):
    # Log of loan amount
    df['LoanAmount_log'] = np.log(df['LoanAmount'].astype('float64')) 

    # Total income and log of total income
    df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']
    df['Total_Income_log'] = np.log(df['Total_Income'].astype('float64')) 
    
    # drop the original features
    transformed_feats = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Total_Income']
    df = df.drop(columns=transformed_feats)
    
    # replace the names so the model works with input data
    df.columns = df.columns.str.replace('_log', '')
    return df

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