"""
Модуль для налаштування логування
"""
import logging


def setup_logger(name: str) -> logging.Logger:
    """Налаштовує та повертає логер з базовою конфігурацією"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    return logging.getLogger(name)