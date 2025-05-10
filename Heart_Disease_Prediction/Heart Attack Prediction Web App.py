# -*- coding: utf-8 -*-
"""
Created on Sat May 10 01:33:56 2025

@author: ASHBI
"""


import pickle 
import numpy as np

import streamlit as st


load_model = pickle.load(open('C:/Users/LENOVO/Desktop/Exercism/MachineLearning/MLModel/trained_model.sav', 'rb'))

lr_model, std = load_model


# Create a function for the prediction

def heart_attack_prediction(input_data):
   
    input_np_arr = np.asarray(input_data)

    input_data = input_np_arr.reshape(1,-1)

    model_result = lr_model.predict(input_data)[0]

    return model_result
    
    
    
def main():
    
 
    # Title
    st.title("A.I. Based Heart Disease Predictor")
    
    # Input Forms
    age = st.text_input('Age of the Patient')
    sex = st.selectbox('Sex', ['Female', 'Male'], index=0)
    cp = st.selectbox('Type of Chest Pain', ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    trestbps = st.text_input('Resting Blood Pressure (in mm Hg)')
    chol = st.text_input('Cholestrol (mg/dl)')
    fbs = st.selectbox('Is Fasting Blood Sugar > 120 mg/dl?', ['Yes', 'No'])
    restecg = st.selectbox('Resting ECG (0-2',  ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
    thalach = st.text_input('Maximum Heart Rate Acheived')
    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.text_input('ST depression induced by exercise relative to rest ST depression induced by exercise relative to rest')
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy",[0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (Thal)", ["Normal", "Fixed defect", "Reversible defect"])
    
   
   
    # Submit Button
    if st.button("Submit"):
        try:
            
            # Convert to numerical
            sex = 1 if sex == 'Male' else 0
            restecg = ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"].index(restecg)
            slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
            thal = ["Normal", "Fixed defect", "Reversible defect"].index(thal) + 1
            cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
            fbs = 1 if fbs == 'Yes' else 0
            exang = 1 if exang == 'Yes' else 0
            ca = [0, 1, 2, 3].index(ca)
                     
            input_data = [int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs),
                int(restecg), int(thalach), int(exang), float(oldpeak), int(slope),
                int(ca), int(thal)]

            
            result = heart_attack_prediction(input_data)
            
        
            if result == 1:
                st.error("This patient has a huge probability of having a haert disease")
            else:
                st.success("This patient is healthy")
            
        
        except ValueError:
           st.error("Please enter valid numeric values for all input fields.")
        return

if __name__ == '__main__':
    main()
    
    
    
    
    
    