from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


def custom_http_exception_handler(request: Request, exc: HTTPException) -> Response:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "error_code": exc.status_code,
        },
    )


class BaseFastAPIResumeError(Exception):
    """Base exception for all FastAPI resume errors"""

    pass


class FileDoesNotExistError(BaseFastAPIResumeError):
    """Exception raised when the file does not exist"""

    pass


class FileIsNotYAMLError(BaseFastAPIResumeError):
    """Exception raised when the file is not a YAML file"""

    pass


class FileReadError(BaseFastAPIResumeError):
    """Exception raised when the file cannot be read"""

    pass
