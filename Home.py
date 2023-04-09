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

html_8 = """
<div style="background-color:#1FFF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4 style="color: #FF0000">การทำนายว่าคนที่เข้าร้านเป็นเพศ ชาย หรือ หญิง</h4></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

dt = pd.read_csv("./data/CustomersRR.csv")
st.write(dt.head(10))

dt1 = dt['Age'].sum()
dt2 = dt['Income '].sum()
dt3 = dt['Spending_Score '].sum()
dt4 = dt['Work_Experience'].sum()
dt5 = dt['Family_Size'].sum()

dx = [dt1, dt2, dt3, dt4, dt5]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4", "d5"])
if st.button("แสดงการจินตทัศน์ข้อมูล"):
    #st.write(dt.head(10))
    st.bar_chart(dx2)
    st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>ทำนายข้อมูล</h4></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

age=st.number_input("กรุณาเลือกข้อมูล อายุ")
Income=st.number_input("กรุณาเลือกข้อมูล รายได้ต่อปี")
Score=st.slider("กรุณาเลือกข้อมูล คะแนนการใช้จ่าย")
Work=st.number_input("กรุณาเลือกข้อมูล ทำงานมาแล้วกี่ปี")
Family_Size=st.number_input("กรุณาเลือกข้อมูล ขนาดของครอบครัว")

if st.button("ทำนายผล"):
   
   X = dt.drop('Gender', axis=1)
   y = dt.Gender
   Knn_model = KNeighborsClassifier(n_neighbors=9)
   Knn_model.fit(X, y)   

   x_input = np.array([[age, Income, Score, Work,Family_Size]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 'Male':
    st.write("ชาย")
   elif out[0] == 'Female':
    st.write("หญิง")
   else:       
    st.writ('xxx')    
    st.button("ไม่แสดงข้อมูล")
else:
   st.write("ไม่แสดงข้อมูล")