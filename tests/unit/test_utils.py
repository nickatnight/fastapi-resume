import pytest

from fastapi_resume.exceptions import FileDoesNotExistError, FileIsNotYAMLError
from fastapi_resume.utils import load_resume_data


def test_load_resume_data_happy_path(temp_yaml_file: str) -> None:
    """Test loading a simple YAML file with name and about"""
    expected_data = {
        "name": {"first": "John", "middle": None, "last": "Doe"},
        "about": "Test about section",
        "position": "Software Engineer",
    }

    # Test the function with the temporary file
    result = load_resume_data(temp_yaml_file)
    assert result == expected_data


def test_load_resume_data_does_not_exist_sad_path() -> None:
    """Test loading a simple YAML file with name and about"""

    with pytest.raises(FileDoesNotExistError):
        load_resume_data("/does/not/exist.yaml")


def test_load_resume_data_is_not_yaml_sad_path(temp_txt_file: str) -> None:
    """Test loading a simple YAML file with name and about"""

    with pytest.raises(FileIsNotYAMLError):
        load_resume_data(temp_txt_file)
