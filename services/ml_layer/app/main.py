from fastapi import APIRouter

router = APIRouter(
    prefix="/ml",
    tags=["ml"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "Hello World"}