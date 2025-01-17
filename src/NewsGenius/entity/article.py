from dataclasses import dataclass

@dataclass
class Article:
    title: str
    description: str
    url: str
    source: str
    author: str = "Unknown"
