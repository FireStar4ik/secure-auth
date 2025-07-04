from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <form action="/register" method="post">
        <input name="username" placeholder="Username"/>
        <input name="password" placeholder="Password" type="password"/>
        <button type="submit">Register</button>
    </form>
    """

@app.post("/register")
def register(username: str, password: str):
    response = requests.post("http://auth-service:8000/register", json={"username": username, "password": password})
    return {"result": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
