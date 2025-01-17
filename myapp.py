
import streamlit as st 

st.write("Hello Fahmi Bang Khai") 
st.success("Good")
st.error("Fail")
st.warning("bad")
st.info("info")


new_title = '<p style="font-family:sans-serif;color:Green; font-size: 42px;">This is advanced font manipulation!</p>' 
st.markdown(new_title, unsafe_allow_html=True) 

st.selectbox("Kuala Lumpur is located at", ['Malaysia', 'Thailand', 'UK'])
st.multiselect("Select 2 states", ['Selangor','Johor','Kedah'])

st.button("Click Here to Proceed")
st.slider("Select the length of stay", 1,10, value=3)

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write("The current number is ", number)

from PIL import Image 
im = Image.open('cathuhh.gif')
st.image(im, width=300)

import pandas as pd
df = pd.read_excel('sampleData.xlsx')
st.dataframe(df)

#Bar Chart
st.bar_chart(df, x="Location", y="Income")
#Line Chart
st.line_chart(df, x="Household", y="Income")
#Scatter Chart
st.scatter_chart(df, x="Household", y="Income")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


col1, col2, col3 = st.columns(3)
with col1:
    st.header("Aliff")
    st.image("1.jpg")
with col2:
    st.header("Azrul")
    st.image("2.jpg")
with col3:
    st.header("Syakirin")
    st.image("3.jpg")


