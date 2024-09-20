import streamlit as st
import requests

st.title("Phishing URL Detection")

url = st.text_input("Enter URL:")

if st.button("Predict"):
    if url:
        response = requests.post("http://api:8000/predict", json={"url": url})
        
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            
            if prediction == 1:
                st.write("⚠️ This is a phishing URL!")
            else:
                st.write("✅ This is a safe URL.")
        else:
            st.write("Error: Unable to get a prediction. Please check the URL or try again later.")
    else:
        st.write("Please enter a valid URL.")
