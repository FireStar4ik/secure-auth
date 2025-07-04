from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

HTML_FORM = """
<form method="post">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <input type="submit">
</form>
"""

@app.get("/", response_class=HTMLResponse)
def form():
    return HTML_FORM

@app.post("/")
def submit(username: str = Form(...), password: str = Form(...)):
    response = requests.post("http://auth-service:8001/register", json={"username": username, "password": password})
    return {"message": response.json()}
