from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    # Server
    HOST: str
    PORT: int
    DEBUG: bool
    # DB postgesql
    PG_NAME: str
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASS: str
    PG_DEBUG: bool

    class Config:
        env_file = ".env-local"
        env_file_encoding = "utf-8"
        env_prefix = "BACKEND_"

    @property
    def PG_URL(self):
        return f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_NAME}"

settings = AppSettings()