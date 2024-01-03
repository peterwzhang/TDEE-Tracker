import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def run_app():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True, workers=2)


if __name__ == "__main__":
    run_app()
