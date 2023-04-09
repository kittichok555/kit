from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

#st.header("การทำนายว่าคนที่เข้าร้านเป็นเพศ ชาย หรือ หญิง ") 
#st.image("./pic/banner.jpg")
#st.image("./pic/my.jpg")

dt = pd.read_csv("./data/CustomersRR.csv")
html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>การทำนายว่าคนที่เข้าร้านเป็นเพศ ชาย หรือ หญิง</h4></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

age=st.slider("กรุณาเลือกข้อมูล อายุ",0, 130, 25)
Income=st.number_input("กรุณาเลือกข้อมูล รายได้ต่อปี")
Score=st.slider("กรุณาเลือกข้อมูล คะแนนการใช้จ่าย",0, 100, 50)
Work=st.slider("กรุณาเลือกข้อมูล ทำงานมาแล้วกี่ปี",0, 50, 5)
Family_Size=st.slider("กรุณาเลือกข้อมูล ขนาดของครอบครัว",0, 20, 3)

if st.button("ทำนายผล"):
   
   X = dt.drop('Gender', axis=1)
   y = dt.Gender
   Knn_model = KNeighborsClassifier(n_neighbors=9)
   Knn_model.fit(X, y)   

   x_input = np.array([[age, Income, Score, Work,Family_Size]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 'Male':
    st.header("ชาย")
   elif out[0] == 'Female':
    st.header("หญิง")
   else:       
    st.header('xxx')    
    st.button("ไม่แสดงข้อมูล")
else:
   st.write("ไม่แสดงข้อมูล")