import streamlit as st
import pickle
import numpy as np

# Load the saved Linear Regression model
with open('pickle.sav', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict EMISSION using the loaded model
def predict_yeild(PRODUCTION,AREA):
    features = np.array([PRODUCTION,AREA])
    features = features.reshape(1,-1)
    yeild = model.predict(features)
    return yeild[0]

# Streamlit UI
st.title('Rice Prediction')
st.write("""
## Input Features
Enter the values for the input features to predict the Yeild Of TamilNadu Rice Prediction.
""")

# Input fields for user 
PRODUCTION = st.number_input('PRODUCTION')
AREA = st.number_input('AREA')


# Prediction button
if st.button('Predict'):

    yield_prediction = predict_yeild(PRODUCTION,AREA)
    st.write(f"YEILD OF Rice: {yield_prediction}")