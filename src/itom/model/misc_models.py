from dataclasses import dataclass
from datetime import date, datetime
from enum import IntEnum
from typing import Optional


class Die(IntEnum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20


@dataclass
class Note:
    creation_date: datetime
    text: str

    def repr_json(self) -> dict:
        return dict(
            __type__=Note.__name__,
            creation_date=self.creation_date,
            text=self.text,
        )


@dataclass
class Enterprise:
    creation_date: datetime
    name: str
    enterprise_type: str
    founding_date: Optional[date] = None
    income_level: Die = Die.D4
    description: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[list[Note]] = None

    def repr_json(self) -> dict:
        return dict(
            __type__=Enterprise.__name__,
            creation_date=self.creation_date,
            name=self.name,
            enterprise_type=self.enterprise_type,
            founding_date=self.founding_date,
            income_level=self.income_level,
            description=self.description,
            location=self.location,
            notes=self.notes,
        )
