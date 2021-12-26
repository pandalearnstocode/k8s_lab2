from fastapi import APIRouter

router = APIRouter(
    prefix="/utility",
    tags=["utility"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "Hello World"}