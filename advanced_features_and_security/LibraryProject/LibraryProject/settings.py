import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Use env vars in production. Example fallback values shown for local dev only.
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# Restrict hosts in production
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1").split()

# Use a strong secret in production (read from env var)
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "insecure-dev-key-for-local")

# Cookies: only over HTTPS in production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Browser protections
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'   # prevents clickjacking
SECURE_HSTS_SECONDS = 31536000  # one year - enable only if HTTPS is correctly configured
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# If your site is behind a proxy (e.g. nginx), make sure to set:
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Content Security Policy (we'll set via middleware or django-csp)
CSP_DEFAULT_SRC = ("'self'",)
# add any other allowed origins (CDNs, analytics) in production:
CSP_SCRIPT_SRC = ("'self'",)  # extend as needed

# Recommended: disable debug-toolbar and any developer-only apps when DEBUG=False
INSTALLED_APPS = [
    # existing apps...
    'bookshelf',
]

MIDDLEWARE = [
    # existing middleware...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Custom CSP middleware (optional) - add after SecurityMiddleware
    'bookshelf.middleware.ContentSecurityPolicyMiddleware',
    # other middleware...
]

# Logging: log security related warnings to help auditing
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {
        'handlers': ['console'],
        'level': os.environ.get("DJANGO_LOG_LEVEL", "WARNING"),
    },
}

AUTH_USER_MODEL = 'bookshelf.CustomUser'
