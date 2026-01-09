# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import numpy as np
import streamlit as st

load_file=pickle.load(open("D:/sav file/trained_model.sav",'rb'))

def prediction_diabetes(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = load_file.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
def main():
    st.title("Diabetes Prediction App")

    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure level")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    Age = st.text_input("Age")
    
    diagnosis =''
    
    if st.button('Diabetes Prediction'):
        diagnosis=prediction_diabetes([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        st.success(diagnosis)
        
if __name__=='__main__':
    main()
                   