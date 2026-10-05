"""Утилиты для работы с датами."""

from datetime import datetime


def get_current_date() -> str:
    """Возвращает текущую дату в формате DD.MM.YYYY (Dev A)."""
    return datetime.now().strftime("%d.%m.%Y")


def format_date(dt: datetime, fmt: str = "%d.%m.%Y") -> str:
    """Форматирует дату по заданному шаблону."""
    return dt.strftime(fmt)

def days_between(date1: datetime, date2: datetime) -> int:
    """Возвращает количество дней между двумя датами."""
    return abs((date2 - date1).days)