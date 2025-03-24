from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_data():
    df = pd.read_csv("/data/transactions.csv")
    return df.to_dict(orient="records")

@app.get("/api/transactions")
def get_transactions():
    df = pd.read_csv("/data/transactions.csv")
    return df.to_dict(orient="records")

@app.get("/api/customers")
def get_customers():
    return {"customers": [{"id": 1, "name": "Ahmed"}]}

@app.get("/api/externalData")
def get_external():
    return {"external": {"blacklist": ["IP123"]}}