import os
from pydantic_settings import BaseSettings

# credentials = {
#     "dbname": os.environ.get("DB_NAME"),
#     "user": os.getenv("DB_USER"),
#     "host": os.getenv("DB_HOST"),
#     "password": os.getenv("DB_PASSWORD"),
# }


class Settings(BaseSettings):
    # DATABASE_URL: str = (
    #     f"postgresql+psycopg2://{credentials['user']}:{credentials['password']}@{credentials['host']}/{credentials['dbname']}"
    # )
    VERSION: str = "1.0.0"
    PROJECT_NAME: str = "Scanner - Manager"
    DESCRIPTION: str = "Restful API -Scanner Manager"
    TIME_ZONE: str = "America/Los_Angeles"

settings = Settings()
