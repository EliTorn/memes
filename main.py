import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
st.title("My Memes Project 📝")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


def download_image():
    # Convert PIL Image to bytes
    modified_image_bytes = BytesIO()
    image.save(modified_image_bytes, format="JPEG")  # Change format as needed

    # Use st.download_button from the st object
    st.download_button(label="Download image",
                       data=modified_image_bytes.getvalue(),
                       file_name="Memes.jpeg",
                       mime="image/jpeg")


if uploaded_file:
    st.image(uploaded_file)
    # Open the image
    image = Image.open(BytesIO(uploaded_file.read()))
    text_size = st.number_input("Enter the size text", 10)
    font = ImageFont.load_default(text_size)
    # Create a drawing object
    draw = ImageDraw.Draw(image)

    text = st.text_input("Enter your text", "Text")
    x = st.number_input("X ", 0)
    y = st.number_input("Y ", 0)
    color = st.text_input("Enter your color :", "red")

    # Add text to the image
    draw.text((x, y), text, font=font, fill=color)

    # Display the image in Streamlit
    st.image(image, caption='Image with Text', use_column_width=True)
    download_image()
