from dataclasses import dataclass

@dataclass
class UserPreferences:
    keywords: list
    category: str = "general"
    country: str = "us"
