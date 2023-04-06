from pydantic import BaseSettings

class Settings(BaseSettings):
    SUPABASE_CONN_STRING: str

    class Config:
        env_file = ".env"

# global instance
settings = Settings()