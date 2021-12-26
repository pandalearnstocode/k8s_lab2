from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/applicationlayer/app")
def read_main(request: Request):
    return {"ping": "pong", "root_path": "applicationlayer"}