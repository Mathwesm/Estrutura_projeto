import os
from functools import wraps
from sys import stderr

from loguru import logger

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger.remove()


logger.add(stderr, format="{time} {level} {message} {file}", level="INFO")


logger.add(
    os.path.join(LOG_DIR, "meu_arquivo_do_logs.log"),
    format="{time} {level} {message} {file}",
    level="INFO",
)

logger.add(
    os.path.join(LOG_DIR, "meu_arquivo_do_logs_critical.log"),
    format="{time} {level} {message} {file}",
    level="CRITICAL",
)


def log_decorador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Chamando função '{func.__name__}' com args={args} e kwargs={kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise

    return wrapper
