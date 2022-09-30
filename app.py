from distutils.command.upload import upload
import streamlit as st
import requests

'''
# Building Detection &  Semantic Segmentation with Satellite Imagery

'''
st.markdown("***")
st.subheader('''
Given a satellite/aerial imagery, generate a new image, that shows the given imagery, segmented into various elements.
''')
st.subheader("(i.e. Building, Land, Road, Vegetation, Water and Others)")
st.subheader("Example:")

api_url = "https://seg-api2-tnfnn6u4nq-ew.a.run.app/"

headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

@st.cache
def upload_image(file):
    '''Upload image to API'''
    files = {
        'file': file,
    }
    response = requests.post(api_url + 'upload_image', headers=headers, files=files)
    return response.text

@st.cache
def get_image(file_name):
    ''' Get Image from API'''
    params = {
            'filename': file_name,
        }
    response = requests.get(api_url +'get_image', params=params, headers=headers)
    image = response.content
    return image

sample_img = get_image("sample_prediction.png") #change to sample_prediction.png
st.image(sample_img)

uploaded_image = st.file_uploader(label="Choose an image to upload",
                                  type=['png', 'jpg'])

if uploaded_image is not None:
    st.image(uploaded_image)

    # Upload image to API to do prediction
    response_message = upload_image(uploaded_image)

    if response_message == f'{{"message":"Successfully uploaded {uploaded_image.name}"}}':
        st.success(f'Successfully uploaded {uploaded_image.name}')

    # api_url = "https://sigapi-tnfnn6u4nq-ew.a.run.app/"

    # headers = {
    #     'accept': 'application/json',
    #     # requests won't add a boundary if this header is set when you pass files=
    #     # 'Content-Type': 'multipart/form-data',
    # }
    # files = {
    #     'file': uploaded_image,
    # }
    # # response = requests.post('http://127.0.0.1:8000/upload', headers=headers, files=files)
    # response = requests.post(api_url + 'upload_image', headers=headers, files=files)

    # if response.text == f'{{"message":"Successfully uploaded {uploaded_image.name}"}}':
    #     st.success(f'Successfully uploaded {uploaded_image.name}')
    pred_multi_class = get_image(f"t1_{uploaded_image.name}")
    pred_building_1 = get_image(f"t2_{uploaded_image.name}")
    pred_building_2 = get_image(f"t3_{uploaded_image.name}")

    selected = st.radio("Choose a Model to preview result:",
                        ["Multi-Class Segmentation",
                         "Building Detection Model 1 (Less accurate but accepts inputs of different dimensions)",
                         "Building Detection Model 2 (More accurate but only accepts inputs of 1024 x 1024 pixels)",
                         "All 3 Models"])

    if selected == "Multi-Class Segmentation":
        # pred_multi_class = get_image(f"t1_{uploaded_image.name}")

        st.image(pred_multi_class)
        st.caption("<h2 style='text-align: center; color: black;'>Multi-Class Segmentation</h2>", unsafe_allow_html=True)
        st.caption("<h3 style='text-align: center; color: black;'>Building, Land, Road, Vegetation, Water and Others</h3>", unsafe_allow_html=True)

        if uploaded_image.name == "hurricane-harvey_00000017_pre_disaster.png":
            st.write("")
            st.caption("<h3 style='text-align: center; color: black;'>Blue = Buildings</h3>", unsafe_allow_html=True)
            st.caption("<h3 style='text-align: center; color: black;'>Lawn Green = Vegetation</h3>", unsafe_allow_html=True)
            st.caption("<h3 style='text-align: center; color: black;'>Teal = Land</h3>", unsafe_allow_html=True)

        if uploaded_image.name == "hurricane-michael_00000511_pre_disaster.png":
            st.write("")
            st.caption("<h3 style='text-align: center; color: black;'>Blue = Buildings</h3>", unsafe_allow_html=True)
            st.caption("<h3 style='text-align: center; color: black;'>Yellow = Vegetation</h3>", unsafe_allow_html=True)
            st.caption("<h3 style='text-align: center; color: black;'>Lawn Green = Land</h3>", unsafe_allow_html=True)

        if uploaded_image.name == "hurricane-michael_00000482_pre_disaster.png":
            st.write("")
            st.caption("<h3 style='text-align: center; color: black;'>Blue = Buildings</h3>", unsafe_allow_html=True)
            st.caption("<h3 style='text-align: center; color: black;'>Yellow = Vegetation</h3>", unsafe_allow_html=True)
            st.caption("<h3 style='text-align: center; color: black;'>Lawn Green = Land</h3>", unsafe_allow_html=True)

    elif selected == "Building Detection Model 1 (Less accurate but accepts inputs of different dimensions)":
        # pred_building_1 = get_image(f"t2_{uploaded_image.name}")

        st.image(pred_building_1)
        st.caption("<h2 style='text-align: center; color: black;'>Building Detection Model 1</h2>", unsafe_allow_html=True)
        st.caption("<h3 style='text-align: center; color: black;'>Buildings Only</h3>", unsafe_allow_html=True)
        st.write("")
        st.caption("<h3 style='text-align: center; color: black;'>White = Buildings</h3>", unsafe_allow_html=True)
        st.caption("<h3 style='text-align: center; color: black;'>Black = Non-Buildings</h3>", unsafe_allow_html=True)

    elif selected == "Building Detection Model 2 (More accurate but only accepts inputs of 1024 x 1024 pixels)":
        # pred_building_2 = get_image(f"t3_{uploaded_image.name}")
        inner_col1, inner_col2, inner_col3 = st.columns([5, 10, 5])

        with inner_col2:
            st.write("")
            st.image(pred_building_2, width=350)
            st.caption("<h2 style='text-align: center; color: black;'>Building Detection Model 2</h2>", unsafe_allow_html=True)
            st.caption("<h3 style='text-align: center; color: black;'>Buildings Only</h3>", unsafe_allow_html=True)
            st.write("")
            st.caption("<h3 style='text-align: center; color: black;'>White = Buildings</h3>", unsafe_allow_html=True)
            st.caption("<h3 style='text-align: center; color: black;'>Black = Non-Buildings</h3>", unsafe_allow_html=True)

    else:
        col1, col2, col3, col4 = st.columns([10, 10, 2, 10])

        with col1:
            # pred_multi_class = get_image(f"t1_{uploaded_image.name}")

            st.image(pred_multi_class)
            st.caption("<h4 style='text-align: center; color: black;'>Multi-Class Segmentation</h4>", unsafe_allow_html=True)
            st.caption("<h4 style='text-align: center; color: black;'>Building, Land, Road, Vegetation, Water and Others</h4>", unsafe_allow_html=True)

        with col2:
            # pred_building_1 = get_image(f"t2_{uploaded_image.name}")

            st.image(pred_building_1)
            st.caption("<h4 style='text-align: center; color: black;'>Building Detection Model 1</h4>", unsafe_allow_html=True)
            st.caption("<h4 style='text-align: center; color: black;'>Buildings Only</h4>", unsafe_allow_html=True)

        with col4:
            # pred_building_2 = get_image(f"t3_{uploaded_image.name}")

            st.write("")
            st.image(pred_building_2, width=120)
            st.write("")
            st.caption("<h4 style='text-align: center; color: black;'>Building Detection Model 2</h4>", unsafe_allow_html=True)
            st.caption("<h4 style='text-align: center; color: black;'>Buildings Only</h4>", unsafe_allow_html=True)


        # with col4:
        #     pred_building_3 = get_image(f"t4_{uploaded_image.name}")

        #     st.image(pred_building_3)
        #     st.caption("<h4 style='text-align: center; color: black;'>Building Detection Model 3</h4>", unsafe_allow_html=True)
        #     st.caption("<h4 style='text-align: center; color: black;'>Buildings Only</h4>", unsafe_allow_html=True)

    # col1, col2 = st.columns(2)

    # with col1:
    #     params = {
    #         'filename': f't1_{uploaded_image.name}',
    #     }
    #     response = requests.get(api_url +'get_image', params=params, headers=headers)

    #     # if response.status_code != 200:
    #     #     params = {'filename': "owl.jpg",}
    #     #     response = requests.get(api_url +'get_image', params=params, headers=headers)

    #     st.image(response.content)
    #     st.caption("<h4 style='text-align: center; color: black;'>Model 1</h4>", unsafe_allow_html=True)
    #     st.caption("<h4 style='text-align: center; color: black;'>Building, Land, Road, Vegetation, Water and Others</h4>", unsafe_allow_html=True)


    # with col2:
    #     params = {
    #         'filename': f't2_{uploaded_image.name}',
    #     }
    #     response = requests.get(api_url +'get_image', params=params, headers=headers)
    #     # from IPython.display import Image, display
    #     # display(Image(response.content))

    #     st.image(response.content)
    #     st.caption("<h4 style='text-align: center; color: black;'>Model 2</h4>", unsafe_allow_html=True)
    #     st.caption("<h4 style='text-align: center; color: black;'>Buildings only</h4>", unsafe_allow_html=True)

    # with col3:
    #     params = {
    #         'filename': f't3_{uploaded_image.name}',
    #     }
    #     response = requests.get(api_url +'get_image', params=params, headers=headers)
    #     # from IPython.display import Image, display
    #     # display(Image(response.content))

    #     if response.status_code != 200:
    #         st.error("Model can only take images that are 1024 by 1024 pixels.")
    #     #     params = {'filename': "owl.jpg",}
    #     #     response = requests.get(api_url +'get_image', params=params, headers=headers)

    #     st.image(response.content)
    #     st.caption("<h4 style='text-align: center; color: grey;'>Buildings only</h4>", unsafe_allow_html=True)

    # with col4:
    #     params = {
    #         'filename': f't4_{uploaded_image.name}',
    #     }
    #     response = requests.get(api_url +'get_image', params=params, headers=headers)
    #     # from IPython.display import Image, display
    #     # display(Image(response.content))

    #     if response.status_code != 200:
    #         st.error("Model can only take images that are 1024 by 1024 pixels.")
    #     #     params = {'filename': "owl.jpg",}
    #     #     response = requests.get(api_url +'get_image', params=params, headers=headers)

    #     st.image(response.content)
    #     st.caption("<h4 style='text-align: center; color: grey;'>Buildings only</h4>", unsafe_allow_html=True)
