from fastapi.responses import FileResponse

from api.main import Gender

class Cookie:
    def __init__(
        self,
        cookie_id: int,
        cookie_name: str,
        cookie_image: FileResponse,
        gender: Gender
    ) -> None:
        pass
