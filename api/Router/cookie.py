from fastapi import APIRouter

router = APIRouter(
    prefix="/cookie/v1"
)

@router.get('/cookie_id/{cookie_id}/info')
async def read_cookie(cookie_id: int):
    return {'cookie_id': cookie_id}