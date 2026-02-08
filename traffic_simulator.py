from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Enable CORS so your Python scripts and Browser can communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. The Model: Current state of the junctions in Hyderabad
traffic_state = {
    "Hitech_City": {"status": "RED", "emergency": False},
    "Jubilee_Hills": {"status": "RED", "emergency": False}
}


class SignalUpdate(BaseModel):
    junction_id: str
    action: str

# 2. The View: Route to serve the HTML Dashboard


@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    try:
        with open("index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Error: index.html not found!</h1><p>Please ensure the HTML file is in the same folder.</p>"

# 3. Data Endpoint: Used by the Dashboard to get updates


@app.get("/status")
def get_status():
    return traffic_state

# 4. Control Endpoint: Used by the AI Controller (or n8n) to change lights


@app.post("/control")
async def control_traffic(data: SignalUpdate):
    if data.junction_id not in traffic_state:
        raise HTTPException(status_code=404, detail="Junction not found")

    if data.action == "EMERGENCY_CLEAR":
        traffic_state[data.junction_id]["status"] = "GREEN"
        traffic_state[data.junction_id]["emergency"] = True
        return {"message": f"🚨 EMERGENCY: {data.junction_id} cleared!"}

    # Reset logic for normal flow
    if data.action == "ROUTINE":
        traffic_state[data.junction_id]["status"] = "RED"
        traffic_state[data.junction_id]["emergency"] = False
        return {"message": "Routine flow restored."}

    return {"message": "Command processed"}

if __name__ == "__main__":
    # Binding to 0.0.0.0 is critical for local network access
    uvicorn.run(app, host="0.0.0.0", port=8000)
