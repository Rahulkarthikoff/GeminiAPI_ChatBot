# import requests
# import streamlit as st

# API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
# headers = {"Authorization": "Bearer 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"}

# st.title("Image Captioning")

# def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
#     response = requests.post(API_URL, headers=headers, data=data)
#     return response.json()
# up_load = st.file_uploader("Upload an image",type="jpg")
# output = query(up_load)



###################################################################################################
import requests
import streamlit as st


st.title("Image - Captioning")

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(file):
    if file is not None:
        data = file.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
    else:
        return None

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload an image", type="jpg")

# Process the uploaded file
output = query(uploaded_file)

if output:
    st.subheader(output[0]['generated_text'])  # Display the caption output
else:
    st.write("No image uploaded")


#st.subheader(output[0]["generated_text"])