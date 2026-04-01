# Execute this file before invoking streamlit app
# <venv>/Scripts/activate
# <venv>>> python main.py # this script
#
# In another window
# setup same VENV
# streamlit run app.py  # start APP - must run 'python main.py' to start Fast Serve

# Your entry point for testing the Agentic Flow.
# import sys
# sys.path.append(".")
import os

# packages to load .env file
from dotenv import load_dotenv
from pathlib import Path
try:
	load_dotenv(Path('../'))
except:
	load_dotenv()
final:
	print(f"ENV file '.env' not found")

#### FastAPI ####
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# Assuming ShadowAuditor is in a file named auditor_logic.py
from .auditor_logic import ShadowAuditor 

app = FastAPI(title="Shadow Auditor API")

# Initialize auditor
API_KEY = os.getenv("ABUSEIPDB_KEY", "your_default_key")
auditor = ShadowAuditor(API_KEY, "Strict Security Policy")

class AuditRequest(BaseModel):
    worker_id: str
    thought: str
    action: str

@app.post("/audit")
async def perform_audit(request: AuditRequest):
    try:
        result = auditor.audit_step(request.worker_id, request.thought, request.action)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

