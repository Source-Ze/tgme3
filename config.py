import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 21627756))

    API_HASH = os.environ.get("API_HASH", "fe77fbf0cae9f7f5ece37659e2466cf1")

    DEVLOO = os.environ.get("DEVLOO", "")
    
    MAX_ACCOUNTS = os.environ.get("MAX_ACCOUNTS", "")
    
    user_bot = os.environ.get("user_bot", "")
    
    id_bot = os.environ.get("id_bot", "")