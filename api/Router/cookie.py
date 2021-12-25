from fastapi import APIRouter, HTTPException
from Cookie.core.Items import items
from Cookie.core.model.Cookie import Cookie

router = APIRouter(
    prefix="/cookie/v1"
)

@router.get('/cookie_id/list')
async def read_cookie_list(start: int, length: int):
    if start + length >= len(items):
        raise HTTPException(status_code=404, detail="Out of Index")

    return list(map(Cookie.asJsonInfo, items[start:start+length+1]))

@router.get('/cookie_id/detail')
async def read_cookie_detail(cookie_id: int):
    for item in items:
        if item.cookie_id == cookie_id:
            return item.asJsonDetail()
    raise HTTPException(status_code=404, detail="Not Found Error")