from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_main():
    return {"ping": "pong", "root_path": "applicationlayer"}


subapi = FastAPI()


@subapi.get("/app")
def read_sub():
    return {"ping": "pong", "root_path": "applicationlayer/app"}


app.mount("/applicationlayer", subapi)