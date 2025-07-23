from typer.testing import CliRunner

from fastapi_resume.cli import app


def test_cli_validate_happy_path(temp_yaml_file: str) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["validate", temp_yaml_file])
    assert result.exit_code == 0
    assert "All recommended fields present" in result.output


def test_cli_validate_sad_path(temp_txt_file: str) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["validate", temp_txt_file])
    assert result.exit_code == 1
    assert "Error validating file" in result.output

def test_cli_validate_file_does_not_exist_sad_path(temp_txt_file: str) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["validate", "does_not_exist.yaml"])
    assert result.exit_code == 1
    assert "❌ Error: Data file" in result.output


def test_cli_info_happy_path(temp_yaml_file: str) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["info", temp_yaml_file])
    assert result.exit_code == 0
    assert "❌ Error reading file" not in result.output


def test_cli_info_sad_path(temp_txt_file: str) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["info", temp_txt_file])
    assert result.exit_code == 1
    assert "❌ Error reading file" in result.output
