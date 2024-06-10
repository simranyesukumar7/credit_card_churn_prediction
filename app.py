#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pickle
import pandas as pd
import os
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_input = open("model.pkl","rb")
svc_model = pickle.load(pickle_input)
port = int(os.environ.get("PORT", 8000))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=["POST"])
def predict():
    input_feat = [x for x in request.form.values()]
    final_model_features = [np.array(input_feat)]
    preds = svc_model.predict(final_model_features)
    print(preds)
    return render_template('index.html', prediction_text = 'The Churn status of the customer is {}'.format(str(preds)))

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=port)


# In[ ]:




