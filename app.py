import streamlit as st
import pickle
import numpy as np

st.title('🐱‍🚀 Delhi NCR House Price Predictor')

st.info('This is a Random FOrest Maching Learning App.')

df = pickle.load(open('df.pkl','rb'))
model = pickle.load(open('RF.pkl','rb'))

area = st.number_input('Area sqft')
bedroom = st.selectbox('Bedrooms', df['Bedrooms'].unique())
bathroom = st.selectbox('Bathrooms', df['Bathrooms'].unique())
building = st.selectbox('Type of building', df['type_of_building'].unique())
status = st.selectbox('Status',df['Status'].unique())
neworold = st.selectbox('New or Old Property',df['neworold'].unique())


if st.button('Predict Price'):

    if status == 'Under Construction':
        status = 1
    else:
        status = 0

    if building == "Individual House":
        building = 1
    else:
        building = 0

    if neworold == "Resale":
        neworold = 1
    else:
        neworold = 0
    
    query = np.array([area,bedroom,bathroom,status,building,neworold])
    query = query.reshape(1,6)
    st.title("The predicted price for the selected house is ₹"+str(int(model.predict(query))))















