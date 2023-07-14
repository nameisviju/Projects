import streamlit as st
import pickle
import pandas as pd
import numpy as np
import math
pipe = pickle.load(open('venv/pipe1.pkl','rb'))
dataf = pickle.load(open('venv/dataf.pkl','rb'))
st.title("Mobile Price Predictor")
brand_name = st.selectbox("Brand",dataf['brand_name'].unique())
rating = st.number_input("Rating")
has_5g = st.selectbox('Has 5G',['Yes','No'])
has_nfc=st.selectbox("Has NFC",['Yes','No'])
has_ir_blaster=st.selectbox(" Has Ir Blaster",['Yes','No'])
processor_brand = st.selectbox("Processor brand",dataf['processor_brand'].unique())
num_cores=st.selectbox("core",['not specified','Quad Core','Hexa Core',"Octa Core"])
processor_speed=st.number_input("Processor speed")
battery_capacity=st.number_input("Battery Capacity")
fast_charging_available=st.selectbox("Fast Charging",['Yes','No'])
ram_capacity=st.selectbox("Ram",[1.0,2.0,3.0,4.0,6.0,8.0,12.0,16.0,18.0,64.0])
internal_memory=st.selectbox("Memory",[8.0,16.0,32.0,64.0,128.0,512.0,256.0,1024.0])
screen_size=st.number_input("Screen Size")
refresh_rate=st.selectbox("Refresh Rate",[60,90,120,144,165,240])
num_rear_camera=st.selectbox("Number of Rear Camera",['1','3','4'])
num_front_cameras=st.number_input("Number of Front Camera")
primary_front_camera=st.number_input("Primary Front Camera in MP")
primary_rear_camera=st.number_input("Primary Rear Camera in MP")
os=st.selectbox("OS",dataf['os'].unique())
resolution_height=st.number_input(" Resolution Height")
resolution_width=st.number_input("Resolution Width")

if st.button("predict price"):
    if has_5g=='Yes':
        has_5g=True
    else:
        has_5g=False
    if has_nfc=="Yes":
        has_nfc=True
    else:
        has_nfc=False
    if has_ir_blaster=="Yes":
        has_ir_blaster=True
    else:
        has_ir_blaster=False
    if fast_charging_available=="Yes":
        fast_charging_available=1
    else:
        fast_charging_available=0
    query=np.array([brand_name, rating, has_5g, has_nfc, has_ir_blaster,
       processor_brand, num_cores, processor_speed, battery_capacity,
       fast_charging_available, ram_capacity, internal_memory,
       screen_size, refresh_rate, num_rear_camera, num_front_cameras,
       primary_front_camera, primary_rear_camera, os,
       resolution_height, resolution_width])
    query=query.reshape(1,21)
    st.title(math.floor(int(np.exp((pipe.predict(query)[0])))))
