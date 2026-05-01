import streamlit as st
from PIL import Image
from med_logic import analyze_medicine

#1.Page setup
st.set_page_config(page_title="MedVision AI", page_icon="🩺", layout="centered")
st.title("🩺 MedVision AI")
st.subheader("Secure Pharmacological Identification Agent")
st.markdown("Take a clear photo of the medicine box or blister pack.")

#2.THE CAMERA WIDGET
camera_photo=st.camera_input("Capture Medicine Image 📸 ")

#3. ANALYZE BUTTON

if camera_photo is not None:
    image=Image.open(camera_photo)
    if st.button("Analyze Medicine Safely", type="primary"):
        with st.spinner("Analyzing pharmacological data and consulting guardrails..."):
            try:
                # Call the imported function
                result = analyze_medicine(image)
                
                st.success("Analysis Complete")
                st.markdown(result)
            except Exception as e:
                st.error(f"An error occurred with the AI connection: {e}")
