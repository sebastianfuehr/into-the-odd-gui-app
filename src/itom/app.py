import json
from datetime import datetime
from typing import Optional

from controller.json_controller import ItomJSONDecoder, ItomJSONEncoder
from model.misc_models import Factory, Note
from model.settings import Settings


class App:
    def __init__(self, settings_file_path: Optional[str] = None) -> None:
        self.settings = Settings(
            app_name="Itom",
            app_author="Sebastian Führ",
            settings_file_path=settings_file_path,
        )

        note_date = datetime.now()
        notes = [Note(creation_date=note_date, text="Test Note")]

        date = datetime(2023, 7, 29).date()
        new_factory = Factory(
            creation_date=datetime.now(),
            name="Test Factory",
            acquisition_date=date,
            notes=notes,
        )
        json_file = json.dumps(new_factory.repr_json(), cls=ItomJSONEncoder)
        print(json_file)
        decoded_factory = json.loads(json_file, cls=ItomJSONDecoder)
        print(decoded_factory)


if __name__ == "__main__":
    App()
