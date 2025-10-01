#!/bin/bash

# Configuration pour Azure App Service
python -m uvicorn ApiRest:app --host 0.0.0.0 --port 8000
