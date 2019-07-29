"""Definition of all REST API endpoints of the license analysis module."""

import logging
import json
import requests
from src.stack_license import StackLicenseAnalyzer
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.config import Config
from src import config
from src.models import Packages

# Initialize fastapi
app = FastAPI()

# Add CORS origins if needed
origins = [
    "http://localhost:8000",
    "http:localhost",
    "http:localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Add application related config from file
app.Config = Config("config")

# Initialize Stack License Analyzer
app.stack_license_analyzer = StackLicenseAnalyzer()


@app.get('/api/v1/liveness')
def liveness():
    """Handle the REST API endpoint /."""
    print("RELOAD")
    return {"status": "ok"}


@app.post('/api/v1/stack_license')
def stack_license(payload: Packages):
    """Handle the REST API endpoint /api/v1/stack_license."""
    # input_json = request.get_json(force=True)
    # app.logger.debug("Stack analysis input: {}".format(input_json))
    input_json = json.loads(payload.json())
    response = app.stack_license_analyzer.compute_stack_license(payload=input_json)
    # app.logger.debug("Stack analysis output: {}".format(response))

    return response


if __name__ == "__main__":
    app.run()
