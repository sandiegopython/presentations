# Django settings for demo_project project.

DEBUG = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ak5k0&*5l-5l2v=@tq*s%qdcuc=f2tkzr+&ca0rnzr&e3io)!o'

ROOT_URLCONF = 'demo_project.urls'

RAVEN_CONFIG = {
    'dsn': 'http://97bc1e8ab26240ecaffb28618d1713dd:392500d9ba054ae4a3e323617b2f19f6@localhost:8000/2',
}

# Add raven to the list of installed apps
INSTALLED_APPS = (
    # ...
    'raven.contrib.django.raven_compat',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
