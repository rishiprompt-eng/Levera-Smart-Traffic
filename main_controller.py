import requests
import json
import time
from google import genai

# 1. SETUP: Your API Key
# Replace with your actual API key
client = genai.Client(api_key="YOUR_API_KEY_HERE")

# 2. MOCK DATA
mock_data = {
    "junction": "Hitech_City",
    "vehicle_count": 45,
    "weather": "Rainy",
    "ambulance_detected": True
}

# 3. AI LOGIC
prompt = f"Analyze: {json.dumps(mock_data)}. If 'ambulance_detected' is True, output 'ACTION: EMERGENCY_CLEAR'. Otherwise 'ACTION: ROUTINE'. Output only the action string."


def run_automation():
    print("🚀 Levera AI System Initialized...")

    # EXACT MODEL NAME FROM YOUR DISCOVERY SCAN
    active_model = "models/gemini-2.5-flash"

    config = {
        'safety_settings': [
            {'category': 'HARM_CATEGORY_HATE_SPEECH', 'threshold': 'BLOCK_NONE'},
            {'category': 'HARM_CATEGORY_HARASSMENT', 'threshold': 'BLOCK_NONE'},
            {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'threshold': 'BLOCK_NONE'},
            {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'threshold': 'BLOCK_NONE'}
        ]
    }

    try:
        # 4. BRAIN: Using 2.5 Flash
        response = client.models.generate_content(
            model=active_model,
            contents=prompt,
            config=config
        )

        ai_decision = response.text.strip()
        print(f"🧠 AI Decision: {ai_decision}")

        # 5. MUSCLE: Control the FastAPI Dashboard
        if "EMERGENCY_CLEAR" in ai_decision:
            payload = {"junction_id": "Hitech_City",
                       "action": "EMERGENCY_CLEAR"}
            res = requests.post("http://localhost:8000/control", json=payload)
            print(f"🚦 Hardware Response: {res.json()['message']}")
        else:
            print("🟢 Traffic flow is normal.")

    except Exception as e:
        print(f"❌ Execution Error: {e}")


if __name__ == "__main__":
    run_automation()
