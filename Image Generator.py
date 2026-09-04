import streamlit as st
from diffusers import DiffusionPipeline

st.set_page_config(
    page_title="Image Generator",
    page_icon="🖼️"
)

st.title("🎨 Image Generator")

prompt = st.text_input(
    "Enter your prompt:",
    "lotus in water"
)

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        pipe = DiffusionPipeline.from_pretrained("nota-ai/bk-sdm-tiny")
        image = pipe(prompt).images[0]
        st.image(image, caption="Generated Image")