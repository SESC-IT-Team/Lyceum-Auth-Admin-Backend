from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def return_ok():
    return {"status": "ok"}