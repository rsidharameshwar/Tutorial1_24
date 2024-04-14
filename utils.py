import numpy as np
import numpy as np
import config
import json
import pickle

class DiabeticPrediction():

    def __init__(self,Glucose, BloodPressure, SkinThickness, Insulin, bmi,DiabetesPedigreeFunction, Age):
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin
        self.bmi=bmi
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age= Age

    def load_model(self):
        with open(config.pkl_model_path,"rb") as f:
            self.model=pickle.load(f)

        with open(config.project_path,"r") as f:
            self.project = json.load(f)     

    def diabetic_prediction(self):
        self.load_model()
        test_array=np.zeros(len(self.project["columns"]))

        test_array[0]=self.Glucose
        test_array[1]=self.BloodPressure
        test_array[2]=self.SkinThickness
        test_array[3]=self.Insulin
        test_array[4]=self.bmi
        test_array[5]=self.DiabetesPedigreeFunction
        test_array[6]=self.Age

        prediction=self.model.predict([test_array])

        return prediction



    

