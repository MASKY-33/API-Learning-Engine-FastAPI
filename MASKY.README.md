# API Learning Engine (FastAPI)
This project is designed purely to help you understand how APIs work, how FastAPI handles incoming internet data, and how different HTTP methods behave.
It introduces GET routes, POST routes, and dynamic path parameters.

# Purpose
The system acts as a simple training engine that shows how FastAPI receives data from the internet, processes it, and sends structured JSON responses back to the client.

## Features
- FastAPI application
- Multiple GET endpoints
- One POST endpoint
- Dynamic path parameters
- Clear demonstration of how data travels from the browser → API → Python function → JSON response

# Endpoints Overview
1. / — Home Port (GET)
Returns a welcome message.
Shows how FastAPI automatically converts Python dictionaries into JSON for the browser.

2. /status — System Status (GET)
Returns a small data package containing firewall and database status.
Demonstrates how GET routes deliver predefined information.

3. /incident/add — Add Incident (POST)
Accepts a string parameter event from the client.
Shows how POST routes receive data from outside and return a confirmation message.

4. /incident/{incident_id} — Specific Incident (GET)
Uses a dynamic path parameter.
Demonstrates how FastAPI extracts values directly from the URL and injects them into the function.


## Learning Purpose
This project teaches:
- How GET and POST routes work
- How FastAPI converts Python dicts into JSON
- How incoming data is captured through function parameters
- How dynamic URL segments (/{incident_id}) are read and used
- How APIs communicate with external clients (browsers, tools, scripts)
- It is a simple but effective module for getting API fundamentals into your fingers.
