from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env
load_dotenv()

class Settings(BaseSettings):
    database_hostname: str 
    database_port: str 
    database_password: str 
    database_name: str 
    database_username: str 
    secret_key: str 
    algorithm: str 
    access_token_expire_minutes: int 

    class Config:
        env_file = ".env"

# settings variable will save all the env variable info
settings = Settings()
#print(settings.database_name)
