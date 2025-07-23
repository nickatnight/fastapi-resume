from pathlib import Path
from typing import Any

import yaml
from fastapi import APIRouter, FastAPI
from starlette.exceptions import HTTPException

from fastapi_resume.api.basic import create_basic_router
from fastapi_resume.api.contact import create_contact_router
from fastapi_resume.api.education import create_education_router
from fastapi_resume.api.experience import create_experience_router
from fastapi_resume.api.health import create_health_router
from fastapi_resume.api.projects import create_projects_router
from fastapi_resume.api.search import create_search_router
from fastapi_resume.api.skills import create_skills_router
from fastapi_resume.exceptions import (
    FileDoesNotExistError,
    FileIsNotYAMLError,
    FileReadError,
    custom_http_exception_handler,
)
from fastapi_resume.responses import ORJSONPrettyResponse


def create_api(data_file: str = "data.yaml") -> FastAPI:
    """Create a FastAPI app instance with the specified data file"""
    app = FastAPI(
        title="Resume API",
        description="An API for my resume",
        version="1.0.0",
        redoc_url="/docs",
        docs_url=None,
        default_response_class=ORJSONPrettyResponse,
    )
    router = APIRouter()

    def get_resume_data() -> dict[str, Any]:
        # always raise an HTTPException when loading data fails for api
        try:
            return load_resume_data(data_file)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # Include all section routers with the shared dependency
    router.include_router(create_basic_router(get_resume_data))
    router.include_router(create_experience_router(get_resume_data))
    router.include_router(create_education_router(get_resume_data))
    router.include_router(create_skills_router(get_resume_data))
    router.include_router(create_projects_router(get_resume_data))
    router.include_router(create_contact_router(get_resume_data))
    router.include_router(create_search_router(get_resume_data))
    router.include_router(create_health_router(data_file))

    app.include_router(router)
    app.add_exception_handler(HTTPException, custom_http_exception_handler)  # type: ignore

    return app


def load_resume_data(file_path: str) -> dict[str, Any]:
    """Load and parse the data.yaml file"""
    yaml_path = Path(file_path)

    if not yaml_path.exists():
        raise FileDoesNotExistError(f"{file_path} file not found")

    if not str(yaml_path).endswith(".yaml"):
        raise FileIsNotYAMLError(f"{file_path} is not a YAML file")

    data = None

    try:
        with open(yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except Exception as e:
        raise FileReadError(f"Error loading resume data: {str(e)}")

    return data  # type: ignore
