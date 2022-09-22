from distutils.command.upload import upload
import streamlit as st
import cv2
import requests

'''
# Project Satellite Front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

uploaded_image = st.file_uploader(label="Choose an image to upload",
                                  type=['png', 'jpg'])

if uploaded_image is not None:
    st.image(uploaded_image)

# Function to preprocess image
def preprocess(image):
    pass

# Call API to do prediction

api_url = "https://segapi-tnfnn6u4nq-ew.a.run.app/get_image"

params = dict(
    filename=uploaded_image
)

response = requests.get(api_url, params=params)

prediction = response.json()
file_name = st.text_input('Save file as:', 'E.g. img102_label.png ')
# Button to download predicted label

if uploaded_image is not None and prediction is not None:
    file_name = st.text_input('Save file as:', 'E.g. img102_label.png ')

    with open(uploaded_image, "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="flower.png",
                mime="image/png"
            )
