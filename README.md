 Levera: AI-Powered Smart City Traffic Manager

This project uses Gemini 2.5 Flash and FastAPI to prioritize emergency vehicles in real-time. It is designed to modernize urban infrastructure by shifting from static timers to dynamic, AI-driven traffic control.

 🏗️ Technical Architecture

The Levera system follows a Modular Microservices pattern to ensure high availability and low-latency response times for smart city infrastructure.

 Core Components:
1. AI Reasoning Engine (Gemini 2.5 Flash): Processes raw sensor data (JSON) to make real-time traffic decisions.
2. Middleware Controller (Python): Handles API rate limiting with Exponential Backoff and manages safety guardrails.
3. Simulation Backend (FastAPI): A RESTful API that simulates the physical traffic light hardware.
4. Real-time Dashboard (HTML/JS): A visual representation of the traffic junction status.

 Key Features:
 Resilient Connectivity: Implements automatic retries for API 429 (Rate Limit) errors.
 Safety Optimized: Utilizes custom HarmCategory configurations to ensure the AI never refuses an emergency command.
 Scalable Logic: Designed to easily integrate with real-world IoT sensors in Hyderabad.




 🚀 Setup & Installation

 1. Prerequisites
 Python 3.9+
 A Google Gemini API Key

 2. Installation
```bash
 Clone the repository
git clone [https://github.com/rishiprompt-eng/Levera-Smart-Traffic.git](https://github.com/rishiprompt-eng/Levera-Smart-Traffic.git)
cd Levera-Smart-Traffic

 Install dependencies
pip install -r requirements.txt
