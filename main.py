from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins and GET methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from JSON file and convert to dict
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json") 
with open(file_path) as f:
    data = json.load(f)
    STUDENT_MARKS = {item["name"]: item["marks"] for item in data}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [STUDENT_MARKS.get(n, 0) for n in names]
    return JSONResponse(content={"marks": marks})