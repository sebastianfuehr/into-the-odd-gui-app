from dataclasses import dataclass
from datetime import datetime


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
