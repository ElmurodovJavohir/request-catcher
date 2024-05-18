import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from config.settings import MIDDLEWARE

if "whitenoise.middleware.WhiteNoiseMiddleware" not in MIDDLEWARE:
    MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
    }
)
