import streamlit as st
import numpy as np
from PIL import Image
import requests
import time


NGROK_SERVER = 'https://8e98-146-152-233-49.ngrok-free.app'

def analyseImage(imgNP):
    cnnModelPath = f"{NGROK_SERVER}/cnn/"
    imageInput = {
        "imageList": imgNP.tolist()
    }
    with st.spinner('Analysing Diseases...'):
        result = requests.post(cnnModelPath, json=imageInput)
        st.success("Done!")
    if(result.status_code == 200):
        disease = result.text
        st.write(f"Disease Detected: {disease}")
        st.markdown("<br /> <br />", unsafe_allow_html=True)
        getSymptoms(disease)
    else:
        st.write("An Error Occured! Try Again!")
    


def generate_text_slowly(text, speed=0.1):
    text_placeholder = st.empty()
    chunks = text.split()
    value = ""
    for chunk in chunks:
        if text_placeholder.empty():
            value += " " + chunk
        else:
            value += " " 
        text_placeholder.write(value)
        time.sleep(speed) 




def getSymptoms(diseaseClassified):
    llmModelPath = f"{NGROK_SERVER}/llm/" 
    diseaseClass = {
        "disease": diseaseClassified
    }
    with st.spinner(f'Suggesting Help for {diseaseClassified}'):
        res = requests.post(llmModelPath, json=diseaseClass)
        st.success("Done!")
    if(res.status_code == 200):
        resJSON = res.json()
        st.markdown("<br /> <br /> <br />", unsafe_allow_html=True)
        generate_text_slowly(resJSON['result'])
    else:
        st.write("An Error Occured! Try Again!")






def main():
    st.title("Skin Diseases Analysis Application")
    with st.form(key='image_form'):
        image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button(label='Analyse')

    if image is not None:
        image_pil = Image.open(image)
        st.image(image_pil, caption='Your uploaded Image', use_column_width=True)
        imageNP = np.array(image_pil, dtype=np.uint8)
        analyseImage(imageNP)

    


if __name__ == "__main__":
    main()






