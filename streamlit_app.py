# streamlit_app.py

import streamlit as st
import requests

st.title("🪪 ID Card Processor")
st.write("Upload an identity card image to extract structured data using Gemini AI.")

uploaded_file = st.file_uploader("Upload an ID card image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Process with Gemini"):
        with st.spinner("Processing..."):
            try:
                response = requests.post(
                    "http://localhost:8000/process-id/",
                    files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)},
                )
                if response.status_code == 200:
                    st.success("✅ Data extracted successfully!")
                    st.json(response.json())
                else:
                    st.error(f"❌ Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
