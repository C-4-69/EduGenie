from fastapi import FastAPI

app = FastAPI(title="EduGenie")


@app.get("/")
def root():
    return {"message": "Welcome to EduGenie"}


@app.get("/health")
def health():
    return {"status": "healthy"}