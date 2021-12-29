from starlette.responses import FileResponse
from Cookie.core.model.Gender import CookieGender
from Cookie.core.model.Grade import CookieGrade
from Cookie.core.model.Skill import CookieSkill
from Cookie.core.model.Position import CookiePosition
from Cookie.core.model.Type import CookieType
from .model.Cookie import Cookie

items = [
    Cookie(
        cookie_id = 1,
        cookie_name = "용감한 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/brave-cookie.webp",
        cookie_grade = CookieGrade.COMMON,
        cookie_gender = CookieGender.MALE,
        cookie_type = CookieType.CHARGE,
        cookie_position = CookiePosition.FRONT,
        cookie_skill = CookieSkill(
            name="용감한 돌격",
            description="용감하게 돌진해 부딪히며 주변 범위에 피해를 입힌다."
        ),
    ),
    Cookie(
        cookie_id = 2,
        cookie_name = "딸기맛 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/strawberry-cookie.webp",
        cookie_grade = CookieGrade.COMMON,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = CookieType.DEFENSE,
        cookie_position = CookiePosition.FRONT,
        cookie_skill = CookieSkill(
            name="다가오지 마...",
            description="겁먹은 딸기맛 쿠키가 거대 롤리팝을 붙잡고 빙글빙글! 주변 범위에 지속적으로 피해를 입힌다."
        ),
    ),
    Cookie(
        cookie_id = 3,
        cookie_name = "마법사맛 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/wizard-cookie.webp",
        cookie_grade = CookieGrade.COMMON,
        cookie_gender = CookieGender.MALE,
        cookie_type = CookieType.MAGIC,
        cookie_position = CookiePosition.MIDDLE,
        cookie_skill = CookieSkill(
            name="번개구름 소환",
            description="마법진 위로 짜릿짜릿한 번개구름을 소환한다. 번개구름은 전진하며 마법진 위의 적에게 낙뢰를 뿌려 지속적인 범위 피해를 입힌다."
        ),
    ),
    Cookie(
        cookie_id = 4,
        cookie_name = "칠리맛 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/chili-pepper-cookie.webp",
        cookie_grade = CookieGrade.EPIC,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = CookieType.PENETRATION,
        cookie_position = CookiePosition.MIDDLE,
        cookie_skill = CookieSkill(
            name="발빠른 습격",
            description="바람처럼 빠른 몸놀림으로 후방의 적들을 기습해 범위 피해를 준다. 4연타의 마지막 검격은 반드시 독하디 독한 칠리맛 쿠키의 치명타가 적용된다."
        ),
    ),
    Cookie(
        cookie_id = 5,
        cookie_name = "커스터드 3세맛 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/custard-cookie.webp",
        cookie_grade = CookieGrade.RARE,
        cookie_gender = CookieGender.MALE,
        cookie_type = CookieType.HEAL,
        cookie_position = CookiePosition.BACK,
        cookie_skill = CookieSkill(
            name="훌륭한 왕",
            description="체력 비율이 가장 낮은 쿠키 둘을 골라 치료하고 잠시 동안 유지되는 보호막을 씌운다. 나는 훌륭한 왕이니까!"
        ),
    ),
    Cookie(
        cookie_id = 6,
        cookie_name = "퓨어바닐라 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/pure-vanilla-cookie.webp",
        cookie_grade = CookieGrade.ANCIENT,
        cookie_gender = CookieGender.MALE,
        cookie_type = CookieType.HEAL,
        cookie_position = CookiePosition.BACK,
        cookie_skill = CookieSkill(
            name="사랑과 평화",
            description="바닐라꽃 지팡이로 부드럽고 따뜻한 빛을 비춘다. 빛이 은은하고도 멀리 퍼져나가며 아군 전체의 체력을 회복시키고 최대 체력의 일정 비율만큼 체력 보호막을 생성한다."
        ),
    ),
    Cookie(
        cookie_id = 7,
        cookie_name = "홀리베리 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/hollyberry-cookie.webp",
        cookie_grade = CookieGrade.ANCIENT,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = CookieType.DEFENSE,
        cookie_position = CookiePosition.FRONT,
        cookie_skill = CookieSkill(
            name="방패에 건 맹세",
            description="함성ㅇ르 질러라! 베리-홀리 방패로 두려움 없이 돌진한다. 추가로 모든 아군 쿠키의 지속 피해, 간접 피해를 제외한 피해 일정량을 대신 흡수한다. 스킬 시전 시간 일부 중 스킬 끊김을 포함한 스킬 시전 방해 효과에 강해진다."
        ),
    ),
    Cookie(
        cookie_id = 8,
        cookie_name = "골드치즈 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/golden-cheese-cookie.webp",
        cookie_grade = CookieGrade.ANCIENT,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = CookieType.SHOOT,
        cookie_position = CookiePosition.BACK,
        cookie_skill = None
    ),
    Cookie(
        cookie_id = 9,
        cookie_name = "다크카카오 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/dark-cacao-cookie.webp",
        cookie_grade = CookieGrade.ANCIENT,
        cookie_gender = CookieGender.MALE,
        cookie_type = CookieType.CHARGE,
        cookie_position = CookiePosition.FRONT,
        cookie_skill = None,
    ),
    Cookie(
        cookie_id = 10,
        cookie_name = "세인트릴리 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/white-lily-cookie.webp",
        cookie_grade = CookieGrade.ANCIENT,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = CookieType.SUPPORT,
        cookie_position = CookiePosition.BACK,
        cookie_skill = None,
    ),
    Cookie(
        cookie_id = 11,
        cookie_name = "달빛술사 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/moonlight-cookie.webp",
        cookie_grade = CookieGrade.LEGENDARY,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = None,
        cookie_position = None,
        cookie_skill = None
    ),
    Cookie(
        cookie_id = 12,
        cookie_name = "바다요정 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/sea-fairy-cookie.webp",
        cookie_grade = CookieGrade.LEGENDARY,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = CookieType.EXPLOSION,
        cookie_position = CookiePosition.MIDDLE,
        cookie_skill = CookieSkill(
            name="솟구치는 마음",
            description="소환수를 제외한 가장 가까운 최대 다섯 적에게 물줄기를 쏘아 기절시키며, 일정 시간 후 물줄기가 만든 보름달 같은 웅덩이에서 영원의 힘을 담은 물기둥이 솟구쳐 큰 피해를 입힌다."
        )
    ),
    Cookie(
        cookie_id = 13,
        cookie_name = "불꽃정령 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/fire-spirit-cookie.webp",
        cookie_grade = CookieGrade.LEGENDARY,
        cookie_gender = CookieGender.MALE,
        cookie_type = None,
        cookie_position = None,
        cookie_skill = None
    ),
    Cookie(
        cookie_id = 14,
        cookie_name = "바람궁수 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/wind-archer-cookie.webp",
        cookie_grade = CookieGrade.LEGENDARY,
        cookie_gender = CookieGender.MALE,
        cookie_type = None,
        cookie_position = None,
        cookie_skill = None
    ),
    Cookie(
        cookie_id = 15,
        cookie_name = "천년나무 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/millennial-tree-cookie.webp",
        cookie_grade = CookieGrade.LEGENDARY,
        cookie_gender = CookieGender.MALE,
        cookie_type = None,
        cookie_position = None,
        cookie_skill = None
    ),
    Cookie(
        cookie_id = 16,
        cookie_name = "어둠마녀 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/dark-enchantress-cookie.webp",
        cookie_grade = CookieGrade.LEGENDARY,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = CookieType.MAGIC,
        cookie_position = None,
        cookie_skill = None
    ),
    Cookie(
        cookie_id = 17,
        cookie_name = "감초맛 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/licorice-cookie.webp",
        cookie_grade = CookieGrade.EPIC,
        cookie_gender = CookieGender.MALE,
        cookie_type = CookieType.MAGIC,
        cookie_position = CookiePosition.MIDDLE,
        cookie_skill = CookieSkill(
            name="해골 부르기",
            description="검은 번개의 환영으로 큰 피해와 함께 감초젤리 해골이 소환된다. 강력한 주술로 잠시 동안 아군의 방어력이 증가한다."
        )
    ),
    Cookie(
        cookie_id = 18,
        cookie_name = "독버섯맛 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/poison-mushroom-cookie.webp",
        cookie_grade = CookieGrade.LEGENDARY,
        cookie_gender = CookieGender.MALE,
        cookie_type = CookieType.EXPLOSION,
        cookie_position = CookiePosition.MIDDLE,
        cookie_skill = CookieSkill(
            name="보라버섯 독구름",
            description="주변으로 보랏빛 독을 퍼뜨리는 버섯을 심는다. 운 나쁘게 걸린 적들을 중독시켜 헤롱거리게 만들지만, 결코 악의는 없다나."
        )
    ),
    Cookie(
        cookie_id = 19,
        cookie_name = "석류맛 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/pomegranate-cookie.webp",
        cookie_grade = CookieGrade.EPIC,
        cookie_gender = CookieGender.FEMALE,
        cookie_type = CookieType.SUPPORT,
        cookie_position = CookiePosition.BACK,
        cookie_skill = CookieSkill(
            name="석류 주술",
            description="오싹한 주문도 우리 편일 땐 든든한 법! 붉은 주술을 사용하여 쿠키들의 체력을 조금씩 회복하고 잠시 동안 아군의 공격력이 증가한다."
        )
    ),
    Cookie(
        cookie_id = 20,
        cookie_name = "다크초코 쿠키",
        cookie_image = "http://localhost:8000/cookie/v1/cookie/image/dark-choco-cookie.webp",
        cookie_grade = CookieGrade.LEGENDARY,
        cookie_gender = CookieGender.MALE,
        cookie_type = None,
        cookie_position = None,
        cookie_skill = None
    ),
]