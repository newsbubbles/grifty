"""
fastapi_app.py

A minimal FastAPI application to expose Grifty functionalities as an API.
"""
from fastapi import FastAPI
from ceo_agent import CEOAgent

app = FastAPI()
ceo = CEOAgent()

@app.get("/")
def read_root():
    return {"message": "Welcome to Grifty - The AI CEO API"}

@app.get("/pitch")
def create_pitch(product: str, audience: str):
    return {"pitch": ceo.create_pitch(product, audience)}

@app.get("/do_ceo_things")
def do_ceo_things():
    return ceo.do_ceo_things()
