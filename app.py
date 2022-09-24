import streamlit as st
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

    api_url = "https://sigapi-tnfnn6u4nq-ew.a.run.app/"

    headers = {
        'accept': 'application/json',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }
    files = {
        'file': uploaded_image,
    }
    # response = requests.post('http://127.0.0.1:8000/upload', headers=headers, files=files)
    response = requests.post(api_url + 'upload_image', headers=headers, files=files)

    if response.text == f'{{"message":"Successfully uploaded {uploaded_image.name}"}}':
        st.success(f'Successfully uploaded {uploaded_image.name}')


    col1, col2 = st.columns(2)

    with col1:
        params = {
            'filename': f't1_{uploaded_image.name}',
        }
        response = requests.get(api_url +'get_image', params=params, headers=headers)
        # from IPython.display import Image, display
        # display(Image(response.content))

        # if response.status_code != 200:
        #     params = {'filename': "owl.jpg",}
        #     response = requests.get(api_url +'get_image', params=params, headers=headers)

        st.image(response.content)
        st.caption("<h4 style='text-align: center; color: grey;'>Building, Land, Road, Vegetation, Water and Others</h4>", unsafe_allow_html=True)

    with col2:
        params = {
            'filename': f't2_{uploaded_image.name}',
        }
        response = requests.get(api_url +'get_image', params=params, headers=headers)
        # from IPython.display import Image, display
        # display(Image(response.content))

        st.image(response.content)
        st.caption("<h4 style='text-align: center; color: grey;'>Buildings only</h4>", unsafe_allow_html=True)
