<p align="center">
    <a href="https://github.com/nickatnight/fastapi-resume/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/fastapi-resume/actions/workflows/main.yaml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/nickatnight/fastapi-resume">
        <img alt="Coverage" src="https://codecov.io/gh/nickatnight/fastapi-resume/branch/main/graph/badge.svg?token=5yV0ottQ9o"/>
    </a>
    <a href="https://pypi.org/project/fastapi-resume/">
        <img alt="PyPi Shield" src="https://img.shields.io/pypi/v/fastapi-resume">
    </a>
    <a href="https://docs.astral.sh/uv/">
        <img alt="uv version" src="https://img.shields.io/badge/uv-0.7.18+-purple">
    </a>
    <a href="https://www.python.org/downloads/">
        <img alt="Python Versions Shield" src="https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white">
    </a>
    <!-- <a href="https://fastapi-resume.readthedocs.io/en/latest/"><img alt="Read The Docs Badge" src="https://img.shields.io/readthedocs/fastapi-resume"></a> -->
    <a href="https://github.com/nickatnight/fastapi-resume/blob/master/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/fastapi-resume">
    </a>
</p>

# fastapi-resume

A thin wrapper around FastAPI to expose your CV as a JSON REST API

## Usage

Install via pip

```sh
$ pip install fastapi-resume
```

## Usage

```sh
$ fast-resume --help
Usage: fast-resume [OPTIONS] COMMAND [ARGS]...

 FastAPI Resume API Server


╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ serve      Start the FastAPI Resume API server.                                                                                                                                          │
│ validate   Validate a YAML data file without starting the server.                                                                                                                        │
│ info       Display information about the resume data without starting the server.                                                                                                        │
╰───
```

### Basic (local)
See the [example](./fastapi_resume/templates/example.yaml) for a sample YAML file

```sh
$ fast-resume serve <my_data.yaml>
```

Then you can `curl` your new resume API:

```sh
$ curl http://localhost:8000/
```

## Documentation
See docs for more real word examples and how to deploy to your favorite cloud provider (Coming soon)
