import os
from pydantic import BaseSettings

credentials = {
    "dbname": os.environ.get("DB_NAME_OP_USERS"),
    "user": os.getenv("DB_USER"),
    "host": os.getenv("DB_HOST"),
    "password": os.getenv("DB_PASSWORD"),
}


class Settings(BaseSettings):
    DATABASE_URL: str = (
        f"postgresql+psycopg2://{credentials['user']}:{credentials['password']}@{credentials['host']}/{credentials['dbname']}"
    )
    STORAGE_ACCOUNT_CS: str
    CONTAINER_NAME: str = "opsuser-manager-documents"
    VERSION: str = "1.0.0"
    PROJECT_NAME: str = "OPS User - Manager"
    DESCRIPTION: str = "Restful API - OPS User Manager"
    TIME_ZONE: str

    # Redis
    REDIS_OPERA_HOST: str
    REDIS_OPERA_DB: int = 0
    REDIS_EXP_KEY_SECONDS: int


settings = Settings()

redis_client = redis.Redis(
    host=settings.REDIS_OPERA_HOST,
    db=settings.REDIS_OPERA_DB,
)
