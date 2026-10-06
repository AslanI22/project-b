"""Утилиты для работы с файлами."""

import json
import os


def read_file(path: str, encoding: str = "utf-8") -> str:
    """Читает содержимое текстового файла."""
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def write_file(path: str, content: str, encoding: str = "utf-8") -> None:
    """Записывает содержимое в файл, создавая папки при необходимости."""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding=encoding) as f:
        f.write(content)


def read_json(path: str) -> dict:
    """Читает JSON-файл и возвращает словарь."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: dict) -> None:
    """Записывает словарь в JSON-файл с отступами."""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)