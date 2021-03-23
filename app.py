import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

st.title("IRIS DATA")
st.text_input("USER NAME")
uploaded_file = st.file_uploader("upload file")
button = st.button("submit")
if button == True:
    df= pd.read_csv(uploaded_file)
    st.write(df)
    st.markdown("output 1")
    st.write(df.head())
    fig = plt.figure()
    plt.scatter(df['sepal.length'],df['petal.length'])
    st.write(fig)

# st.markdown("output 2")
# x = alt.Chart(df).mark_point(color = 'g').encode(
#           x = 'petal.length',
#           y = 'sepal.length')
# st.write(x)
