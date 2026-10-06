"""Тесты для logger."""

import sys
import os
import tempfile
import logging

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from logger import get_logger, log_event


def test_logger_creates_file():
    with tempfile.TemporaryDirectory() as tmp:
        logger = get_logger("test_logger", log_dir=tmp)
        log_event(logger, "Hello log")
        log_file = os.path.join(tmp, "test_logger.log")
        assert os.path.exists(log_file)
        content = open(log_file, encoding="utf-8").read()
        assert "Hello log" in content

        # Важно: закрываем handler'ы, чтобы файл освободился (Windows)
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)