import pytest
from environs import EnvError

from app.config import load_config


def test_load_config_reads_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "sqlite:///test.db")
    monkeypatch.setenv("SECRET_KEY", "test-secret")
    monkeypatch.setenv("DEBUG", "true")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    config = load_config()

    assert config.database_url == "sqlite:///test.db"
    assert config.secret_key == "test-secret"
    assert config.debug is True
    assert config.log_level == "DEBUG"


def test_load_config_fails_without_database_url(
    monkeypatch: pytest.MonkeyPatch, tmp_path
) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("SECRET_KEY", raising=False)

    empty_env = tmp_path / ".env"
    empty_env.write_text("")

    with pytest.raises(EnvError):
        load_config(path=str(empty_env))
