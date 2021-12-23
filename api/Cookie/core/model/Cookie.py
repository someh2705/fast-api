from fastapi.responses import FileResponse
from Cookie.core.model.Gender import CookieGender
from Cookie.core.model.Grade import CookieGrade
from Cookie.core.model.Skill import CookieSkill
from Cookie.core.model.Type import CookieType

class Cookie:
    def __init__(
        self,
        *,
        cookie_id: int,
        cookie_name: str,
        cookie_image: FileResponse,
        cookie_gender: CookieGender,
        cookie_type: CookieType,
        cookie_grade: CookieGrade,
        cookie_skill: CookieSkill
    ) -> None:
        self.cookie_id = cookie_id
        self.cookie_name = cookie_name
        self.cookie_image = cookie_image
        self.cookie_gender = cookie_gender
        self.cookie_type = cookie_type
        self.cookie_grade = cookie_grade
        self.cookie_skill = cookie_skill

    def asJsonInfo(self):
        return {
            "cookie_id": self.cookie_id,
            "cookie_name": self.cookie_name,
            "cookie_image": self.cookie_image,
            "cookie_gender": self.cookie_gender,
            "cookie_type": self.cookie_type,
            "cookie_grade": self.cookie_grade,
            "cookie_skill": self.cookie_skill,
        }