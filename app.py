import streamlit as st
# from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
import random
import seaborn as sb
from PIL import Image

st.set_page_config(
    page_title="Web Server Log Analysis",
    page_icon="📝",
    layout="wide",
    # initial_sidebar_state="expanded"
)

model1 = joblib.load('model_1')
model4 = joblib.load('model_4')
model2 = joblib.load('RandomForestClassifier')
model3 = joblib.load('AdaBoostClassifier')
model5 = joblib.load('XGBRFClassifier')
model6 = joblib.load('CatBoostClassifier')

df = pd.read_csv('third_result.csv')

ip = [i for i in df['Host']]
method = [i for i in df['Method']]
endpoint = [i for i in df['Endpoint']]
protocol = [i for i in df['Protocol']]
status_code = [i for i in df['Status Code']]
content_size = [i for i in df['Content Size']]
no_of_requests = [i for i in df['No of Requests']]

l1=[]
list1=[]

st.title('Web Server Log Analysis')

st.header('Data Analysis')

st.subheader('Frequency Distributions')

option = st.selectbox('Select the column name to know its frequency distributions',
    ('Protocol','Status Code','No of Requests'))

if st.button('Plot Charts'):
    d = df[option].value_counts().plot(kind='bar')
    st.pyplot(d.figure)

st.subheader('Unique Values')

option2 = st.selectbox('Select the column name to know the number of unique values in it',
    ('Host','Method','Endpoint','Protocol','Status Code','Content Size','No of Requests'))

if st.button('Number of Unique Values'):
    st.write(len(df[option2].unique()))

st.subheader('Correlation Matrix')

if st.button('Display Correlation Matrix'):
    dataplot = sb.heatmap(df.corr(), cmap="YlGnBu", annot=True)
    st.pyplot(dataplot.figure)

st.subheader('Outliers')

option3 = st.selectbox('Select the column name to graph the outliers in it',
    ('Host','Method','Endpoint','Protocol','Status Code','Content Size','No of Requests'))

if st.button('Boxplot the Column'):
    h = df.boxplot(column=[option3])
    st.pyplot(h.figure)

st.subheader('Kurtosis and Skew')

option4 = st.selectbox('Select the column name find kurtosis and skew',
    ('Host','Method','Endpoint','Protocol','Status Code','Content Size','No of Requests'))

if st.button('Find Kurtosis and Skew'):
    l = df[option4].plot(kind='density')
    st.pyplot(l.figure)
    st.write('This distribution has skew : ', df[option4].skew())
    st.write('This distribution has kurtosis : ', df[option4].kurt())

st.header('Data Processing')
st.markdown('#### Data Before Anomaly Detection')
df2 = pd.read_csv('logs_df.csv')
st.dataframe(df2)

st.markdown('#### Anomaly Detection using Pycaret')


image1 = Image.open('iforest.png')
image2 = Image.open('cluster.png')
image3 = Image.open('knn.png')

if st.button('IForest'):
    st.image(image1, caption='IForest')
if st.button('Cluster'):
    st.image(image2, caption='Cluster')
if st.button('KNN'):
    st.image(image3, caption='KNN')
else:
    st.write('')
st.markdown('##### The KNN model yielded the best results out of the three and was therefore selected as the main anomaly detection model.')

st.markdown('#### Data After Anomaly Detection')
st.dataframe(df)
    
st.header('Model Sandbox')

if st.checkbox('Select a Random IP Configuration to Test'):
    l1 = df.sample().values.flatten().tolist()
    st.write('IP Address Selected : ',l1[0])
    st.write('Method Selected : ',l1[3])
    st.write('Endpoint Selected : ',l1[4])
    st.write('Protocol Selected : ',l1[5])
    st.write('Status Code Selected : ',l1[6])
    st.write('Content Size Selected : ',l1[7])
    st.write('No of Requests Selected : ',l1[8])
    list1 = [l1[0], l1[3], l1[4], l1[5], l1[6], l1[7], l1[8]]
else:
    st.write('')
    

def predict(model, lists):

    data = pd.DataFrame({
        'Host': [lists[0]],
        'Method': [lists[1]],
        'Endpoint': [lists[2]],
        'Protocol': [lists[3]],
        'Status Code': [lists[4]],
        'Content Size': [lists[5]],
        'No of Requests': [lists[6]]
    })

    prediction = model.predict(data)

    return prediction

st.markdown('#### Prediction')
if st.button('Predict Using XGBoost Model'):
    prediction1 = predict(model1, list1)
    st.write('The predicted value using XGBoost Model is: ', prediction1[0])
    st.write('The original value for the given data is: ', l1[9])
    
if st.button('Predict using Gradient Boosting Model'):
    prediction2 = predict(model4, list1)
    st.write('The predicted value using Gradient Boosting Model is: ', prediction2[0])
    st.write('The original value for the given data is: ', l1[9])
if st.button('Predict using XGBoostRF Model'):
    prediction3 = predict(model5, list1)
    st.write('The predicted value using XGBoostRF Model is: ', prediction3[0])
    st.write('The original value for the given data is: ', l1[9])
if st.button('Predict using CATBoost Model'):
    prediction4 = predict(model6, list1)
    st.write('The predicted value using CATBoost Model is: ', prediction4[0])
    st.write('The original value for the given data is: ', l1[9])
if st.button('Predict using AdaBoost Model'):
    prediction5 = predict(model3, list1)
    st.write('The predicted value using AdaBoost Model is: ', prediction5[0])
    st.write('The original value for the given data is: ', l1[9])
if st.button('Predict using Random Forest Model'):
    prediction6 = predict(model6, list1)
    st.write('The predicted value using Random Forest Model is: ', prediction6[0])
    st.write('The original value for the given data is: ', l1[9])
else:
    st.write('')

st.header('Model Statistics')

image4 = Image.open('CatBoost.png')
image5 = Image.open('AdaBoost.png')
image6 = Image.open('Gradient Boost.png')
image7 = Image.open('RF.png')
image8 = Image.open('XGB.png')
image9 = Image.open('XGBRF.png')

st.subheader('CatBoost')
st.image(image4, caption='CatBoost')

st.subheader('AdaBoost')
st.image(image5, caption='AdaBoost')

st.subheader('Gradient Boosting')
st.image(image6, caption='Gradient Boosting')

st.subheader('RF')
st.image(image7, caption='Random Forest')

st.subheader('XGB')
st.image(image8, caption='XGB')

st.subheader('XGBRF')
st.image(image9, caption='XGBRF')