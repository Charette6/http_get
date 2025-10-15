import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()
clientid = "teeest"
api_key = "u12344m5n5n12l3l5"

username = "zandyz"
# Fetch API key from environment variables
@app.get("/")
async def read_root():
  return {"Message": "Hello"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
