from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse
from Cookie.core.Items import items
from Cookie.core.model.Cookie import Cookie

router = APIRouter(
    prefix="/cookie/v1"
)

@router.get('/cookie_id/list')
async def read_cookie_list(start: int, length: int):
    cache = list()
    for index in range(length):
        if (start + index) >= len(items):
            break
        cache.append(items[start+index].asJsonInfo())

    hasNext = not (start + length >= len(items))
    last = start + length
    if not hasNext:
        last = None

    return {
            "list": cache,
            "last": last,
            "next": hasNext
        }

@router.get('/cookie_id/detail')
async def read_cookie_detail(cookie_id: int):
    for item in items:
        if item.cookie_id == cookie_id:
            return item.asJsonDetail()
    raise HTTPException(status_code=404, detail="Not Found Error")

@router.get('/cookie/image/{image}')
async def read_cookie_image(image: str):
    return FileResponse(
            f"Cookie/Resource/{image}", 
            filename=f"{image}", 
            media_type="image/png"
        )