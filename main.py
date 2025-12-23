from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello, World!"}

@app.get("/healthz")
async def health():
    return {"status": "Healthy"}
