import streamlit as st
from PIL import Image
import io


def main():
    st.title("Skin Doctor")
    #Form to upload an image
    with st.form(key='image_form'):
        image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button(label='Analyse')

    if image is not None:
        image_bytes = image.read()
        st.image(Image.open(io.BytesIO(image_bytes)), caption='Uploaded Image', use_column_width=True)


if __name__ == "__main__":
    main()
