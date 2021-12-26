from fastapi import FastAPI, Request

app = FastAPI(root_path="/ml_layer")


@app.get("/app")
def read_main(request: Request):
    return {"ping": "pong", "root_path": request.scope.get("root_path")}