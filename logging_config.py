import logging
from logging.config import dictConfig


def setup_logging():
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "app.log",
                "formatter": "default",
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["console", "file"],
        },
        "loggers": {
            "uvicorn": {
                "level": "INFO",
                "handlers": ["console", "file"],
                "propagate": False,
            },
        },
    }
    dictConfig(logging_config)
    logging.getLogger("passlib").setLevel(logging.ERROR)
