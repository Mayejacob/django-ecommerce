from .base import *

ALLOWED_HOSTS = [
    "ecommerce-bold-bird-4463.fly.dev",
]

DATABASES = {"default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))}
