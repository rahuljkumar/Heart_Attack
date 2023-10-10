import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\proprocessor.pkl'
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            if preds==0:
                preds="No risk of a heart attack"
            else:
                preds="There is a risk of heart attack"
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        age:int, 
        sex:int, 
        cp:int, 
        trtbps:int, 
        chol:int, 
        fbs:int, 
        restecg:int, 
        thalachh:int, 
        exng:int, 
        oldpeak:float, 
        slp:int, 
        caa:int, 
        thall:int):

        self.age = age
        self.sex = sex
        self.cp = cp
        self.trtbps = trtbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalachh = thalachh
        self.exng = exng
        self.oldpeak = oldpeak
        self.slp = slp
        self.caa = caa
        self.thall = thall
   

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "cp": [self.cp],
                "trtbps": [self.trtbps],
                "chol": [self.chol],
                "fbs": [self.fbs],
                "restecg": [self.restecg],
                "thalachh": [self.thalachh],
                "exng": [self.exng],
                "oldpeak": [self.oldpeak],
                "slp": [self.slp],
                "caa": [self.caa],
                "thall": [self.thall]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)