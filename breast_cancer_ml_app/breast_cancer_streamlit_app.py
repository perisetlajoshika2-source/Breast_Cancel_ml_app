import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("breast_cancer_model.pkl", "rb"))

st.title("Breast Cancer Prediction App")

radius_mean = st.number_input("Radius Mean")
texture_mean = st.number_input("Texture Mean")
perimeter_mean = st.number_input("Perimeter Mean")
area_mean = st.number_input("Area Mean")

if st.button("Predict"):

    st.success("Prediction Generated Successfully")