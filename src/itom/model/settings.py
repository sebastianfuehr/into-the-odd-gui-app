from configparser import ConfigParser
from pathlib import Path
from typing import Optional

from appdirs import AppDirs


class Settings:
    """
    Attributes:
        app_root_dir(Path): The root directory of the application.
    """

    app_root_dir = Path(__file__).parent.parent.parent.parent

    def __init__(
        self, app_name: str, app_author: str, settings_file_path: Optional[str] = None
    ) -> None:
        """
        Args
            app_name: The name of the application.
            app_author: The name of the author or the organization
                which is publishing the application.
            settings_file_path: The file path for the config file. If not
                given, the application attempts to read from the system
                user settings directory. See appdirs directory for more
                info.
        """
        self.dirs = AppDirs(app_name, app_author)
        self.config = self.load_config_file(settings_file_path)
        self.load_settings()

    def load_config_file(
        self, settings_file_path: Optional[str] = None
    ) -> ConfigParser:
        default_config_path = f"{self.app_root_dir}/config/default.ini"
        if settings_file_path is not None:
            user_config = settings_file_path
        else:
            user_config = f"{self.dirs.user_config_dir}/settings.ini"
        config_parser = ConfigParser()

        if Path(user_config).is_file():
            config_parser.read(user_config)
        else:
            config_parser.read(default_config_path)
        return config_parser

    def load_settings(self) -> None:
        self.name = self.config["DEFAULT"]["settings_name"]
        self.data_dir = self.create_data_dir_path()

    def create_data_dir_path(self) -> str:
        """Checks whether the user settings overwrite the default data
        directory path. If not, sets the variable to be the default,
        relative path.
        """
        data_dir_usr_settings = self.config["directories"]["data_dir"]
        if len(data_dir_usr_settings) == 0:
            return f"{self.app_root_dir}/data/"
        else:
            return f"{self.app_root_dir}/{data_dir_usr_settings}"
