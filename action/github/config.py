from pydantic_settings import BaseSettings

class Config(BaseSettings):
    WHITE:str = "\033[37m"
    GREEN:str = "\033[32m"
    RESET_COLOR:str = "\033[0m"
    MODELT35:str = "gpt-3.5-turbo"
    MODELT4:str = "gpt-4-1106-preview"
    MODEL:str = "gpt-4-1106-preview"

    class Config:
        env_prefix = ''  # defaults to no prefix, i.e. ""