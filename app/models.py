from pydantic import BaseModel
from typing import List


class Planet_data(BaseModel):
    longitude: str
    latitude_shara: str
    speed: str
    nakshatra: str
    motion: str
    state: str
    # residing_in: str | None
    nakshatra_lord: str
    right_ascension: float = 0.00
    declination: float = 0.00
    raw_longitude: float = 0.00


class Planet(BaseModel):
    name: str
    planet_data: dict
