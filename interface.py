from flask import Flask ,render_template,jsonify,request 
import config
from project_app.utils import DiabeticPrediction
import pickle
import json

app=Flask(__name__)

@app.route("/")

def base():
    return render_template("home.html")

@app.route("/predict",methods=['POST'])

def home():
    Glucose =request.form["Glucose"]
    BloodPressure = request.form["BloodPressure"]
    SkinThickness = request.form["SkinThickness"]
    Insulin = request.form["Insulin"]
    bmi= request.form["bmi"]
    DiabetesPedigreeFunction = request.form["DiabetesPedigreeFunction"]
    Age = request.form["Age"]

    get_pred=DiabeticPrediction(Glucose, BloodPressure, SkinThickness, Insulin,bmi,DiabetesPedigreeFunction, Age)
    result=get_pred.diabetic_prediction()

    return render_template("after.html",data=result)  
    # return jsonify ({result:f"the result is {result}"}) 

if __name__== "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NO,debug=True)






