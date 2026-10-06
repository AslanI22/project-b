# Project B — Utils Library

![CI](https://github.com/AslanI22/project-b/actions/workflows/ci.yml/badge.svg)

Библиотека утилит для работы с датами, строками, файлами и логированием.
Используется в проекте [project-a](https://github.com/AslanI22/project-a) через editable-установку.

## Установка

```bash
pip install -e .
```

Или как зависимость в другом проекте:

```bash
pip install -e /path/to/project-b
```

## Модули

### `date_utils`
| Функция | Описание |
|---|---|
| `get_current_date()` | Текущая дата в формате `YYYY-MM-DD` |
| `format_date(dt, fmt)` | Форматирование даты по шаблону |
| `days_between(d1, d2)` | Количество дней между датами |

### `string_utils`
| Функция | Описание |
|---|---|
| `reverse_string(s)` | Реверс строки |
| `capitalize_words(s)` | Title Case |
| `count_words(s)` | Число слов |
| `to_upper(s)` | Верхний регистр |

### `file_utils`
| Функция | Описание |
|---|---|
| `read_file(path)` / `write_file(path, content)` | Чтение/запись текста |
| `read_json(path)` / `write_json(path, data)` | Чтение/запись JSON |

### `logger`
| Функция | Описание |
|---|---|
| `get_logger(name, log_dir)` | Настроенный логгер (файл + консоль) |
| `log_event(logger, msg, level)` | Записать событие |

## Использование

```python
from project_b_utils import (
    get_current_date,
    reverse_string,
    read_json,
    get_logger,
)

print(get_current_date())          # 2026-10-06
print(reverse_string("hello"))     # olleh

logger = get_logger("my_app")
logger.info("Hello from logger")
```

## Тесты

```bash
pytest tests/ -v
```

6 тестов, покрывают все модули.

## CI/CD

GitHub Actions автоматически запускает тесты и сборку пакета при push в `main`.
Конфигурация — `.github/workflows/ci.yml`. Зависимости обновляются через Dependabot (`.github/dependabot.yml`).

## Структура

```
project-b/
├── .github/
│   ├── workflows/ci.yml
│   └── dependabot.yml
├── src/
│   ├── __init__.py
│   ├── date_utils.py
│   ├── string_utils.py
│   ├── file_utils.py
│   └── logger.py
├── tests/
│   ├── test_utils.py
│   ├── test_file_utils.py
│   └── test_logger.py
├── setup.py
├── README.md
└── .gitignore
```