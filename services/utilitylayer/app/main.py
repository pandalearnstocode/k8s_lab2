from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_main():
    return {"ping": "pong", "root_path": "utilitylayer"}


subapi = FastAPI()


@subapi.get("/app")
def read_sub():
    return {"ping": "pong", "root_path": "utilitylayer/app"}


app.mount("/utilitylayer", subapi)