import streamlit as st
import pickle
import numpy as np
with open('model_saving.pkl','rb')as file:
    model=pickle.load(file)

st.title("HOUSE PRICE PREDICTION")
st.write("Enter the following data")
SF=st.number_input("Square_Footage",value=0)
NB=st.number_input("Num_Bedrooms",value=0)
NBR=st.number_input("Num_Bathrooms",value=0)
YB=st.number_input("Year_Built",value=0)
GS=st.selectbox("Garage_Size",[0,1])
if st.button("predict the price"):
    Input=np.array([[SF,NB,NBR,YB,GS]])
    prediction=model.predict(Input)
    st.success(f'{prediction[0]:,.2f} $')