from itom.model.settings import Settings


def test_load_config_file() -> None:
    settings = Settings(
        app_name="Itom",
        app_author="Sebastian Führ",
        settings_file_path=f"{Settings.app_root_dir}/tests/data/test-settings.ini",
    )
    assert settings.name == "Test Settings"
