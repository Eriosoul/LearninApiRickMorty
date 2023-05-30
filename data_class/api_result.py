from dataclasses import dataclass
from typing import Optional


@dataclass
class APIInfoData:
    count: int
    pages: int
    next: Optional[str]
    prev: Optional[str]


@dataclass
class APIResults:
    id: int
    name: str
    status: str
    species: str
    image: str
    # episode: list


@dataclass
class APILocation:
    name: str
    url: str


@dataclass
class APIAllInfoData:
    info: APIInfoData
    results: list[APIResults]
    location: APILocation
