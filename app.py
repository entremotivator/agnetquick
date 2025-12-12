import streamlit as st
import requests

WEBHOOK_URL = "https://agentonline-u29564.vm.elestio.app/webhook/bbe644ab-agentflow"

st.title("Business Profile Questionnaire")

st.write("Please fill out the details below. Your responses will be sent to the automation webhook.")

with st.form("business_form"):
    st.subheader("Business Details")
    business_name = st.text_input("Business Name")
    business_goals = st.text_area("Business Goals")

    st.subheader("Contact Information")
    contact_name = st.text_input("Your Name")
    contact_email = st.text_input("Email")
    contact_phone = st.text_input("Phone Number")

    st.subheader("Online Presence")
    website = st.text_input("Website URL")

    st.subheader("Profiled Answers")
    target_audience = st.text_area("Target Audience")
    services_offered = st.text_area("Main Services or Products")
    brand_voice = st.text_area("Brand Voice / Style")
    competitors = st.text_area("Top Competitors (optional)")
    
    submitted = st.form_submit_button("Submit")

if submitted:
    data = {
        "business_name": business_name,
        "business_goals": business_goals,
        "contact_name": contact_name,
        "contact_email": contact_email,
        "contact_phone": contact_phone,
        "website": website,
        "profiled_answers": {
            "target_audience": target_audience,
            "services_offered": services_offered,
            "brand_voice": brand_voice,
            "competitors": competitors
        }
    }

    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 200:
            st.success("Your information has been sent successfully!")
        else:
            st.error(f"Webhook error: {response.status_code}")
    except Exception as e:
        st.error(f"Failed to send data: {e}")
