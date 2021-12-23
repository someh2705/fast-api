from starlette.responses import FileResponse
from Cookie.core.model.Gender import CookieGender
from Cookie.core.model.Grade import CookieGrade
from Cookie.core.model.Skill import CookieSkill
from Cookie.core.model.Type import CookieType
from .model.Cookie import Cookie

items = [
    Cookie(
        cookie_id = 1,
        cookie_name = "용감한 쿠키",
        cookie_image = FileResponse(
            "../Resource/brave-cookie.webp", 
            filename="brave-cookie.webp", 
            media_type="image/webp"
        ),
        cookie_gender = CookieGender.MALE,
        cookie_type = CookieType.CHARGE,
        cookie_grade = CookieGrade.COMMON,
        cookie_skill = CookieSkill(
            name="용감한 돌격",
            description="용감하게 돌진해 부딪히며 주변 범위에 피해를 입힌다."
        ),
    )
]