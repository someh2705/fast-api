from enum import Enum

class CookieType(Enum):
    DEFENSE = "방어형",
    CHARGE = "돌격형",
    PENETRATION = "침투형",
    EXPLOSION = "폭발형",
    MAGIC = "마법형",
    SUPPORT = "지원형",
    HEAL = "회복형",
    SHOOT = "사격형"