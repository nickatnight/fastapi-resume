import os
import tempfile
from typing import Callable, Generator
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_simple_yaml_file_content() -> str:
    """Create a simple YAML file for testing"""
    return """
name:
  first: John
  middle:
  last: Doe
about: Test about section
position: Software Engineer
"""


@pytest.fixture
def mock_simple_txt_file_content() -> str:
    """Create a simple TXT file for testing"""
    return """
This is a simple TXT file for testing
"""


@pytest.fixture
def create_temp_file() -> Generator[Callable[[str, str], str], None, None]:
    """Create a reusable function for creating temporary files with automatic cleanup"""
    created_files = []

    def _create_temp_file(content: str, suffix: str = ".tmp") -> str:
        """Create a temporary file with given content and suffix"""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=suffix, delete=False
        ) as temp_file:
            temp_file.write(content)
            file_path = temp_file.name
            created_files.append(file_path)
            return file_path

    yield _create_temp_file

    # Clean up all created files
    for file_path in created_files:
        try:
            os.unlink(file_path)
        except OSError:
            pass  # File might already be deleted


@pytest.fixture
def temp_yaml_file(
    mock_simple_yaml_file_content: str, create_temp_file: MagicMock
) -> str:
    """Create a temporary YAML file for testing"""
    return create_temp_file(mock_simple_yaml_file_content, ".yaml")  # type: ignore


@pytest.fixture
def temp_txt_file(
    mock_simple_txt_file_content: str, create_temp_file: MagicMock
) -> str:
    """Create a temporary TXT file for testing"""
    return create_temp_file(mock_simple_txt_file_content, ".txt")  # type: ignore
