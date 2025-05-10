# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle 
import numpy as np


#load_file = pickle.load(open('C:\Users\LENOVO\Desktop\Exercism\MachineLearning\MLModel\trained_model.sav', 'rb'))

load_model = pickle.load(open('C:/Users/LENOVO/Desktop/Exercism/MachineLearning/MLModel/trained_model.sav', 'rb'))

lr_model, std = load_model

input_data = [63,1,3,145,233,1,0	,150, 0	,2.3	,0	,0	,1	]

input_np_arr = np.array(input_data)

input_data = input_np_arr.reshape(1,-1)

model_result = lr_model.predict(input_data)[0]

if model_result == 1:
  print("This patient has heart problem")
else:
  print("This pratient is healthy")