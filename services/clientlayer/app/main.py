import streamlit as st
import httpx

st.write("Hello World")
st.balloons()

form = st.form(key='application-layer')
name = form.text_input('Enter your name')
submit = form.form_submit_button('Submit')

st.write('Press submit to have your name printed below')

if submit:
    r = httpx.get('http://hello.world/applicationlayer/app')
    st.write(f'hello {r.text}')

