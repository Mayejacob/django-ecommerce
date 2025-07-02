from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {"default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))}
