from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_main():
    return {"ping": "pong", "root_path": "datalayer"}


subapi = FastAPI()


@subapi.get("/app")
def read_sub():
    return {"ping": "pong", "root_path": "datalayer/app"}


app.mount("/datalayer", subapi)