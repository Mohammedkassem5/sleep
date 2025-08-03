import pandas as pd 
import numpy as np 
import plotly.express as px 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 

df =pd.read_csv("sleep.csv")
print(df.head())
df['Sleep Disorder']=df['Sleep Disorder'].replace(np.nan,"Normal")

st.sidebar.header("Sleep dashboard")
st.sidebar.image("download.png")
st.sidebar.write("the purpose of dashbpard")

cat_filter=st.sidebar.selectbox('filters',['Gender','Occupation','BMI Category',None])


a1, a2, a3, a4 = st.columns(4)
a1.metric("Avg age", round(df['Age'].mean(), 2))
a2.metric("Count of ID", round(df["Person ID"].count(), 0))
a3.metric("Max daily steps", round(df["Daily Steps"].max(), 0))
a4.metric("Avg Sleep Duration", round(df["Sleep Duration"].mean(), 0))
st.subheader("Quality of Sleep vs Stress Level")
fig=px.scatter(data_frame=df,x="Stress Level",y="Quality of Sleep",color=cat_filter,size="Quality of Sleep")
st.plotly_chart(fig,use_container_width=True)

# Add vertical space ABOVE columns
st.write("")  # 1 empty line
st.write("")  # 2 empty lines (adjust count for more space)

# Create 3 columns: c1, spacer, c2
c1, spacer, c2 = st.columns([4, 0.5, 3])

with c1:
    st.text('Occupation VS Avg Sleep Duration (Sorted)')
    avg_sleep_by_occ = df.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=False).reset_index()
    fig1 = px.bar(data_frame=avg_sleep_by_occ, x='Occupation', y='Sleep Duration')
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.text('Gender VS Quality of Sleep')
    gender_sleep = df.groupby('Gender')['Quality of Sleep'].mean().reset_index()
    fig2 = px.pie(gender_sleep, names='Gender', values='Quality of Sleep')
    st.plotly_chart(fig2, use_container_width=True)

# Add vertical space BELOW columns
st.write("")  # 1 empty line
st.write("")  # 2 empty lines (add more for bigger space)

st.subheader("Pair Plot & Heatmap for Numerical Features")