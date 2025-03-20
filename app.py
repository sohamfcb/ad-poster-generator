import streamlit as st
from huggingface_hub import InferenceClient
import os
import pymysql
import pywhatkit as kit
from PIL import Image
import io
import time
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title='Advertisement Poster Generator')
st.title('Advertisement Poster Generator')

client = InferenceClient("stabilityai/stable-diffusion-xl-base-1.0", token=os.getenv('HF_TOKEN'))

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='fcbarcelonaxavi',
    database='visiting_card_details'
)

mycursor=conn.cursor()

mycursor.execute("SELECT phone FROM details;")
data=mycursor.fetchall()
phone_nos=[number[0].strip().replace(' ','') for number in data]

input_query=st.text_input('Describe your image:')

btn=st.button('Generate image')

if btn:
    image = client.text_to_image(input_query)
    st.image(image, caption='Generated Image')
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    with open(f'{input_query.split()[0]}.png', 'wb') as f:
        f.write(img_bytes.read())

    for number in phone_nos:
        kit.sendwhats_image(number,img_path=f"{input_query.split()[0]}.png")
        time.sleep(10)