from fastapi import APIRouter

router = APIRouter(
    prefix="/optimization",
    tags=["optimization"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "Hello World"}