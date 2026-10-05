"""Утилиты для работы с датами."""

from datetime import datetime


def get_current_date() -> str:
    """Возвращает текущую дату в формате YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")


def format_date(dt: datetime, fmt: str = "%d.%m.%Y") -> str:
    """Форматирует дату по заданному шаблону."""
    return dt.strftime(fmt)