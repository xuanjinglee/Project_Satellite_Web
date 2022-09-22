import streamlit as st
import cv2
import numpy as np
import requests

'''
# Project Satellite Front
'''

st.markdown('''
Given a satellite/aerial imagery,

Generate an image that show given image segmented into numerous key elements.

(i.e. Building, Land, Road, Vegetation, Water and Others)
''')

uploaded_image = st.file_uploader(label="Choose an image to upload",
                                  type=['png', 'jpg'])

# def display_image(image):

if uploaded_image is not None:
    st.image(uploaded_image)

    # Call API to do prediction

    api_url = "https://segapi-tnfnn6u4nq-ew.a.run.app/upload_image"

    headers = {
        'accept': 'application/json',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }
    files = {
        'file': uploaded_image,
    }
    # response = requests.post('http://127.0.0.1:8000/upload', headers=headers, files=files)
    response = requests.post('https://segapi-tnfnn6u4nq-ew.a.run.app/upload_image', headers=headers, files=files)

    st.write(response.text)

    params = {
        'filename': f'transformed_{uploaded_image.name}',
    }
    response = requests.get('https://segapi-tnfnn6u4nq-ew.a.run.app/get_image', params=params, headers=headers)
    # from IPython.display import Image, display
    # display(Image(response.content))

    st.image(response.content)
