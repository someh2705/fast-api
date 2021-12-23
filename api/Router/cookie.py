from fastapi import APIRouter, HTTPException
from Cookie.core.Items import items

router = APIRouter(
    prefix="/cookie/v1"
)

@router.get('/cookie_id/{cookie_id}/info')
async def read_cookie_info(cookie_id: int):
    for item in items:
        if item.cookie_id == cookie_id:
            return item.asJsonInfo()
    raise HTTPException(status_code=404, detail="Not Found Error")

@router.get('/cookie_id/{cookie_id}/detail')
async def read_cookie_detail(cookie_id: int):
    return {'cookie_id': cookie_id, 'detail': None}