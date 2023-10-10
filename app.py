from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import RobustScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            age=int(request.form.get('age')),
            sex=int(request.form.get('sex')),
            cp=int(request.form.get('cp')),
            trtbps=int(request.form.get('trtbps')),
            chol=int(request.form.get('chol')),
            fbs=int(request.form.get('fbs')),
            restecg=int(request.form.get('restecg')),
            thalachh=int(request.form.get('thalachh')),
            exng=int(request.form.get('exng')),
            oldpeak=float(request.form.get('oldpeak')),
            slp=int(request.form.get('slp')),
            caa=int(request.form.get('caa')),
            thall=int(request.form.get('thall'))
            

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results)
        #the results in above line is used in home.html line 108
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)        