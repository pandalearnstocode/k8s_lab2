import streamlit as st
import httpx


application_form = st.form(key='application-layer')
application_name = application_form.text_input('Enter your name')
application_submit = application_form.form_submit_button('Submit')

st.write('Application Layer Communication Test:')

if application_submit:
    r = httpx.get('http://hello.world/applicationlayer/app')
    st.write(f'hello {r.text}')


data_form = st.form(key='data-layer')
data_name = data_form.text_input('Enter your name')
data_submit = data_form.form_submit_button('Submit')

st.write('Data Layer Communication Test:')

if data_form:
    r = httpx.get('http://hello.world/datalayer/app')
    st.write(f'hello {r.text}')

ml_form = st.form(key='ml-layer')
ml_name = ml_form.text_input('Enter your name')
ml_submit = ml_form.form_submit_button('Submit')

st.write('ML Layer Communication Test:')

if ml_submit:
    r = httpx.get('http://hello.world/mllayer/app')
    st.write(f'hello {r.text}')



optimization_form = st.form(key='optimization-layer')
optimization_name = optimization_form.text_input('Enter your name')
optimization_form = optimization_form.form_submit_button('Submit')

st.write('Optimization Layer Communication Test:')

if optimization_form:
    r = httpx.get('http://hello.world/optimizationlayer/app')
    st.write(f'hello {r.text}')


utility_form = st.form(key='utility-layer')
utility_name = utility_form.text_input('Enter your name')
utility_form = utility_form.form_submit_button('Submit')

st.write('Utility Layer Communication Test:')

if utility_form:
    r = httpx.get('http://hello.world/utilitylayer/app')
    st.write(f'hello {r.text}')