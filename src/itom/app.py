from typing import Optional

from model.settings import Settings


class App:
    def __init__(self, settings_file_path: Optional[str] = None) -> None:
        self.settings = Settings(
            app_name="Itom",
            app_author="Sebastian Führ",
            settings_file_path=settings_file_path,
        )


if __name__ == "__main__":
    App()
