from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_main():
    return {"ping": "pong", "root_path": "mllayer"}


subapi = FastAPI()


@subapi.get("/app")
def read_sub():
    return {"ping": "pong", "root_path": "mllayer/app"}


app.mount("/mllayer", subapi)