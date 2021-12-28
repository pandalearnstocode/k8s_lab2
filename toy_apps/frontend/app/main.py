import streamlit as st
import requests
import json
url = 'http://web:8000/login'

application_form = st.form(key='application-layer')
application_email = application_form.text_input('Enter your email')
application_password = application_form.text_input('Enter your password')
application_submit = application_form.form_submit_button('Submit')

if application_submit:
    login_data = {"email": application_email,"password":application_password}
    r = requests.post(url, data=json.dumps(login_data))
    st.write(f'hello {r.text}')


option = st.selectbox('How would you like to be contacted?', ('brazil', 'us', 'uk'))
st.write('You selected:', option)