"""Тесты для file_utils."""

import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from file_utils import read_file, write_file, read_json, write_json


def test_write_and_read_file():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "test.txt")
        write_file(path, "hello")
        assert read_file(path) == "hello"


def test_write_json_creates_nested_dirs():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "nested", "dir", "data.json")
        write_json(path, {"key": "value", "число": 42})
        data = read_json(path)
        assert data["key"] == "value"
        assert data["число"] == 42