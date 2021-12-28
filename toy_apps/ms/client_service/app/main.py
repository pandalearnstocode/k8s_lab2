import streamlit as st
import requests
import json
import pandas as pd
import httpx
app_layer_url = 'http://web:8000/'
utils_layer_url = 'http://utils:8000/'

application_form = st.form(key='application-layer')
application_email = application_form.text_input('Enter your email')
application_password = application_form.text_input('Enter your password')
application_submit = application_form.form_submit_button('Submit')

if application_submit:
    login_data = {"email": application_email,"password":application_password}
    r = requests.post(app_layer_url + "login", data=json.dumps(login_data))
    st.write(f'hello {r.text}')

option = st.selectbox('How would you like to be contacted?', ('brazil', 'us', 'uk'))
download_data_form = st.form(key='data-layer')
download_data_submit = download_data_form.form_submit_button('Download')
if download_data_submit:
    r = httpx.get(utils_layer_url + f"generate_data/{option}")
    r = httpx.get(utils_layer_url + f"pull_data/{option}")
    data = r.json()
    raw_data = data['Data']
    # TODO: Fix the data parsing in a correct format in pandas
    df = pd.DataFrame.from_records(raw_data)
    st.write(df)