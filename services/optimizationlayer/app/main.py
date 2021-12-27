from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_main():
    return {"ping": "pong", "root_path": "optimizationlayer"}


subapi = FastAPI()


@subapi.get("/app")
def read_sub():
    return {"ping": "pong", "root_path": "optimizationlayer/app"}


app.mount("/optimizationlayer", subapi)