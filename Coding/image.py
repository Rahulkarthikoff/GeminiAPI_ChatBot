import requests
import streamlit as st
import base64
API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

st.title('Text-to-Image Bot')


import base64

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("dog1.jpg")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)





def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input('Enter a prompt:'),
})
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))



if st.button('Generate'):
	st.image(image)
