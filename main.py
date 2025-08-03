from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}!"}

