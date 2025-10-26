import streamlit as st
from PIL import Image
import requests
import io

st.set_page_config(page_title="SEGP WebApp Prototype 1")
st.title("📸 SEGP WebApp Prototype 1")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Option to send to backend
    if st.button("Send to AI Model"):
        st.write("🔄 Sending image to cloud backend...")

        # Simulated backend endpoint (replace later)
        backend_url = "https://segp-backend.onrender.com/predict"

        try:
            response = requests.post(
                backend_url,
                files={"file": uploaded_file.getvalue()},
                timeout=10
            )
            if response.status_code == 200:
                result = response.json()
                st.success("✅ AI Response Received!")
                st.json(result)
            else:
                st.error(f"❌ Backend returned {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.warning("⚠️ Backend not available (simulation mode)")
            st.info("Pretending we got a fake prediction:")
            st.json({"label": "banana", "confidence": 0.94})
