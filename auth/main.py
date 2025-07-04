from fastapi import FastAPI, HTTPException, Request
import json, uuid, os

app = FastAPI()
DATA_DIR = "/data"
REQUESTS_DIR = os.path.join(DATA_DIR, "requests")
USERS_FILE = os.path.join(DATA_DIR, "users.json")

os.makedirs(REQUESTS_DIR, exist_ok=True)

@app.post("/register")
def register(req: dict):
    username = req["username"]
    password = req["password"]

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE) as f:
            users = json.load(f)
    else:
        users = []

    if any(u["username"] == username for u in users):
        raise HTTPException(status_code=400, detail="User exists")

    job_id = str(uuid.uuid4())
    with open(os.path.join(REQUESTS_DIR, f"{job_id}.json"), "w") as f:
        json.dump({"username": username, "password": password}, f)

    return {"status": "job created"}
