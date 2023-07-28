from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    creation_date: datetime
    text: str
