from typing import Any, Callable

from fastapi import APIRouter, Depends


def create_education_router(get_resume_data: Callable[[], dict[str, Any]]) -> APIRouter:
    """Create a router for education-related endpoints"""
    router = APIRouter()

    @router.get("/education")
    def get_education(
        resume_data: dict[str, Any] = Depends(get_resume_data),
    ) -> dict[str, Any]:
        """Get education information"""
        return {"education": resume_data.get("education", [])}

    return router
