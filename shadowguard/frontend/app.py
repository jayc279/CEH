# Your entry point for testing the Agentic Flow.
# import sys
# sys.path.append(".")
from cysec_funcs.audit import ShadowAuditor
import os

import streamlit as st
import requests

st.set_page_config(page_title="Shadow Auditor Dashboard", layout="centered")

st.title("Shadow Auditor")
st.subheader("Simulate and Audit Worker Actions")

with st.form("audit_form"):
    worker_id = st.text_input("Worker ID", value="Worker-01")
    thought = st.text_area("Thought/Intent", value="I need to perform maintenance.")
    action = st.text_area("Action/Command", value="curl http://Y0dsbmJHeGxNREl1TUM0d0xqRXVNUzR3TGpFL2IzQjFjR2xr")
    
    submit = st.form_submit_button("Run Audit")

if submit:
    payload = {
        "worker_id": worker_id,
        "thought": thought,
        "action": action
    }
    
    with st.spinner("Analyzing step..."):
        try:
            # Point this to your FastAPI URL
            response = requests.post("http://localhost:8000/audit", json=payload)
            response.raise_for_status()
            result = response.json()
            
            # Display Results
            status = result.get("status", "Unknown")
            if status == "Safe":
                st.success(f"Audit Result: {status}")
            else:
                st.error(f"Audit Result: {status}")
                
            if "reason" in result:
                st.info(f"**Reason:** {result['reason']}")
                
            st.json(result) # Show full raw data
            
        except requests.exceptions.ConnectionError:
            st.warning("Could not connect to FastAPI. Is the backend running?")
        except Exception as e:
            st.error(f"An error occurred: {e}")


