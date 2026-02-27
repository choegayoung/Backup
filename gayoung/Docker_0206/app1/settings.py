from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    kafka_topic: str = "test"
    kafka_server: str = "localhost:9092"
    mariadb_user: str = "team2"
    mariadb_password: str = "team2"
    mariadb_host: str = "db.quadecologics.cloud"
    mariadb_database: str = "team2"
    mariadb_port: int = 5050

    model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore")

settings = Settings()