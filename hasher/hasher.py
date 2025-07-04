import os, json, bcrypt, time

DATA_DIR = "/data"
REQUESTS_DIR = os.path.join(DATA_DIR, "requests")
USERS_FILE = os.path.join(DATA_DIR, "users.json")

os.makedirs(REQUESTS_DIR, exist_ok=True)

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

while True:
    files = os.listdir(REQUESTS_DIR)
    for file in files:
        if not file.endswith(".json"):
            continue

        path = os.path.join(REQUESTS_DIR, file)
        with open(path) as f:
            data = json.load(f)

        username, password = data["username"], data["password"]
        hashed = hash_password(password)

        if os.path.exists(USERS_FILE):
            with open(USERS_FILE) as f:
                users = json.load(f)
        else:
            users = []

        users.append({"username": username, "password": hashed})
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=2)

        os.remove(path)
    time.sleep(2)
